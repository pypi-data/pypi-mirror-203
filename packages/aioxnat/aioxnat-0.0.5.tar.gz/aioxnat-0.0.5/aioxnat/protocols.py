import enum, functools
import abc, typing

import httpx

__all__ = (
    (
        "Ta",
        "Ps",
        "_AsyncChunkGenerator",
        "_GenericTypeFactory",
        "_MappingSeries",
        "_Validator",
        "AsyncRestAPI",
        "HasURI",
        "HasURL",
        "ResourceAction",
        "ProjectObject"
    ))

Ps = typing.ParamSpec("Ps")
Ta = typing.TypeVar("Ta")

_AsyncChunkGenerator = typing.AsyncGenerator[typing.Sequence[Ta], None]
_MappingSeries = typing.Sequence[typing.Mapping[str, str]]
_GenericTypeFactory = (
    typing.Callable[[type[Ta]], Ta] |
    typing.Callable[typing.Concatenate[type[Ta], Ps], Ta])
"""
Outline of callable which produces an object of
the given type.
"""

_Validator = (
    typing.Callable[[Ta], bool] |
    typing.Callable[typing.Concatenate[Ta, Ps], bool])
"""
Callable returning whether object passes
validation.
"""


def isvalidator(vfn: typing.Callable) -> bool:
    """
    Whether this callable is a validator.
    """

    return (callable(vfn) and getattr(vfn, "__is_validator__", False))


class HasURI(typing.Protocol):

    @property
    def URI(self) -> str:
        ...


class HasURL(typing.Protocol):

    @property
    def URL(self) -> str:
        ...


class ResourceAction(enum.Enum):
    REFRESH = enum.auto()
    DELETE = enum.auto()
    CREATE = enum.auto()


@typing.runtime_checkable
class ProjectObject(typing.Protocol):
    """
    An element in the heirarchy of an XNAT
    project.
    """

    __validators__: typing.Iterable[_Validator[typing.Self, Ps]] = () #type: ignore[valid-type]

    @functools.cached_property
    def is_valid(self):
        """
        Whether or not this `ProjectObject` is
        valid according to it's validators.
        """

        return all([vfn(self) for vfn in self.__validators__])

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """
        The name associated with this object.
        """

    @abc.abstractmethod
    def into_mapping(self) -> typing.Mapping[str, str]:
        """
        Transforms this object into a mapping of
        it's values.
        """

    @classmethod
    @abc.abstractmethod
    def from_mapping(cls, mapping: typing.Mapping[str, str]) -> typing.Self:
        """
        Transforms the given mapping into a this
        `ProjectObject` type.
        """

    @classmethod
    def insert_validator(cls, vfn: _Validator[typing.Self, Ps]) -> None:
        """
        Inserts a validator into this object's
        series of validators.
        """

        tmp = set(cls.__validators__)
        if vfn in tmp:
            raise ValueError("validator already included.")

        tmp.add(vfn) #type: ignore[arg-type]
        cls.__validators__ = tuple(tmp)

    @classmethod
    def remove_validator(cls, vfn: _Validator[typing.Self, Ps]) -> None:
        """
        Removes a validator from the series of
        validators.
        """

        tmp = set(cls.__validators__)
        if vfn not in tmp:
            raise ValueError("validator not in validators.")

        tmp.remove(vfn) #type: ignore[arg-type]
        cls.__validators__ = tuple(tmp)

    def __init_subclass__(cls):
        # Find and 'register' validators.
        for name in dir(cls):
            attr = getattr(cls, name, None)
            if not (attr and isvalidator(attr)):
                continue

            try:
                cls.insert_validator(attr)
            except ValueError:
                ... # validator already inserted.


class AsyncRestAPI(typing.Protocol):

    @property
    @abc.abstractmethod
    def URL(self) -> str:
        """
        URL pointing to the target host. This
        includes the protocol.
        """

    @abc.abstractmethod
    def get_experiments(self,
                        project_name: str,
                        *,
                        chunk_size: typing.Optional[int]
                        ) -> _AsyncChunkGenerator[ProjectObject]:
        """
        Retrieves experiment data from a
        particular project.
        """

    @typing.overload
    @abc.abstractmethod
    def get_scans(self,
                  experiment_or_project: str,
                  /) -> _AsyncChunkGenerator[ProjectObject]:
        ...

    @typing.overload
    @abc.abstractmethod
    def get_scans(self,
                  experiment_or_project: ProjectObject,
                  /) -> _AsyncChunkGenerator[ProjectObject]:
        ...

    @typing.overload
    @abc.abstractmethod
    def get_scans(self,
                  experiment_or_project: str,
                  *,
                  chunk_size: typing.Optional[int]
                  ) -> _AsyncChunkGenerator[ProjectObject]:
        ...

    @typing.overload
    @abc.abstractmethod
    def get_scans(self,
                  experiment_or_project: ProjectObject,
                  *,
                  chunk_size: typing.Optional[int]
                  ) -> _AsyncChunkGenerator[ProjectObject]:
        ...

    @abc.abstractmethod #type: ignore[misc]
    def get_scans(self,
                  experiment_or_project: ProjectObject | str,
                  *,
                  chunk_size: typing.Optional[int]
                  ) -> _AsyncChunkGenerator[ProjectObject]:
        """
        Retrieves scans related to a particular
        experiment.
        """

    @typing.overload
    @abc.abstractmethod
    async def resources(self, scan: ProjectObject, /) -> _MappingSeries:
        """Retrieves resources from a scan."""

    @typing.overload
    @abc.abstractmethod
    async def resources(self,
                        scan: ProjectObject,
                        name: str, /) -> typing.Sequence[ProjectObject]:
        """
        Retrieves resource data from a scan.
        """

    @typing.overload
    @abc.abstractmethod
    async def resources(self,
                        scan: ProjectObject,
                        name: str,
                        action: ResourceAction,
                        **params: str) -> None:
        """
        Perform the given action on a resource
        belonging to a scan.
        """

    @abc.abstractmethod
    async def resources(self,
                        scan: ProjectObject,
                        name: typing.Optional[str] = None,
                        action: typing.Optional[ResourceAction] = None,
                        **params: str
                        ) -> _MappingSeries | typing.Sequence[ProjectObject] | None:
        ...

    @classmethod
    @abc.abstractmethod
    def build_client(cls, api: typing.Self) -> httpx.Client:
        """Builds a raw client object."""

    @abc.abstractmethod
    async def __aenter__(self) -> typing.Self:
        ...

    async def __aexit__(self, *exc_details):
        ...
