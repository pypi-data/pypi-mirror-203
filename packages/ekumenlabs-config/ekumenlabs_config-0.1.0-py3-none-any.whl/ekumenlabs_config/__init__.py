from datetime import date

from .models import ConfigValue


async def get_bool_config(key: str) -> bool:
    return await ConfigValue.get_boolean(key)


async def get_int_config(key: str) -> int:
    return await ConfigValue.get_int(key)


async def get_float_config(key: str) -> float:
    return await ConfigValue.get_float(key)


async def get_string_config(key: str) -> str:
    return await ConfigValue.get_string(key)


async def get_date_config(key: str) -> date:
    return await ConfigValue.get_date(key)
