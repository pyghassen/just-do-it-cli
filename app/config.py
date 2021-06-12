from environs import Env

env = Env()
env.read_env()
STORAGE_FILE_PATH = env('STORAGE_FILE_PATH')  # => raises error if not set
PRIORIY_ICONS_MAP = {1: '⛄', 2: '🌧️', 3: '🌊', 4: '🔥', 5: '🌋'}


class Status:
    PENDING = 1
    IN_PROGRESS = 2
    DONE = 3


class PendingTaskProperties:
    status = Status.PENDING
    icon = '◻'
    foreground_color = (46, 139, 87)
    strikethrough = None
    underline = None
    bold = None


class InProgressTaskProperties:
    status = Status.IN_PROGRESS
    icon = '…'
    foreground_color = (30, 144, 255)
    strikethrough = None
    underline = True
    bold = True


class DoneTaskProperties:
    status = Status.DONE
    icon = '✔'
    foreground_color = (220, 220, 220)
    strikethrough = True
    underline = None
    bold = None
