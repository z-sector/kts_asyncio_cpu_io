import time
from typing import List

from cpu_ops.const import CALL_COUNT
from cpu_ops.utils import countdown, print_exec


def main() -> List[int]:
    return [countdown() for _ in range(CALL_COUNT)]


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print_exec(elapsed)
