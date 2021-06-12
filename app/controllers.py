from typing import Dict

from app.models import Board, Task


class BoardController:
    model = Board

    def __init__(self, storage: Dict):
        self.storage = storage

    @classmethod
    def get_board_by_id(cls, storage, board_id):
        data = storage.read()
        return cls.model(id=str(board_id), **data[str(board_id)])

    def get_last_id(self):
        last_board_id = 0
        for board_id in self.storage.read():
            if last_board_id < int(board_id):
                last_board_id = int(board_id)
        return last_board_id

    def create(self, name):
        _id = self.get_last_id() + 1
        board = self.model(id=_id, name=name)
        data = self.storage.read()
        data.update(board.to_dict())
        self.storage.write(data)
        return board

    def edit(self, board_id, name):
        board = self.get_board_by_id(self.storage, board_id)
        board.name = name
        data = self.storage.read()
        data.update(board.to_dict())
        self.storage.write(data)
        return board

    def delete(self, board_id):
        data = self.storage.read()
        data.pop(str(board_id))
        self.storage.write(data)


class TaskController:
    model = Task

    def __init__(self, storage: Dict):
        self.storage = storage

    @classmethod
    def get_task_by_id(cls, storage, task_id):
        data = storage.read()
        task = None
        for board_id, board_data in data.items():
            for _task_id, task_data in board_data['tasks'].items():
                if _task_id == task_id:
                    task = cls.model(
                        id=str(task_id), board_id=board_id, **task_data
                    )
        return task

    def get_last_id(self):
        last_task_id = 0
        for board_data in self.storage.read().values():
            for task_id in board_data['tasks']:
                if last_task_id < int(task_id):
                    last_task_id = int(task_id)
        return last_task_id

    def create(self, board_id, description):
        _id = self.get_last_id() + 1
        task = self.model(id=str(_id), description=description)
        data = self.storage.read()
        data[board_id]['tasks'].update(task.to_dict())
        self.storage.write(data)
        return task

    def edit(self, id, description=None, status=None, priority=None):  # pylint: disable=W0622,C0103
        task = self.get_task_by_id(self.storage, id)

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

    def delete(self, id):  # pylint: disable=W0622,C0103
        task = self.get_task_by_id(self.storage, id)
        data = self.storage.read()
        data[task.board_id]['tasks'].pop(id)
        self.storage.write(data)
