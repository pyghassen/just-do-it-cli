"""
The config module contains all the needed configuration values.

STORAGE_FILE_PATH: The file path for the storage which will be loaded from
    `.env` file.
PRIORIY_ICONS_MAP: The map that contains the priority value along side with the
    icon which will be displayed.
Status: The class which holds status values.
PendingTaskProperties: The class which holds the configurations for a pending
    task.
InProgressTaskProperties: The class which holds the configurations for an in
    progress task.
DoneTaskProperties: The class which holds the configurations for a done task.
"""
from environs import Env

env = Env()
env.read_env()

STORAGE_FILE_PATH = env('STORAGE_FILE_PATH')  # => raises error if not set

PRIORIY_ICONS_MAP = {1: '⛄', 2: '🌧️', 3: '🌊', 4: '🔥', 5: '🌋'}


class Status:  # pylint: disable=R0903
    """
    Status class.

    The status class contains three attributes which are holding the values that
    it will be useed for status comparison, it will be saved to or read from the
    storage.
    """

    PENDING = 1
    IN_PROGRESS = 2
    DONE = 3


class PendingTaskProperties:  # pylint: disable=R0903
    """
    Pending task properties class.

    The pending task properties class holds all the configurations needed
    for display purposes.
    """

    status = Status.PENDING
    icon = '◻'
    foreground_color = (46, 139, 87)
    strikethrough = None
    underline = None
    bold = None


class InProgressTaskProperties:  # pylint: disable=R0903
    """
    In progress task properties class.

    The in progress task properties class holds all the configurations needed
    for display purposes.
    """

    status = Status.IN_PROGRESS
    icon = '…'
    foreground_color = (30, 144, 255)
    strikethrough = None
    underline = True
    bold = True


class DoneTaskProperties:  # pylint: disable=R0903
    """
    Done task properties class.

    The done task properties class holds all the configurations needed
    for display purposes.
    """

    status = Status.DONE
    icon = '✔'
    foreground_color = (220, 220, 220)
    strikethrough = True
    underline = None
    bold = None
