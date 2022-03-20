"""The models module contains the Board and the Task classes."""
from typing import Dict, Optional

from just_do_it_cli.config import (
    Status,
    PRIORITY_VALUES,
    INVALID_PRIORIY_VALUE_ERROR_MESSAGE,
)


class Board:  # pylint: disable=R0903
    """Board model class."""

    def __init__(
        self,
        id: str = None,  # pylint: disable=W0622
        name: str = None,
        tasks: dict = None,
    ) -> None:  # pylint: disable=W0622
        """
        Board model constructor.

        Args:
        ----
            id (str): The board ID.
            name (str): The name of the board.
            tasks (dict): A dictionary containing dictionaries of all the tasks
                which belongs to this board, or an empty dictionary if the
                board does not have tasks yet.
        """
        self.id = id  # pylint: disable=C0103
        self.name = name
        self.tasks = tasks if tasks is not None else {}

    def to_dict(self) -> Dict:
        """Return a dictionary representation of the board instance."""
        return {self.id: {'name': self.name, 'tasks': self.tasks}}


class Task:  # pylint: disable=R0903
    """Task model class."""

    def __init__(  # pylint: disable=R0913
        self,
        id: str = None,  # pylint: disable=W0622
        description: str = None,
        status: int = Status.PENDING,
        priority: int = 3,
        board_id: str = None,
    ) -> None:
        """
        Task model constructor.

        Args:
        ----
            id (str): The task ID.
            description (str): The description of task.
            status (int): The status of the task with the possible following
                values, `1` for `pending` or `2` for `in progress` or `3` for
                `done` as defined in `app.config.Status` class.
            priority (int): The task priority with the possible following
                values, `1` for `trivial` or `2`for `minor` or `3` for `major`
                or `4` for `critical` or `5` for `blocker`.
            board_id (str): The board ID which this task belongs to.
        """
        self.id = id  # pylint: disable=C0103
        self.description = description
        self.priority = priority
        self.status = status
        self.board_id = board_id

    @property
    def priority(self) -> int:
        """Return the value for priority attribute"""
        return self._priority

    @priority.setter
    def priority(self, value: int) -> Optional[None]:
        """
        Set the value for the priority attribute or raise
        `ValueError`
        """
        if value in PRIORITY_VALUES:
            self._priority = value
        else:
            raise ValueError(INVALID_PRIORIY_VALUE_ERROR_MESSAGE)

    def to_dict(self) -> Dict:
        """Return a dictionary representation of the task instance."""
        return {
            self.id: {
                'description': self.description,
                'priority': self.priority,
                'status': self.status,
            }
        }
