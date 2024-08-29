def common_elements() -> set[int]:
    first_range = set(range(0, 100, 3))
    second_range = set(range(0, 100, 5))
    return first_range.intersection(second_range)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")
