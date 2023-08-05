import os
from pprint import pprint

from loguru import logger


def hello_world(*args, **kwargs):
    print("hello world")
    pprint(args)
    pprint(kwargs)


def list_files(dir: str = None):
    if dir is None:
        dir = os.path.abspath(os.path.dirname(__file__))
    logger.info(f"ls {dir}")
    pprint(os.listdir(dir))


if __name__ == "__main__":
    import fire

    fire.core.Display = lambda lines, out: print(*lines, file=out)
    fire.Fire(
        {
            "hello_world": hello_world,
            "list_files": list_files,
        }
    )
