num = [10, 3, 7, 90, 99]
strNum = list(map(str, num))
sorted(strNum, key=lambda x, y: x + y, y + x)
