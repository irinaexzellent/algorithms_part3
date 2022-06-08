def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quickSort(arr, low, high):
    if low < high:
        pi=partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def big_triangle(array):
    array_lenght = len(array)
    quickSort(array, 0, array_lenght-1) 
    perimeter = -1
    for i in range(array_lenght-1, -1, -1):
        for j in range(i-1, -1, -1):
            for k in range(j-1, -1, -1):
                if array[i] < (array[j] + array[k]):
                    perimeter = array[i] + array[j] + array[k]
                    return perimeter
    return perimeter


if __name__ == "__main__":
    input()
    numbers = [int(item) for item in input().split()]
    print(big_triangle(numbers))
