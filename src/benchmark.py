import time


def benchmark(
        algorithm,
        text,
        pattern
):

    start = time.perf_counter()

    algorithm(
        text,
        pattern
    )

    end = time.perf_counter()

    return round(
        (end-start)*1000,
        5
    )