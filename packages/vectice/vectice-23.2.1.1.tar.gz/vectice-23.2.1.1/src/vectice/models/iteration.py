from __future__ import annotations

import logging
from contextlib import suppress
from textwrap import dedent
from typing import TYPE_CHECKING

from rich.table import Table

from vectice.api.http_error_handlers import NoStepsInPhaseError, VecticeException
from vectice.api.json.iteration import (
    IterationInput,
    IterationStatus,
)
from vectice.utils.common_utils import _check_read_only, _get_step_type, _temp_print
from vectice.utils.last_assets import _get_last_user_and_default_workspace

if TYPE_CHECKING:
    from vectice import Connection
    from vectice.api import Client
    from vectice.models import Phase, Project, Step, Workspace
    from vectice.models.model import Model

_logger = logging.getLogger(__name__)


class Iteration:
    """Represent a Vectice iteration.

    Iterations reflect the model development and test cycles completed
    by data scientists until a fully functional algorithm is ready for
    deployment.  Each iteration contains the sequence of steps defined
    at the Phase and acts as a guardrail for data scientists to
    provide their updates.

    Typical usage example:

    ```python
    my_iteration = my_phase.iteration()

    my_iteration.step_cleaning = my_dataset
    # you can append assets of the same types (datasets/models) with +=
    my_iteration.step_cleaning += my_other_dataset

    my_iteration.step_model = my_model
    my_iteration.step_model += my_other_model
    ```

    If steps are added to a phase after iterations have been created
    and completed, these steps won't appear in these iterations.

    ```tree
    iteration 1
        step 1
        step 2
        step 3
    ```

    NOTE: **Phases and Steps Definitions are created in the Vectice App,
    Iterations are created from the Vectice Python API.**

    To create a new iteration:

    ```python
    my_iteration = my_phase.iteration()
    ```
    """

    __slots__ = [
        "_id",
        "_index",
        "_phase",
        "_status",
        "_client",
        "_model",
        "_current_step",
        "_steps",
        "__dict__",
    ]

    def __init__(
        self,
        id: int,
        index: int,
        phase: Phase,
        status: IterationStatus = IterationStatus.NotStarted,
    ):
        """Initialize an iteration.

        Vectice users shouldn't need to instantiate Iterations manually,
        but here are the iteration parameters.

        Parameters:
            id: The iteration identifier.
            index: The index of the iteration.
            phase: The project to which the iteration belongs.
            status: The status of the iteration.
        """
        self.__dict__ = {}
        self._id = id
        self._index = index
        self._phase = phase
        self._status = status
        self._client: Client = self._phase._client
        self._model: Model | None = None
        self._current_step: Step | None = None
        self._steps = self._populate_steps()

    def __repr__(self):
        steps = len(self.steps)
        return f"Iteration (index={self._index}, status={self._status}, No. of steps={steps})"

    def __eq__(self, other: object):
        if not isinstance(other, Iteration):
            return NotImplemented
        return self.id == other.id

    def _populate_steps(self):
        with suppress(NoStepsInPhaseError):
            return {step.slug: step for step in self.steps}
        return {}

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]
        if item in super().__getattribute__("_steps"):
            if not self._temp_type_filter(item):
                self._steps[item] = self.step(self._steps[item].name)
            return self._steps[item]
        raise AttributeError(f"The attribute '{item}' does not exist.")

    def __setattr__(self, attr_name, attr_value):
        if not (hasattr(self, attr_name) or attr_name in self.__slots__):
            raise AttributeError(f"The attribute '{attr_name}' does not exist.")
        elif hasattr(self, "_steps") and attr_name in super().__getattribute__("_steps"):
            if self._status in {IterationStatus.Abandoned, IterationStatus.Completed}:
                raise VecticeException(f"The Iteration is {self._status.name} and is read-only!")
            self._steps[attr_name] = self._steps[attr_name]._step_factory_and_update(value=attr_value)
        else:
            super().__setattr__(attr_name, attr_value)

    # TODO: remove this once StepModel is implemented
    def _temp_type_filter(self, slug: str) -> bool:
        """Temporary step type filter.

        Currently we rely on the model being set. Once StepModel is
        implemented we can remove this as we won't rely on the attributes being set.

        Parameters:
            slug: The step slug.

        Returns:
            A boolean.
        """
        if self._steps[slug]._model:
            return True
        return False

    @property
    def id(self) -> int:
        """The iteration's identifier.

        Returns:
            The iteration's identifier.
        """
        return self._id

    @id.setter
    def id(self, iteration_id: int):
        """Set the iteration's identifier.

        Parameters:
            iteration_id: The identifier.
        """
        _check_read_only(self)
        self._id = iteration_id

    @property
    def index(self) -> int:
        """The iteration's index.

        Returns:
            The iteration's index.
        """
        return self._index

    @property
    def completed(self) -> bool:
        """Whether this iteration is completed.

        Returns:
            Whether the iteration is completed.
        """
        return self._status is IterationStatus.Completed

    @property
    def properties(self) -> dict:
        """The iteration's identifier and index.

        Returns:
            A dictionary containing the `id` and `index` items.
        """
        return {"id": self.id, "index": self.index}

    @property
    def step_names(self) -> list[str]:
        """The names of the steps required in this iteration.

        Returns:
            The steps names.
        """
        return [step.name for step in self.steps]

    def step(self, step: str) -> Step:
        """Get a step by name.

        Step names are configured for a phase by the Vectice administrator.

        Parameters:
            step: The name of the step

        Returns:
            A step.
        """
        steps_output = self._client.get_step_by_name(step, self.id)
        _logger.debug(f"Step: {steps_output.name} successfully retrieved.")
        step_object = _get_step_type(
            id=steps_output.id,
            iteration=self,
            name=steps_output.name,
            index=steps_output.index,
            slug=steps_output.slug,
            description=steps_output.description,
            completed=steps_output.completed or None,
            artifacts=steps_output.artifacts,
            step_type=steps_output.step_type,
            text=steps_output.text,
        )
        self._current_step = step_object
        return step_object

    @property
    def steps(self) -> list[Step]:
        """The steps required in this iteration.

        Returns:
            The steps required in this iteration.
        """
        steps_output = self._client.list_steps(self._phase.id, self.index, self._phase.name)
        return [
            _get_step_type(
                id=item.id,
                iteration=self,
                name=item.name,
                index=item.index,
                slug=item.slug,
                description=item.description,
                completed=item.completed or None,
                artifacts=item.artifacts,
                step_type=item.step_type,
            )
            for item in sorted(steps_output, key=lambda x: x.index)
        ]

    def list_steps(self) -> None:
        """List the steps to which this iteration has access and print the steps in a tabular format.

        Returns:
            None
        """
        steps_output = sorted(self._client.list_steps(self.phase.id, self.index), key=lambda x: x.index)
        user_name, _ = _get_last_user_and_default_workspace(self._client)

        rich_table = Table(expand=True, show_edge=False)

        rich_table.add_column("step id", justify="left", no_wrap=True, min_width=5, max_width=5)
        rich_table.add_column("shortcut", justify="left", no_wrap=True, min_width=5, max_width=20)
        rich_table.add_column("artifacts", justify="left", no_wrap=True, min_width=5, max_width=15)
        rich_table.add_column("comment", justify="left", no_wrap=True, min_width=5, max_width=20)

        def _get_artifact_id(artifact) -> int | None:
            if artifact.dataset_version_id:
                return int(artifact.dataset_version_id)
            if artifact.model_version_id:
                return int(artifact.model_version_id)
            if artifact.entity_file_id:
                return int(artifact.entity_file_id)
            return None

        for count, step in enumerate(steps_output, 1):
            if count > 10:
                break
            step_text = step.text if step.text != "None" else None
            steps_started = False
            # TODO no artifacts, remove nested
            for number, artifact in enumerate(step.artifacts, 1):
                artifact_id = _get_artifact_id(artifact)
                if not steps_started:
                    rich_table.add_row(
                        str(step.id), step.slug, f"{number}. {artifact.type.value} {artifact_id}", step_text
                    )
                if steps_started:
                    rich_table.add_row(None, None, f"{number}. {artifact.type.value} {artifact_id}", None)
                steps_started = True
            if not step.artifacts:
                rich_table.add_row(
                    str(step.id),
                    step.slug,
                    None,
                    step_text,
                )
        if not steps_output:
            rich_table.add_row(
                None,
                None,
                None,
                None,
            )
        description = f"""There are {len(steps_output)} steps in iteration {self.index!r}."""
        tips = dedent(
            """
        >> To access a specific step, use iteration.step(Step ID)
        >> To access an array of steps, use iteration.steps"""
        ).lstrip()
        link = dedent(
            f"""
        For quick access to the list of steps in the Vectice web app, visit:
        {self._client.auth._API_BASE_URL}/project/phase/iteration?w={self.workspace.id}&iterationId={self.id}"""
        ).lstrip()

        _temp_print(description)
        _temp_print(table=rich_table)
        _temp_print(tips)
        _temp_print(link)

    def cancel(self) -> None:
        """Cancel the iteration by abandoning all unfinished steps."""
        iteration_input = IterationInput(status=IterationStatus.Abandoned.name)
        self._client.update_iteration(self.id, iteration_input)
        self._status = IterationStatus.Abandoned
        _logger.info(f"Iteration with index {self.index} canceled.")

    def complete(self) -> None:
        """Mark the iteration as completed."""
        if self._status is IterationStatus.Abandoned:
            raise VecticeException("The iteration is canceled and cannot be completed.")
        iteration_input = IterationInput(status=IterationStatus.Completed.name)
        self._client.update_iteration(self.id, iteration_input)
        self._status = IterationStatus.Completed
        _logger.info(f"Iteration with index {self.index} completed.")

    def delete(self) -> None:
        self._client.delete_iteration(self.id)
        _logger.info(f"Iteration with index {self.index} was deleted.")

    @property
    def connection(self) -> Connection:
        """The connection to which this iteration belongs.

        Returns:
            The connection to which this iteration belongs.
        """
        return self._phase.connection

    @property
    def workspace(self) -> Workspace:
        """The workspace to which this iteration belongs.

        Returns:
            The workspace to which this iteration belongs.
        """
        return self._phase.workspace

    @property
    def project(self) -> Project:
        """The project to which this iteration belongs.

        Returns:
            The project to which this iteration belongs.
        """
        return self._phase.project

    @property
    def phase(self) -> Phase:
        """The phase to which this iteration belongs.

        Returns:
            The phase to which this iteration belongs.
        """
        return self._phase
