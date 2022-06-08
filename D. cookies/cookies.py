def count_satisfied(greed_factor, size_cookies):
    greed_factor.sort()
    size_cookies.sort()
    count_satisfied = 0
    next_cookie = 0
    index_factor = 0
    while index_factor != len(greed_factor):
        for cookie in range(next_cookie, len(size_cookies)):
            if size_cookies[cookie] >= greed_factor[index_factor]:
                next_cookie = cookie + 1
                count_satisfied += 1
                break
        index_factor += 1
    return count_satisfied


if __name__ == '__main__':
    input()
    greed_factor = [int(item) for item in input().split()]
    input()
    size_cookies = [int(item) for item in input().split()]
    print(count_satisfied(greed_factor, size_cookies))