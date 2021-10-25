import time
from concurrent.futures import ProcessPoolExecutor
from typing import List

from cpu_ops.const import CALL_COUNT
from cpu_ops.utils import countdown, print_exec


def main() -> List[int]:
    with ProcessPoolExecutor(max_workers=CALL_COUNT) as executor:
        futures = [
            executor.submit(countdown) for _ in range(CALL_COUNT)
        ]

        return [f.result() for f in futures]


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print_exec(elapsed)
