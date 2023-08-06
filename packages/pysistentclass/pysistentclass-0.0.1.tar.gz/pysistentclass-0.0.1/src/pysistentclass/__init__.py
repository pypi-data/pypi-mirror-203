from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List

from importlib import import_module

import json, yaml, toml

import inspect
import hashlib

import colorlog as logging 


def logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    myFormatter = logging.ColoredFormatter(log_colors={'DEBUG': 'yellow', 'INFO': 'reset', 'ERROR': 'bold_red'}, fmt="%(log_color)s%(levelname)s %(asctime)s " + name + " > %(message)s")
    handler = logging.StreamHandler()
    handler.setFormatter(myFormatter)
    logger.addHandler(handler)

    return logger


LOGGER = logger(__name__ + ".py")


class SettingsAttributeError(Exception):
    pass


skip_underscore_keys = lambda obj: {
    k: v for k, v in vars(obj).items() if not k.startswith("_")
}


json_pretty = lambda obj: json.dumps(obj, indent=4, sort_keys=True, default=vars)


class Format(str, Enum):
    deserializer: callable
    serializer: callable

    def __new__(
        cls, name: str, deserializer: callable = None, serializer: callable = None
    ) -> Format:
        obj = str.__new__(cls, name)
        obj._value_ = name
        obj.deserializer = deserializer
        obj.serializer = serializer
        return obj

    JSON = (
        "json",
        lambda s, object_hook: json.loads(s, object_hook=object_hook),
        lambda obj: json.dumps(obj, indent=4, sort_keys=True, default=vars),
    )
    YAML = ("yaml", yaml.safe_load, yaml.safe_dump)
    TOML = ("toml", toml.loads, toml.dumps)


class Scope(str, Enum):
    PUBLIC = "public"
    PRIVATE = "private"
    
    class _ScopeRepr:
        def __repr__(self) -> str:
            pass


@dataclass
class Entry:
    # _class: str
    # _module: str
    _scope: Scope
    _class_key: str
    # _key: str


@dataclass
class Settings(dict):
    settings_file: Path
    module_names: List[str] = field(default_factory=list)
    _classes: Dict[str, Dict[str, str]] = field(default_factory=dict)
    _settings: Dict[str, Entry] = field(default_factory=dict)
    format: Format = Format.JSON
    logging_level: int = logging.DEBUG

    def json_object_hook(self, obj: dict) -> Entry:
        if "_class_key" in obj:
            class_key = obj["_class_key"]
            module = import_module(self._classes[class_key]["module"])
            class_name = self._classes[class_key]["class_name"]
            if not hasattr(module, class_name):
                raise SettingsAttributeError(f"{module} does not have {class_name}")
            class_obj = getattr(module, class_name)
            return class_obj(**obj)
        return obj

    def __post_init__(self):
        LOGGER.setLevel(self.logging_level)
        LOGGER.debug(f"__post_init__()")
        LOGGER.debug(f"registering classes")
        class_keys_file = self.settings_file.parent / "classes.json"
        if not class_keys_file.exists():
            LOGGER.debug(f"creating {class_keys_file}")
            class_keys_file.write_text("{}")
        self._classes = json.loads(class_keys_file.read_text())

        LOGGER.debug(
            f"importing {len(self.module_names)} modules: {', '.join(self.module_names)}"
        )
        for mod_name in self.module_names:
            try: 
                module = import_module(mod_name)
            except ModuleNotFoundError as e:
                LOGGER.error(f"module '{mod_name}' not found")
                exit(1)
            classes = inspect.getmembers(
                module,
                lambda o: inspect.isclass(o)
                and issubclass(o, Entry)
                and o is not Entry,
            )
            for class_name, class_obj in classes:
                key = f"{mod_name}.{class_name}"
                key_hash = hashlib.md5(key.encode()).hexdigest()
                if key_hash in self._classes:
                    LOGGER.debug(f"o {key}")
                else:
                    LOGGER.debug(f"+ {key}")
                    self._classes[key_hash] = {
                        "module": mod_name,
                        "class_name": class_name,
                    }
            # print(self._classes)
        class_keys_file.write_text(json.dumps(self._classes, indent=4))
        if not self.settings_file.is_file():
            if self.settings_file.suffix == "":
                self.settings_file = self.settings_file.with_suffix(
                    f".{self.format.value}"
                )
            self.settings_file.touch()
        LOGGER.debug(f"defining settings")
        LOGGER.debug(f"format={self.format}")
        for class_key, module_class_dict in self._classes.items():
            module = import_module(module_class_dict["module"])
            class_obj = getattr(module, module_class_dict["class_name"])
            scope = getattr(class_obj, "_scope", Scope.PUBLIC)
            instance = class_obj(
                _class_key=class_key,
                _scope=scope,
            )
            LOGGER.debug(f"+ instance of {class_obj}")
            self._settings[module_class_dict["class_name"]] = instance

    def get(self, key: str) -> Entry:
        return self._settings[key]

    def write(self):
        serialized = self.format.serializer(self._settings)
        self.settings_file.write_text(serialized)

    def read(self):
        LOGGER.debug(f"reading settings {self.settings_file}")
        serialized = self.settings_file.read_text()
        default_serialized = self.format.serializer(self._settings)
        deserialized = {}
        try:
            if serialized:
                deserialized = self.format.deserializer(
                    serialized, self.json_object_hook
                )
        except SettingsAttributeError as e:
            LOGGER.debug(e)
        if serialized != default_serialized:
            LOGGER.debug("serialized != default_serialized")
        if not deserialized:
            LOGGER.debug("deserialized is None or empty using default settings!")
            deserialized = self._settings
        self._settings = deserialized
        self.public = {}
        self.private = {}
        for k, v in self._settings.items():
            if v._scope == Scope.PUBLIC:
                self.public[k] = v
            else:
                self.private[k] = v
        

    def __repr__(self) -> str:
        return json.dumps(
            self._settings, sort_keys=True, default=skip_underscore_keys, indent=4
        )
