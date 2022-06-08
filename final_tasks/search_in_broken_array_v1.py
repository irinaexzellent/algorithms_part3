#68704230
def broken_search(numbers, target) -> int:
    left = 0
    right = len(numbers)-1
    if right == 0:
        if numbers[0] == target:
            return 0
        return -1
    elif numbers[right] == target:
        return right
    while left <= right:
        mid = int((left + right) / 2)
        if numbers[mid] == target:
            return mid
        if numbers[left] <= numbers[mid]:
            if numbers[left] <= target and target <= numbers[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if numbers[mid] <= target and target <= numbers[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def test():
    array = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(array, 5) == 6
