def merge(array, start, mid, end):
    temp = [0]*(end-start)
    i, j, k = start, mid, 0
    while (i < mid and j < end):
        if array[i] <= array[j]:
            temp[k] = array[i]
            k += 1
            i += 1
        else:
            temp[k] = array[j]
            k += 1
            j += 1

    while (i < mid):
        temp[k] = array[i]
        k += 1
        i += 1

    while (j < end):
        temp[k] = array[j]
        k += 1
        j += 1

    for i in range(start, end):
        array[i] = temp[i-start]

    return array


def merge_sort(array, start, end):
    if (start < end-1):
        mid = int((start + end)/2)
        merge_sort(array, start, mid)
        merge_sort(array, mid, end)
        merge(array, start, mid, end)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected
