import time
from concurrent.futures import ThreadPoolExecutor
from typing import Any, List, Dict

from io_ops.const import REQUEST_COUNT
from io_ops.utils import get_data_from_covidtracking, print_exec


def main() -> List[Dict[str, Any]]:
    with ThreadPoolExecutor(max_workers=REQUEST_COUNT) as executor:
        futures = [
            executor.submit(get_data_from_covidtracking) for _ in range(REQUEST_COUNT)
        ]

        return [f.result() for f in futures]


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print_exec(elapsed)
