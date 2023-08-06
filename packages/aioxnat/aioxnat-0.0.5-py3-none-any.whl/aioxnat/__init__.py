"""
Asyncronous XNAT RESTful Interface.
RESTful interface, from client to XNAT, for basic operations.
"""

__all__ = (
    (
        "AsyncRestAPI",
        "Experiment",
        "FileData",
        "Scan",
        "SimpleAsyncRestAPI"
    ))
__version__ = (0, 0, 5)

from aioxnat.protocols import AsyncRestAPI
from aioxnat.objects import FileData, Experiment, Scan
from aioxnat.rest import SimpleAsyncRestAPI
