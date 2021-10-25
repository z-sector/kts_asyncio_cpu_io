import time
from concurrent.futures.thread import ThreadPoolExecutor
from typing import List

from cpu_ops.utils import countdown, print_exec


def main() -> List[int]:
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(countdown) for _ in range(10)
        ]

        return [f.result() for f in futures]


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print_exec(elapsed)
