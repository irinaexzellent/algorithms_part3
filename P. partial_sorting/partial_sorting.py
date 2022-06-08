def find_count_segments(array):
    count = 1
    current_index = 0
    current_block_max = 0
    while current_index != len(array)-1:
        current_min = array[current_index+1]
        for j in range(current_index+1, len(array)):
            if array[j] < current_min:
                current_min = array[j]
        if current_block_max > 0:
            if current_block_max < current_min:
                count += 1
        elif array[current_index] < current_min:
            count += 1
        current_index += 1
        if array[current_index] > current_block_max:
            current_block_max = array[current_index]
    return count


if __name__ == '__main__':
    input()
    nums = list(map(int, input().split()))
    result = find_count_segments(nums)
    print(result)