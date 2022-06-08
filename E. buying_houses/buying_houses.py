def efficient_quick_sort(array, start, end):
    if start >= end:
        return array
    pivot = array[end]
    left = start
    right = end - 1
    while left <= right:
        while left <= right and array[left] <= pivot:
            left += 1
        while left <= right and array[right] >= pivot:
            right -= 1
        if left < right:
            array[left], array[right] = array[right], array[left]
    array[left], array[end] = array[end], array[left]
    efficient_quick_sort(array, start, left-1)
    efficient_quick_sort(array, left+1, end)


def purchase_opportunity(count_houses_and_budget, cost_houses):
    common_count_houses = count_houses_and_budget[0]
    budget = count_houses_and_budget[1]
    summ = 0
    if common_count_houses == 1:
        if cost_houses[0] <= budget:
            return 1
        else:
            return 0
    efficient_quick_sort(cost_houses, 0, common_count_houses - 1)
    for index_house in range(0, common_count_houses):
        summ += cost_houses[index_house]
        if summ > budget:
            return index_house
    return common_count_houses


if __name__ == '__main__':
    count_houses_and_budget = [int(item) for item in input().split()]
    cost_houses = [int(item) for item in input().split()]
    print(purchase_opportunity(count_houses_and_budget, cost_houses))