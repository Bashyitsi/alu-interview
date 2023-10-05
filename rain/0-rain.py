#!/usr/bin/python3
"""
0-rain
"""


def rain(walls):
    """
    Calculate how many square units of water will be retained between walls.

    :param walls: A list of non-negative integers representing wall heights.
    :type walls: List[int]
    :return: Integer indicating the total amount of rainwater retained.
    :rtype: int
    """
    if not walls or len(walls) < 3:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n
    water_trapped = 0

    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    for i in range(n):
        water_trapped += min(left_max[i], right_max[i]) - walls[i]

    return water_trapped

