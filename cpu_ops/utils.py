def countdown() -> int:
    i = 0
    while i < 5_000_000:
        i += 1

    return i


def print_exec(elapsed: float) -> None:
    print(f'=====================================================================')
    print(f'Executed in {elapsed:0.4f} seconds.')
    print(f'=====================================================================')
