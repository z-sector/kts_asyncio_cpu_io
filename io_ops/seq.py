import time
from typing import Any, List, Dict

import requests


def main() -> List[Dict[str, Any]]:
    res = []
    for _ in range(10):
        res.append(
            requests.get('https://api.covidtracking.com/v1/us/current.json').json()
        )

    return res


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f'=====================================================================')
    print(f'{__file__} executed in {elapsed:0.4f} seconds.')
    print(f'=====================================================================')
