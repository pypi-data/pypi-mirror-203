import json
import logging
import typing
from datetime import date, datetime
from enum import Enum

from tortoise import Model, fields
from tortoise.exceptions import DoesNotExist

from .exceptions import ConfigurationError

logger = logging.getLogger(__name__)


class ConfigType(Enum):
    STRING = "s"
    INTEGER = "i"
    FLOAT = "f"
    BOOLEAN = "b"
    DATE = "d"


def _validate_or_raise(
    value: bool | int | float | str | date, type_obj: typing.Type, type_label: str
):
    if type(value) != type_obj:
        raise ValueError(f"Value >{value}< is not a {type_label}")


class ConfigValue(Model):
    id = fields.CharField(pk=True, max_length=128)
    type = fields.CharEnumField(
        enum_type=ConfigType,
        max_length=1,
    )
    data = fields.JSONField(null=False)

    @staticmethod
    async def create_bool(key: str, value: bool):
        _validate_or_raise(value, bool, "bool")
        await ConfigValue.create(
            id=key, type=ConfigType.BOOLEAN, data={"default": value}
        )

    @staticmethod
    async def create_integer(key: str, value: int):
        _validate_or_raise(value, int, "int")
        await ConfigValue.create(
            id=key, type=ConfigType.INTEGER, data={"default": value}
        )

    @staticmethod
    async def create_float(key: str, value: float):
        _validate_or_raise(value, float, "float")
        await ConfigValue.create(id=key, type=ConfigType.FLOAT, data={"default": value})

    @staticmethod
    async def create_string(key: str, value: str):
        _validate_or_raise(value, str, "str")
        await ConfigValue.create(
            id=key, type=ConfigType.STRING, data={"default": value}
        )

    @staticmethod
    async def create_date(key: str, value: date):
        _validate_or_raise(value, date, "date")
        await ConfigValue.create(
            id=key,
            type=ConfigType.DATE,
            data=json.dumps({"default": value}, indent=4, default=str),
        )

    @staticmethod
    async def __get_value(key: str, config_type: ConfigType):
        try:
            config = await ConfigValue.get(id=key)
        except DoesNotExist as e:
            raise ConfigurationError(f"Config '{key}' doesn't exist") from e
        if config.type != config_type:
            raise ConfigurationError(
                f"Config '{key}' is not of type {config_type.name}"
            )
        return config.data.get("value", config.data.get("default"))

    @staticmethod
    async def get_boolean(key: str) -> bool:
        return await ConfigValue.__get_value(key, ConfigType.BOOLEAN)

    @staticmethod
    async def get_int(key: str) -> int:
        return await ConfigValue.__get_value(key, ConfigType.INTEGER)

    @staticmethod
    async def get_float(key: str) -> float:
        return await ConfigValue.__get_value(key, ConfigType.FLOAT)

    @staticmethod
    async def get_string(key: str) -> str:
        return await ConfigValue.__get_value(key, ConfigType.STRING)

    @staticmethod
    async def get_date(key: str) -> date:
        return datetime.strptime(
            await ConfigValue.__get_value(key, ConfigType.DATE), "%Y-%m-%d"
        ).date()
