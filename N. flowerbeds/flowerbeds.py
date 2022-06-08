def resulting_flowerbeds(flowerbeds, count_flowerbeds):
    print(flowerbeds)
    flowerbeds.sort()
    print(flowerbeds)
    index = 0
    start, end = flowerbeds[index]
    results = []
    index += 1
    while index < count_flowerbeds:
        if start <= flowerbeds[index][0] <= end:
            current_end = flowerbeds[index][1]
            index += 1
            if current_end > end:
                end = current_end
        else:
            results.append([start, end])
            start, end = flowerbeds[index]
            index += 1
    results.append([start, end])
    return results



if __name__ == '__main__':
    count_flowerbeds = int(input())
    flowerbeds = [None]*count_flowerbeds
    for flowerbed in range(count_flowerbeds):
        start, end = map(int, input().split())
        flowerbeds[flowerbed] = [start, end]
    result = resulting_flowerbeds(flowerbeds, count_flowerbeds)
    for list in range (0, len(result)):
        print(*result[list])

 