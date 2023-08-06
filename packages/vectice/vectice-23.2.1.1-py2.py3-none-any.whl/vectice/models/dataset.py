from __future__ import annotations

import logging
from datetime import datetime

from pandas import DataFrame

from vectice.models.property import Property
from vectice.models.resource.base import Resource
from vectice.models.resource.bigquery_resource import BigQueryResource
from vectice.models.resource.metadata.base import DatasetSourceUsage, DatasetType
from vectice.models.resource.metadata.db_metadata import DBMetadata
from vectice.models.resource.metadata.files_metadata import FilesMetadata
from vectice.models.resource.metadata.source import Source

_logger = logging.getLogger(__name__)


class Dataset:
    def __init__(
        self,
        type: DatasetType,
        name: str | None = None,
        resource: Resource | None = None,
        training_resource: Resource | None = None,
        testing_resource: Resource | None = None,
        validation_resource: Resource | None = None,
        derived_from: list[int | Dataset] | None = None,
        dataframe: DataFrame | None = None,
        training_dataframe: DataFrame | None = None,
        testing_dataframe: DataFrame | None = None,
        validation_dataframe: DataFrame | None = None,
        # attachments: str | list[str] | None = None,
        properties: dict[str, str | int] | list[Property] | Property | None = None,
    ):
        """Initialize a dataset.

        Users should not instantiate a dataset directly but rather use the provided static methods
        [`origin()`][vectice.models.dataset.Dataset.origin],
        [`clean()`][vectice.models.dataset.Dataset.clean], and
        [`modeling()`][vectice.models.dataset.Dataset.modeling].

        Parameters:
            type: The type of dataset.
            name: The name of the dataset.
            resource: A single resource (for origin and clean datasets).
            training_resource: The resource for the training set (for modeling datasets).
            testing_resource: The resource for the testing set (for modeling datasets).
            validation_resource: The resource for the validation set (optional, for modeling datasets).
            derived_from: A list of datasets (or ids) from which this dataset is derived.
            dataframe: A pandas dataframe for clean and origin datasets.
            training_dataframe: A pandas dataframe for modeling dataset.
            testing_dataframe: A pandas dataframe for modeling dataset.
            validation_dataframe: A pandas dataframe for modeling dataset.
            properties: A dict, for example `{"folds": 32}`.
        """
        derived_from_ids = []
        for df in derived_from or []:
            if isinstance(df, Dataset):
                if df.latest_version_id is None:
                    raise ValueError(
                        f"Dataset '{df.name}' does not have a version id. "
                        "Was it registered in Vectice (assigned to a step)?"
                    )
                derived_from_ids.append(df.latest_version_id)
            else:
                derived_from_ids.append(df)
        self._type = type
        self._name = name or f"dataset {datetime.time}"
        self._resource = resource
        self._training_resource = training_resource
        self._testing_resource = testing_resource
        self._validation_resource = validation_resource
        self._derived_from = derived_from_ids
        self._latest_version_id: int | None = None
        self._properties = self._format_properties(properties) if properties else None
        # self._attachments = self._format_attachments(attachments) if attachments else None

        if self._type is DatasetType.MODELING:
            if self._training_resource is None or self._testing_resource is None:
                raise ValueError("You cannot create a modeling dataset without both training and testing sets")

            self._training_resource.usage = DatasetSourceUsage.TRAINING
            self._testing_resource.usage = DatasetSourceUsage.TESTING
            if self._validation_resource:
                self._validation_resource.usage = DatasetSourceUsage.VALIDATION

        self._has_bigquery_resource = (
            isinstance(self._resource, BigQueryResource)
            or isinstance(self._training_resource, BigQueryResource)
            or isinstance(self._testing_resource, BigQueryResource)
            or isinstance(self._validation_resource, BigQueryResource)
            or isinstance(self.resource, BigQueryResource)
        )
        self._has_dataframe = (
            dataframe is not None
            or training_dataframe is not None
            or testing_dataframe is not None
            or validation_dataframe is not None
        )
        self._fill_file_dataframe(
            [
                (resource, dataframe, "dataframe"),
                (training_resource, training_dataframe, "training_dataframe"),
                (testing_resource, testing_dataframe, "testing_dataframe"),
                (validation_resource, validation_dataframe, "validation_dataframe"),
            ]
        )

    @staticmethod
    def origin(
        resource: Resource,
        name: str | None = None,
        dataframe: DataFrame | None = None,
        properties: dict[str, str | int] | list[Property] | Property | None = None,
        # attachments: str | list[str] | None = None,
    ) -> Dataset:
        """Create an origin dataset.

        Examples:
            ```python
            from vectice import Dataset, FileResource

            dataset = Dataset.origin(
                name="my origin dataset",
                resource=FileResource(path="origin_dataset.csv"),
            )
            ```

        Parameters:
            resource: The resource for the origin dataset.
            name: The name of the dataset.
            dataframe: A pandas dataframe allowing vectice to compute more metadata about this dataset.
            properties: A dict, for example `{"folds": 32}`.
        """
        return Dataset(
            type=DatasetType.ORIGIN,
            name=name,
            resource=resource,
            dataframe=dataframe,
            properties=properties,
            # attachments=attachments,
        )

    @staticmethod
    def clean(
        resource: Resource,
        name: str | None = None,
        derived_from: list[int | Dataset] | None = None,
        dataframe: DataFrame | None = None,
        properties: dict[str, str | int] | list[Property] | Property | None = None,
        # attachments: str | list[str] | None = None,
    ) -> Dataset:
        """Create a clean dataset.

        Examples:
            ```python
            from vectice import Dataset, FileResource

            dataset = Dataset.clean(
                name="my clean dataset",
                resource=FileResource(path="clean_dataset.csv"),
                properties: A dict, for example `{"folds": 32}`.
            )
            ```

        Parameters:
            resource: The resource for the clean dataset.
            name: The name of the dataset.
            derived_from: A list of datasets (or ids) from which this dataset is derived.
            dataframe: A pandas dataframe allowing vectice to compute more metadata about this dataset.
        """
        return Dataset(
            type=DatasetType.CLEAN,
            name=name,
            resource=resource,
            derived_from=derived_from,
            dataframe=dataframe,
            properties=properties,
            # attachments=attachments,
        )

    @staticmethod
    def modeling(
        training_resource: Resource,
        testing_resource: Resource,
        validation_resource: Resource | None = None,
        name: str | None = None,
        training_dataframe: DataFrame | None = None,
        testing_dataframe: DataFrame | None = None,
        validation_dataframe: DataFrame | None = None,
        properties: dict[str, str | int] | list[Property] | Property | None = None,
        # attachments: str | list[str] | None = None,
    ) -> Dataset:
        """Create a modeling dataset.

        Examples:
            ```python
            from vectice import Dataset, FileResource

            dataset = Dataset.modeling(
                name="my modeling dataset",
                training_resource=FileResource(path="training_dataset.csv"),
                testing_resource=FileResource(path="testing_dataset.csv"),
                validation_resource=FileResource(path="validation_dataset.csv"),
            )
            ```

        Parameters:
            training_resource: The resource for the training set (for modeling datasets).
            testing_resource: The resource for the testing set (for modeling datasets).
            validation_resource: The resource for the validation set (optional, for modeling datasets).
            name: The name of the dataset.
            training_dataframe: A pandas dataframe allowing vectice to compute more metadata about the training set.
            testing_dataframe: A pandas dataframe allowing vectice to compute more metadata about the testing set.
            validation_dataframe: A pandas dataframe allowing vectice to compute more metadata about the validation set.
            properties: A dict, for example `{"folds": 32}`.
        """
        return Dataset(
            type=DatasetType.MODELING,
            name=name,
            training_resource=training_resource,
            testing_resource=testing_resource,
            validation_resource=validation_resource,
            training_dataframe=training_dataframe,
            testing_dataframe=testing_dataframe,
            validation_dataframe=validation_dataframe,
            properties=properties,
            # attachments=attachments,
        )

    def __repr__(self):
        return f"Dataset(name={self.name!r}, type={self.type!r})"

    @property
    def type(self) -> DatasetType:
        """The dataset's type.

        Returns:
            The dataset's type.
        """
        return self._type

    @property
    def resource(self) -> Resource | tuple[Resource, Resource, Resource | None]:
        """The dataset's resource.

        Returns:
            The dataset's resource.
        """
        if self._type is DatasetType.MODELING:
            return self._training_resource, self._testing_resource, self._validation_resource  # type: ignore[return-value]
        return self._resource  # type: ignore[return-value]

    @property
    def name(self) -> str:
        """The dataset's name.

        Returns:
            The dataset's name.
        """
        return self._name

    @name.setter
    def name(self, name):
        """Set the dataset's name.

        Parameters:
            name: The name of the dataset.
        """
        self._name = name

    @property
    def derived_from(self) -> list[int]:
        """The datasets from which this dataset is derived.

        Returns:
            The datasets from which this dataset is derived.
        """
        return self._derived_from

    @property
    def latest_version_id(self) -> int | None:
        """The id of the latest version of this dataset.

        Returns:
            The id of the latest version of this dataset.
        """
        return self._latest_version_id

    @latest_version_id.setter
    def latest_version_id(self, value: int) -> None:
        """Set the id of the latest version of this dataset.

        Parameters:
            value: The id of the latest version of this dataset.
        """
        self._latest_version_id = value

    @property
    def properties(self) -> list[Property] | None:
        """The dataset's properties.

        Returns:
            The dataset's properties.
        """
        return self._properties

    @properties.setter
    def properties(self, properties: dict[str, str | int] | list[Property] | Property | None):
        """Set the dataset's properties.

        Parameters:
            properties: The properties of the dataset.
        """
        _logger.warning("To save your updated dataset properties, you must reassign your dataset to a step.")
        self._properties = self._format_properties(properties)

    # @property
    # def attachments(self) -> list[str] | None:
    #     """The attachments associated with the dataset.

    #     Returns:
    #         The attachments associated with the dataset.
    #     """
    #     return self._attachments

    # @attachments.setter
    # def attachments(self, attachments: list[str] | str):
    #     """Attach a file or files to the dataset.

    #     Parameters:
    #         attachments: The filename or filenames of the file or set of files to attach to the dataset.
    #     """
    #     self._attachments = self._format_attachments(attachments)

    @staticmethod
    def _check_key_duplicates(key_list: list[str]):
        if len(key_list) != len(set(key_list)):
            raise ValueError("Duplicate keys are not allowed.")

    # @staticmethod
    # def _format_attachments(attachments: str | list[str]) -> list[str]:
    #     return [attachment for attachment in set(attachments)] if isinstance(attachments, list) else [attachments]

    def _format_properties(self, properties: dict[str, str | int] | list[Property] | Property | None) -> list[Property]:
        if properties is None:
            return []
        if isinstance(properties, Property):
            return [properties]
        if isinstance(properties, list):
            properties = self._remove_incorrect_properties(properties)
            key_list = [prop.key for prop in properties]
            self._check_key_duplicates(key_list)
            return properties
        if isinstance(properties, dict):
            return [Property(key, str(value)) for (key, value) in properties.items()]
        raise ValueError("Please check property type.")

    def _fill_file_dataframe(self, resources: list[tuple[Resource | None, DataFrame | None, str]]):
        for resource, dataframe, arg in resources:
            if dataframe is not None and not isinstance(dataframe, DataFrame):
                raise ValueError(
                    f"Argument '{arg}' of type '{type(dataframe)}' is invalid, only pandas DataFrame is supported."
                )
            if resource is not None and dataframe is not None:
                if isinstance(resource.metadata, FilesMetadata):
                    source = self._get_latest_source(sources=list(resource.metadata.files))
                elif isinstance(resource.metadata, DBMetadata):
                    source = self._get_latest_source(sources=list(resource.metadata.dbs))
                if source is not None:
                    source._dataframe = dataframe

    def _get_latest_source(self, sources: list[Source]) -> Source | None:
        if len(sources) == 0:
            return None
        return sorted(sources, key=lambda source: source.name.lower())[0]

    @staticmethod
    def _remove_incorrect_properties(properties: list[Property]) -> list[Property]:
        for prop in properties:
            if not isinstance(prop, Property):
                _logger.warning(f"Incorrect property '{prop}'. Please check property type.")
                properties.remove(prop)
        return properties
