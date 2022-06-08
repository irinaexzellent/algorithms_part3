def area_difference(area_of_islands, number_difference):
    i = 0
    j = 1
    array_difference = []
    while start < end:
        mid = int((start + end) / 2)
        if mid > number_difference:
            end = mid - 1
            
        else:
            start = mid + 1
        
    i = start
    
    while i != end - 1:
        for j in range(i+1, end):
            difference = abs(area_of_islands[i] - area_of_islands[j])
            array_difference.append(difference)
        i += 1
    bubble_sort(array_difference)

    return array_difference[number_difference-1]
    


if __name__ == "__main__":
    number_of_islands = int(input())
    area_of_islands = [int(item) for item in input().split()]
    number_difference = int(input())
    print(area_difference(area_of_islands, number_difference))