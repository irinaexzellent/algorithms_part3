def brackets(count, s='', left=0, right=0):
    if left == count and right == count:
        print(s)
    else:
        if left < count:
            brackets(count, s + '(', left+1, right)
        if right < left:
            brackets(count, s + ')', left, right+1)


if __name__ == '__main__':
    brackets(int(input()))