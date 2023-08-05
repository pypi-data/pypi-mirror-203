import tomllib
import asyncio

from .event_loop import loop
from .handlers import load_handlers


async def mechanical_bull(config_file):
    with open(config_file, "rb") as fp:
        config = tomllib.load(fp)

    async with asyncio.TaskGroup() as taskgroup:
        for _, value in config.items():
            handlers = load_handlers(value["handlers"])
            taskgroup.create_task(loop(value, handlers))


def main():
    asyncio.run(mechanical_bull("config.toml"))


if __name__ == "__main__":
    main()
