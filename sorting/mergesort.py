"""Merge sort implementations."""
from typing import Sequence


def bottomup_merge_sort(arr):
    """Perform a bottom-up merge sort on a sequence of numbers.

    Args:
        arr: Sequence of numbers to be sorted.

    Returns:
        The provided sequence of numbers, sorted in ascending order.
    """
    pass


def topdown_merge_sort(arr):
    """Perform a top-down merge sort on a sequence of numbers.

    Args:
        arr: Sequence of numbers to be sorted.

    Returns:
        The provided sequence of numbers, sorted in ascending order.
    """
    result = []

    # If the array is empty or contains a single element, return it as is to
    # avoid un-necessary recursion. If it's a two element array, sort manually.
    if not arr:
        result = []
    elif len(arr) == 1:
        result = arr
    elif len(arr) == 2:
        result = [min(arr), max(arr)]
    else:
        middle = int(len(arr) / 2)
        left = arr[:middle]
        right = arr[middle:]

        # Recurse until the array contains a single element.
        left = merge_sort(left)
        right = merge_sort(right)

        left_index = 0
        right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                result.append(right[right_index])
                right_index += 1
            else:
                result.append(left[left_index])
                left_index += 1
        result += left[left_index:] + right[right_index:]

    return result


def main() -> None:
    """Script entrypoint."""
    res: Sequence = topdown_merge_sort([18, 12, 16, 22, 5, 24, 9])
    print(res)


if __name__ == "__main__":
    main()
