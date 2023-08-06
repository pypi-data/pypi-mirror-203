from __future__ import annotations

import logging
from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

from vectice.models.resource.metadata import DatasetType

if TYPE_CHECKING:
    from vectice.models.resource.metadata import DatasetSourceUsage, FilesMetadata

_logger = logging.getLogger(__name__)


class DataWrapper(metaclass=ABCMeta):
    """Deprecated. Base class for DataWrapper.

    WARNING: **Wrappers are deprecated.**
    Instead, use [`Dataset`][vectice.models.dataset.Dataset]
    and [`Resource`][vectice.models.resource.base.Resource].

    Use DataWrapper subclasses to assign datasets to steps.  The
    Vectice library supports a handful of common cases.  Additional
    cases are generally easy to supply by deriving from this base
    class.  In particular, subclasses must override this class'
    abstact methods (`_build_metadata()`, `_fetch_data()`).
    """

    @abstractmethod
    def __init__(
        self,
        name: str,
        usage: DatasetSourceUsage | None = None,
        derived_from: list[int] | None = None,
        type: DatasetType | None = None,
    ):
        """Initialize a data wrapper.

        Parameters:
            name: The name of the data wrapper.
            usage: The usage of the dataset.
            derived_from: The list of dataset ids to create a new dataset from.
            type: The type of the dataset.

        Raises:
            ValueError: When both `type` and `value` arguments are `None`.
        """
        if type is None:
            if usage is None:
                raise ValueError("'type' and 'usage' cannot be both None")
            type = DatasetType.MODELING

        elif type is DatasetType.MODELING and usage is None:
            raise ValueError(f"'usage' must be set when 'type' is {DatasetType.MODELING!r}")

        self._old_name = name
        self._name = name
        self._type = type
        self._usage = usage
        self._derived_from = derived_from
        self._metadata = None
        self._data = None

    @property
    def data(self) -> dict[str, bytes]:
        """The wrapper's data.

        Returns:
            The wrapper's data.
        """
        if self._data is None:
            self._data = self._fetch_data()  # type: ignore[assignment]
        return self._data  # type: ignore[return-value]

    @abstractmethod
    def _fetch_data(self) -> dict[str, bytes]:
        pass

    @abstractmethod
    def _build_metadata(self) -> FilesMetadata:
        pass

    @property
    def name(self) -> str:
        """The wrapper's name.

        Returns:
            The wrapper's name.
        """
        return self._name

    @name.setter
    def name(self, value):
        """Set the wrapper's name.

        Parameters:
            value: The wrapper's name.
        """
        self._name = value
        self._clear_data_and_metadata()

    @property
    def type(self) -> DatasetType:
        """The wrapper's dataset type.

        Returns:
            The wrapper's dataset type.
        """
        return self._type

    @property
    def usage(self) -> DatasetSourceUsage | None:
        """The wrapper's dataset usage.

        Returns:
            The wrapper's dataset usage.
        """
        return self._usage

    @property
    def derived_from(self) -> list[int] | None:
        """The datasets from which this wrapper is derived.

        Returns:
            The datasets from which this wrapper is derived.
        """
        return self._derived_from

    @property
    def metadata(self) -> FilesMetadata:
        """The wrapper's metadata.

        Returns:
            The wrapper's metadata.
        """
        if self._metadata is None:
            self.metadata = self._build_metadata()
        return self._metadata  # type: ignore[return-value]

    @metadata.setter
    def metadata(self, value):
        """Set the wrapper's metadata.

        Parameters:
            value: The metadata to set.
        """
        self._metadata = value

    def _clear_data_and_metadata(self):
        self._data = None
        self._metadata = None
