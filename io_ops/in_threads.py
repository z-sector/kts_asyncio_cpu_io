import time
from concurrent.futures import ThreadPoolExecutor
from typing import Any, List, Dict

import requests


def get_data_from_covidtracking() -> Dict[str, Any]:
    return requests.get('https://api.covidtracking.com/v1/us/current.json').json()


def main() -> List[Dict[str, Any]]:
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(get_data_from_covidtracking) for _ in range(10)
        ]

        res = [f.result() for f in futures]

    return res


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f'=====================================================================')
    print(f'{__file__} executed in {elapsed:0.4f} seconds.')
    print(f'=====================================================================')
