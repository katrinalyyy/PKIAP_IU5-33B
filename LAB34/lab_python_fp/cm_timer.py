from contextlib import contextmanager
from typing import Any, Generator
import time


class Timer:
    def __enter__(self):
        self.IN = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.OUT = time.time() - self.IN
        print(self.OUT)


@contextmanager
def cm_timer() -> Generator[Any, Any, Any]:
    start = time.time()
    yield
    print(time.time() - start)


if __name__ == "__main__":
    pass
