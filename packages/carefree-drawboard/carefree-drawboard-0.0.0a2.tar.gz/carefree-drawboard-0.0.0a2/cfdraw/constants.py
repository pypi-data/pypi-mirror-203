import os

from enum import Enum
from pathlib import Path

# global
DEFAULT_CONFIG_MODULE = "cfconfig"
DEFAULT_CONFIG_ENTRY = "config"
DEFAULT_MODULE = "app"
DEFAULT_ENTRY = "app"
API_VAR = "api"

# frontend
FRONTEND_PORT = "5123"

# api
ERR_CODE = 406
BACKEND_PORT = "8123"
DEV_BACKEND_HOST = "0.0.0.0"
API_HOST = "http://localhost"


class Endpoint(Enum):
    PING = "ping"
    WEBSOCKET = "ws"

    def __str__(self) -> str:
        return f"/{self.value}"

    __repr__ = __str__


# misc
class LogLevel(str, Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


# directories
## common
ROOT = Path(os.path.dirname(__file__))
WEB_ROOT = ROOT / ".web"
## upload
UPLOAD_ROOT = Path("~").expanduser() / ".cache" / "carefree-draw"
UPLOAD_IMAGE_FOLDER_NAME = ".images"
UPLOAD_PROJECT_FOLDER_NAME = ".projects"
PROJECT_META_FILE = "_meta.json"
