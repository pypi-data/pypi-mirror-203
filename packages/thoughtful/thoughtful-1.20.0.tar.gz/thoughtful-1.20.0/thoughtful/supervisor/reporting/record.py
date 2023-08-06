"""
This module contains the ``Record`` class, a non-user facing class that is used
to store information about a step's record. This class is represented in the
run report as a json object.

.. code-block:: json

    {
        "workflow": [
            {
                "step_id": "1.1",
                "step_status": "succeeded",
                "record": {
                    "id": "1",
                    "status": "succeeded"
                }
            }
        ]
    }

"""
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

from thoughtful.supervisor.reporting.status import Status


@dataclass
class Record:
    """
    A record can refer to any object that is being processed by a step. It
    is here represented by its ID and its status.
    """

    record_id: str
    """
    str: The status of the record.
    """

    status: Status
    """
    Status: The status of the record.
    """

    message: Optional[str] = field(default_factory=str)
    """
    Message: Place to store a message about the record. limit 120 characters
    """

    # make required default = {} ?
    metadata: Optional[dict] = field(default_factory=dict)
    """
    Metadata: Place to store metadata about the record.
    """

    def __json__(self):
        return {
            "id": self.record_id,
            "status": self.status.value,
            "message": self.message,
            "metadata": self.metadata,
        }
