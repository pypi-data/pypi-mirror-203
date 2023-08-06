from pathlib import Path

import os
import json

from .coretex import *

__version__ = 1


def getEnvVar(key: str, default: str) -> str:
    if os.environ.get(key) is None:
        os.environ[key] = default

    return os.environ[key]


DEFAULT_CONFIG = {
    "username": None,
    "password": None,
    "token": None,
    "refreshToken": None,
    "serverUrl": getEnvVar("CTX_API_URL", "https://devext.biomechservices.com:29007/"),
    "storagePath": getEnvVar("CTX_STORAGE_PATH", "~/.coretex"),

    # Configuration related to Coretex.ai Node
    "nodeName": None,
    "organizationID": "",
    "image": None
}


def syncConfigWithEnv() -> None:
    configPath = Path("~/.config/coretex/config.json").expanduser()

    # If configuration does not exist create default one
    if not configPath.exists():
        configPath.parent.mkdir(parents = True, exist_ok = True)

        with configPath.open("w") as configFile:
            json.dump(DEFAULT_CONFIG, configFile)

    # Load configuration and override environmet variable values
    with configPath.open("r") as configFile:
        config = json.load(configFile)

    os.environ["CTX_API_URL"] = config["serverUrl"]
    os.environ["CTX_STORAGE_PATH"] = config["storagePath"]
    os.environ["CTX_NODE_NAME"] = config["nodeName"]
    os.environ["CTX_ORGANIZATION_ID"] = config["organizationID"]


syncConfigWithEnv()
