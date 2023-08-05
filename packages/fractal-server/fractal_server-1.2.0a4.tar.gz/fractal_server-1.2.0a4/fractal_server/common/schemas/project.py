from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from pydantic import Field
from pydantic import validator
from sqlmodel import SQLModel

from ._validators import val_absolute_path
from ._validators import valstr


__all__ = (
    "ProjectCreate",
    "ProjectRead",
    "ProjectUpdate",
    "DatasetUpdate",
    "DatasetCreate",
    "DatasetRead",
    "ResourceCreate",
    "ResourceRead",
    "ResourceUpdate",
)


# RESOURCE


class _ResourceBase(SQLModel):
    """
    Base class for Resource
    """

    path: str


class ResourceCreate(_ResourceBase):
    # Validators
    _path = validator("path", allow_reuse=True)(val_absolute_path("path"))


class ResourceUpdate(_ResourceBase):
    # Validators
    _path = validator("path", allow_reuse=True)(val_absolute_path("path"))


class ResourceRead(_ResourceBase):
    id: int
    dataset_id: int


# DATASET


class _DatasetBase(SQLModel):
    """
    Base class for Dataset

    Attributes:
        name: TBD
        type: TBD
        meta: TBD
        read_only: TBD
    """

    name: str
    type: Optional[str]
    meta: Dict[str, Any] = Field(default={})
    read_only: bool = False


class DatasetUpdate(_DatasetBase):
    name: Optional[str]
    meta: Optional[Dict[str, Any]] = None
    read_only: Optional[bool]

    # Validators
    _name = validator("name", allow_reuse=True)(valstr("name"))
    _type = validator("type", allow_reuse=True)(valstr("type"))


class DatasetCreate(_DatasetBase):
    # Validators
    _name = validator("name", allow_reuse=True)(valstr("name"))
    _type = validator("type", allow_reuse=True)(valstr("type"))


class DatasetRead(_DatasetBase):
    id: int
    resource_list: List[ResourceRead]
    project_id: int
    read_only: bool


# PROJECT


class _ProjectBase(SQLModel):
    """
    Base class for Project

    Attributes:
        name: TBD
        read_only: TBD
    """

    name: str
    read_only: bool = False


class ProjectCreate(_ProjectBase):
    default_dataset_name: Optional[str] = "default"

    # Validators
    _name = validator("name", allow_reuse=True)(valstr("name"))
    _default_dataset_name = validator(
        "default_dataset_name", allow_reuse=True
    )(valstr("default_dataset_name"))


class ProjectRead(_ProjectBase):
    id: int
    dataset_list: List[DatasetRead] = []


class ProjectUpdate(_ProjectBase):
    name: Optional[str]
    read_only: Optional[bool]

    # Validators
    _name = validator("name", allow_reuse=True)(valstr("name"))
