n = 4
res = ["0" for i in range(n + 1)]
res[1] = "1"
# 对于每一个res子串
for i in range(2, n + 1):
    # 读出子串，判断它的形状
    pre_string = res[i - 1]
    # 遍历子串中的每一个字符
    for char_index, char in enumerate(pre_string):
        if char_index == 0:
            char_repeat = 1
            ans = []
        elif char != pre_string[char_index - 1]:
            # ans.append(str(char_repeat))
            # ans.append(char)
            char_repeat = 1
        else:
            char_repeat += 1
    ans.append(str(char_repeat))
    ans.append(char)
    res[i] = "".join(ans)
    print(i, res[i])