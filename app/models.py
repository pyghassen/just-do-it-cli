from typing import Dict


class Board:
    def __init__(self, id=None, name=None, tasks={}) -> None:
        self.id = id
        self.id = id
        self.name = name
        self.tasks = tasks

    def to_dict(self) -> Dict:
        return {self.id: {'name': self.name, 'tasks': self.tasks}}


class Task:
    board_id = None

    def __init__(
            self,
            id=None,
            description=None,
            priority=3,
            status=1,
            board_id=None
        ) -> None:
        self.id = id
        self.description = description
        self.priority = priority
        self.status = status
        self.board_id = board_id

    def to_dict(self) -> Dict:
        return {
            self.id: {
                'description': self.description,
                'priority': self.priority,
                'status': self.status,
            }
        }
