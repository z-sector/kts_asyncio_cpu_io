from typing import Dict, Any

import requests


def get_data_from_covidtracking() -> Dict[str, Any]:
    return requests.get('https://api.covidtracking.com/v1/us/current.json').json()


def print_exec(elapsed: float) -> None:
    print(f'=====================================================================')
    print(f'Executed in {elapsed:0.4f} seconds.')
    print(f'=====================================================================')
