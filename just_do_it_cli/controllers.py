"""The controllers module contains the board and task controllers classes."""
from typing import Any

from just_do_it_cli.helpers import get_tasks
from just_do_it_cli.models import Board, Task


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
        return cls.model(id=board_id, **data['boards'][str(board_id)])

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
        data = self.storage.read()
        if data['last_board_id'] is not None:
            new_id = data['last_board_id'] + 1
        else:
            new_id = 1
        board = self.model(id=str(new_id), name=name)
        data['boards'].update(board.to_dict())
        data['last_board_id'] = new_id
        data['boards_index'].update({str(new_id): {'external_id': None}})
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
        data['boards'].update(board.to_dict())
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
        del data['boards'][board_id]
        data['last_board_id'] = (
            int(sorted(data['boards'].keys())[-1]) if data['boards'] else None
        )
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
        board_id = data['tasks_index'][task_id]['board_id']
        task_data = data['boards'][board_id]['tasks'][task_id]
        task = cls.model(id=task_id, board_id=board_id, **task_data)
        return task

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
        data = self.storage.read()
        if data['last_task_id'] is not None:
            new_id = data['last_task_id'] + 1
        else:
            new_id = 1
        data['last_task_id'] = new_id
        task = self.model(id=str(new_id), description=description)
        data['boards'][board_id]['tasks'].update(task.to_dict())
        data['tasks_index'].update(
            {str(new_id): {'board_id': board_id, 'external_id': None}}
        )
        self.storage.write(data)
        return task

    def edit(
        self,
        task_id: str,
        description: str = None,
        status: int = None,
        priority: int = None,
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
        data['boards'][task.board_id]['tasks'].update(task.to_dict())
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
        del data['boards'][task.board_id]['tasks'][task_id]
        tasks = get_tasks(data['boards'])
        data['last_task_id'] = int(sorted(tasks.keys())[-1]) if tasks else None
        del data['tasks_index'][task_id]
        self.storage.write(data)
