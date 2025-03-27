def minimum_latency_region(latencies: list, target: int) -> int:
    left = 0
    right = len(latencies) - 1

    while left <= right:
        middle = (left + right) // 2
        if target == latencies[middle]:
            return middle
        elif target < latencies[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return - 1

minimum_latency_region([15, 23, 34, 50, 60, 78], 15)