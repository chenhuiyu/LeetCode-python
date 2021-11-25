num = [10, 3, 7, 90, 99]
strNum = list(map(str, num))


def cmp(a, b):
    if a + b > b + a:
        return 1
    else:
        return -1


sorted(strNum, key=lambda x, y: x + y, y + x)
