from typing import Dict


class Board:
    def __init__(self, id=None, name=None, tasks=None) -> None:  # pylint: disable=W0622
        self.id = id  # pylint: disable=C0103
        self.name = name
        self.tasks = tasks if tasks is not None else {}

    def to_dict(self) -> Dict:
        return {self.id: {'name': self.name, 'tasks': self.tasks}}


class Task:
    board_id = None

    def __init__(  # pylint: disable=R0913
            self,
            id=None,  # pylint: disable=W0622
            description=None,
            priority=3,
            status=1,
            board_id=None
        ) -> None:
        self.id = id  # pylint: disable=C0103
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
