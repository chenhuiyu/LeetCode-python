num = [10, 3, 7, 90, 99]
strNum = list(map(str, num))


def cmp(a, b):
    if a + b > b + a:
        return 1
    else:
        return -1


import functools

ans = sorted(strNum, key=functools.cmp_to_key(cmp), reverse=True)

"".join(ans)
