def isSubsequence(string1, string2):
    start = -1
    for symbol in string1:
        start = string2.find(symbol, start + 1)
        if start == -1:
            return False
    return True


if __name__ == "__main__":
    string1 = str(input().split())
    string2 = str(input().split())
    print(isSubsequence(string1, string2))
