def bubble_sort(array):
    if len(array) == 2:
        if array[0] < array[1]:
            print(*array)
    indetical_element = all(item == array[0] for item in array)
    if indetical_element is True:
        print(*array)
        return
    else:
        for i in range(len(array) - 1):
            swapped = False
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swapped = True
            if not swapped:
                return
            print(*array)


if __name__ == "__main__":
    lenght = int(input())
    array = [int(item) for item in input().split()]
    bubble_sort(array)
