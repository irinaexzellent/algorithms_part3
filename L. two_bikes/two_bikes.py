def buying_bikes(cumulations, x, left, right):
    if cumulations[0] >= x:
        return 1
    if cumulations[1] >= x:
        return 2
    if x > cumulations[right]:
        return -1
    elif right == left:
        return left + 1
    mid = int((left + right) / 2)
    if cumulations[mid] < x:
        return buying_bikes(cumulations, x, mid+1, right)
    else:
        return buying_bikes(cumulations, x, left, mid)


if __name__ == '__main__':
    days = int(input())
    cumulations = [int(item) for item in input().split()]
    cost_of_bike = int(input())
    print(buying_bikes(cumulations, cost_of_bike, left = 0, right = days - 1), buying_bikes(cumulations, cost_of_bike * 2,  left = 0, right = days - 1))
    