import time
from typing import List

from utils import countdown


def main() -> List[int]:
    res = []
    for _ in range(10):
        res.append(countdown())

    return res


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f'=====================================================================')
    print(f'{__file__} executed in {elapsed:0.4f} seconds.')
    print(f'=====================================================================')
