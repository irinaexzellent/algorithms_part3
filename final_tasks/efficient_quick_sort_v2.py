#68723301
def efficient_quick_sort(participants, start, end):
    if start >= end:
        return participants
    pivot = participants[end]
    left = start
    right = end - 1
    while left <= right:
        while left <= right and participants[left] <= pivot:
            left += 1
        while left <= right and participants[right] >= pivot:
            right -= 1
        if left < right:
            participants[left], participants[right] = participants[right], participants[left]
    participants[left], participants[end] = participants[end], participants[left]
    efficient_quick_sort(participants, start, left-1)
    efficient_quick_sort(participants, left+1, end)


def info_about_participant(participants):
    participants[1] = - int(participants[1])
    participants[2] = int(participants[2])
    return [participants[1], participants[2], participants[0]]


if __name__ == '__main__':
    count_of_paticipants = int(input())
    participants = [info_about_participant(input().split())
                    for _ in range(count_of_paticipants)]
    start = 0
    efficient_quick_sort(participants, start, len(participants)-1)
    print(*(list(zip(*participants))[2]), sep='\n')
