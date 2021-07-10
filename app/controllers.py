"""The controllers module contains the board and task controllers classes."""
from typing import Any

from app.models import Board, Task


class BoardController:
    """Board controller class."""

    model = Board

    def __init__(self, storage: Any) -> None:
        """
        Board controller constructor.

        Args:
        ----
            storage (JsonStorage): A JsonStorage instance.
        """
        self.storage = storage

    @classmethod
    def get_board_by_id(cls, storage: Any, board_id: str) -> Any:
        """
        Fetch board from the storage.

        Find the board dictionary in the provided storage and load it form it
        then return a board model instance.

        Args:
        ----
            storage (JsonStorage): A JsonStorage instance.
            board_id (str): The board ID.

        Returns
        -------
            A board model instance.
        """
        data = storage.read()
        return cls.model(id=board_id, **data[str(board_id)])

    def get_last_id(self):
        """
        Go through all the board IDs and return the last id.

        Returns
        -------
            Last board id as an integer.
        """
        last_board_id = 0
        for board_id in self.storage.read():
            if last_board_id < int(board_id):
                last_board_id = int(board_id)
        return last_board_id

    def create(self, name: str) -> Any:
        """
        Take a board name and return a board model instance.

        Create a board model instance, save its data to the storage then return.
        it.

        Args:
        ----
            name (str): The name of the board.

        Returns
        -------
            A board model instance.
        """
        _id = self.get_last_id() + 1
        board = self.model(id=_id, name=name)
        data = self.storage.read()
        data.update(board.to_dict())
        self.storage.write(data)
        return board

    def edit(self, board_id: str, name: str) -> Any:
        """
        Take board name and ID and return updated board model instance.

        Find a board by ID, update its data and save it to the storage then
        return the updated board model instance.

        Args:
        ----
            board_id (str): The board ID.
            name (str): The name of the board.

        Returns
        -------
            A board model instance.
        """
        board = self.get_board_by_id(self.storage, board_id)
        board.name = name
        data = self.storage.read()
        data.update(board.to_dict())
        self.storage.write(data)
        return board

    def delete(self, board_id: str) -> None:
        """
        Delete board.

        Find board by ID and delete it from the storage.

        Args:
        ----
            board_id (str): The board ID.
        """
        data = self.storage.read()
        del data[board_id]
        self.storage.write(data)


class TaskController:
    """Task controller class."""

    model = Task

    def __init__(self, storage: Any) -> None:
        """
        Task controller constructor.

        Args:
        ----
            storage (JsonStorage): A JsonStorage instance.
        """
        self.storage = storage

    @classmethod
    def get_task_by_id(cls, storage: Any, task_id: str) -> Any:
        """
        Fetch task from storage.

        Find task in provided the storage and load it then return it.

        Args:
        ----
            storage (JsonStorage): A JsonStorage instance.
            task_id (str): The task ID.

        Returns
        -------
            A task model instance.
        """
        data = storage.read()
        task = None
        for board_id, board_data in data.items():
            for _task_id, task_data in board_data['tasks'].items():
                if _task_id == task_id:
                    task = cls.model(
                        id=task_id, board_id=board_id, **task_data
                    )
        return task

    def get_last_id(self) -> int:
        """
        Get last task ID.

        Go through all the task IDs and return the last id.

        Returns
        -------
            Last task id as an integer.
        """
        last_task_id = 0
        for board_data in self.storage.read().values():
            for task_id in board_data['tasks']:
                if last_task_id < int(task_id):
                    last_task_id = int(task_id)
        return last_task_id

    def create(self, board_id: str, description: str) -> Any:
        """
        Take board ID and task description and return task model instance.

        Create a task model instance, save its data to the storage then return
        it.

        Args:
        ----
            board_id (str): The board ID that the task belongs to.
            description (str): The description of task.

        Returns
        -------
            A task model instance.
        """
        _id = self.get_last_id() + 1
        task = self.model(id=str(_id), description=description)
        data = self.storage.read()
        data[board_id]['tasks'].update(task.to_dict())
        self.storage.write(data)
        return task

    def edit(
            self,
            task_id: str,
            description: str = None,
            status: int = None,
            priority: int = None
        ) -> Any:  # pylint: disable=W0622,C0103
        """
        Take description or status or priority then return the updated task.

        Find a task by ID, update its data and save it to the storage then
        return the updated task instance.

        Args:
        ----
            task_id (str): The task ID.
            description (str): The description of task.
            status (int): The status of the task whether (1) pending or
                (2) in progress or (3) done as defined in app.config.Status
                class.
            priority (int): The task priority whether (1) trivial or (2) minor
                or (3) major or (4) critical or (5) blocker.

        Returns
        -------
            A task model instance.
        """
        task = self.get_task_by_id(self.storage, task_id)

        if description is not None:
            task.description = description
        elif status is not None:
            task.status = status
        else:
            task.priority = priority
        data = self.storage.read()
        data[task.board_id]['tasks'].update(task.to_dict())
        self.storage.write(data)
        return task

    def delete(self, task_id: str) -> None:  # pylint: disable=W0622,C0103
        """
        Delete task.

        Find task by ID and delete it from the storage.

        Args:
        ----
            task_id (str): The task ID.
        """
        task = self.get_task_by_id(self.storage, task_id)
        data = self.storage.read()
        del data[task.board_id]['tasks'][task_id]
        self.storage.write(data)
