def funs_of_conference(id_university, count_universities):
    count_id_universities = {}
    for id in id_university:
        if id in count_id_universities:
            count_id_universities[id] += 1
        else:
            count_id_universities[id] = 1
    result = []
    for key, value in count_id_universities.items():
        result.append([-value, key])
    print(result)
    result.sort()
    result = result[:count_universities]
    result = [element[1] for element in result]
    return result


if __name__ == '__main__':
    input()
    id_universities = [int(item) for item in input().split()]
    count_universities = int(input())
    print(*funs_of_conference(id_universities, count_universities))