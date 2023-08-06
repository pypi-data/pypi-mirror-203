import dataclasses, enum, functools, re, pathlib
import typing

from aioxnat.protocols import *

project_object_dataclass = dataclasses.dataclass(slots=True, frozen=True)


@typing.overload
def validator(**params) -> _Validator:
    ...


@typing.overload
def validator(vfn: _Validator, /) -> _Validator:
    ...


def validator(vfn: _Validator | None = None, **params):
    """
    Marks some callable as a validator function.
    """

    def wrapper(vfn: _Validator):

        @functools.wraps(vfn)
        def inner(*args, **kwds):
            return vfn(*args, **kwds)

        ret = functools.partial(inner, **params)
        setattr(ret, "__is_validator__", True)
        return ret

    if vfn:
        return wrapper(vfn)
    return wrapper


def _members(enumt: type[enum.StrEnum]):
    return enumt.__members__


class ScanQuality(enum.StrEnum):
    USABLE = enum.auto()
    GOOD = enum.auto()
    FAIR = enum.auto()
    QUESTIONABLE = enum.auto()
    POOR = enum.auto()
    UNUSABLE = enum.auto()
    UNDETERMINED = enum.auto()


class ScanSubType(enum.StrEnum):
    UNKNOWN = enum.auto()


class ScanTaskType(enum.StrEnum):
    UNKNOWN = enum.auto()


class BaseExperiment(ProjectObject):
    id: str
    label: str
    project: str

    @functools.cached_property
    def session_number(self): #NOTE: might be HCP specific.
        return ("2" if re.match(r"^.*_X1$", self.label) else "1")

    @functools.cached_property
    def name(self):
        return ":".join([self.project, self.id])

    def into_mapping(self):
        return dataclasses.asdict(self)

    @classmethod
    def from_mapping(cls, mapping: typing.Mapping[str, str]):
        parsed = dict(mapping)
        parsed["id"] = parsed.pop("xnat:subjectassessordata/id", "")
        parsed["subject_id"] = parsed.pop("subject_label", "")
        return cls(**parsed)

    @validator
    def _valid_id(self):
        return bool(re.match(r".*[a-zA-Z0-9].*", self.id))


@project_object_dataclass
class Experiment(BaseExperiment):
    id: str
    xsiType: str
    subject_id: str
    project: str
    label: str
    URI: str


class BaseScan(ProjectObject):
    id: str
    series_description: str
    experiment: Experiment

    __subtype_enum__: type[enum.StrEnum] = ScanSubType
    __tasktype_enum__: type[enum.StrEnum] = ScanTaskType

    @functools.cached_property
    def name(self):
        return ":".join([self.experiment.id, self.id, self.series_description])

    @functools.cached_property
    def subtype(self) -> enum.StrEnum:
        """
        Associated purpose of this scan in
        addition to the task type.
        """

        pattern = r"^.*_(%s).*$" % r"|".join(_members(self.__subtype_enum__).values())
        tmp = re.findall(pattern, self.series_description)

        try:
            return self.__subtype_enum__(tmp[0])
        except IndexError:
            return self.__subtype_enum__("UNKNOWN")

    @functools.cached_property
    def task(self) -> enum.StrEnum:
        """
        Associated task or purpose for which this
        scan was taken.
        """

        pattern = r"^.*(%s).*$" % r"|".join(_members(self.__tasktype_enum__).values())
        tmp = re.findall(pattern, self.series_description)

        try:
            return self.__tasktype_enum__(tmp[0])
        except IndexError:
            return self.__tasktype_enum__("UNKNOWN")

    def into_mapping(self):
        return dataclasses.asdict(self)

    @classmethod
    def from_mapping(cls, mapping: typing.Mapping[str, str]):
        parsed = dict(mapping)
        parsed.pop("xnat_imagescandata_id", None)
        parsed["id"] = parsed.pop("ID", "")
        parsed["data_type"] = parsed.pop("type", "")
        parsed["quality"] = ScanQuality(parsed["quality"])
        return cls(**parsed)

    def set_subtypes(self, enumt: type[enum.StrEnum]):
        """
        Sets the enumerator used to identify what
        the sub type of the scan could be.
        """

        if "UNKNOWN" not in _members(enumt):
            raise AttributeError("Enum type must have member 'UNKNOWN'.")
        self.__subtype_enum__ = enumt

    def set_tasktypes(self, enumt: type[enum.StrEnum]):
        """
        Sets the enumerator used to identify what
        the task type could be.
        """

        if "UNKNOWN" not in _members(enumt):
            raise AttributeError("Enum type must have member 'UNKNOWN'.")
        self.__tasktype_enum__ = enumt

    @validator
    def _valid_subtype(self):
        return (self.subtype.value != "UNKNOWN")

    @validator
    def _valid_tasktype(self):
        return (self.task.value != "UNKNOWN")


@project_object_dataclass
class Scan(BaseScan):
    id: str
    data_type: str
    series_description: str
    quality: ScanQuality
    URI: str
    experiment: Experiment


class BaseFileData(ProjectObject):
    URI: str

    @property
    def name(self):
        return pathlib.Path(self.URI).name

    def into_mapping(self):
        return dataclasses.asdict(self)

    @classmethod
    def from_mapping(cls, mapping: typing.Mapping[str, str]):
        parsed = dict(mapping)

        # Name attribute is unnecessary.
        parsed.pop("Name", "")

        parsed["cat_id"] = parsed.pop("cat_ID", "")
        parsed["content"] = parsed.pop("file_content", "")
        parsed["format"] = parsed.pop("file_format", "")
        parsed["size"] = parsed.pop("Size", "")
        parsed["tags"] = parsed.pop("file_tags", "")

        return cls(**parsed)


@project_object_dataclass
class FileData(BaseFileData):
    content: str
    size: str
    tags: str | tuple[str]
    cat_id: str
    digest: str
    collection: str
    format: str
    URI: str


ExperimentFactory = _GenericTypeFactory[Experiment, Ps]
"""
Callable which produces an `Experiment` object.
"""

ScanFactory = _GenericTypeFactory[Scan, Ps]
"""Callable which produces a `Scan` object."""
