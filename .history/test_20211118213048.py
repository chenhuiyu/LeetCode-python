n = 4
res = ["0" for i in range(n + 1)]
res[1] = "1"
# 对于每一个res子串
for i in range(2, n + 1):
    # 读出子串，判断它的形状
    pre_string = res[i - 1]
    # 遍历子串中的每一个字符
    for char_index, char in enumerate(pre_string):
        # 如果是首字符，repeat设为1
        if char_index == 0:
            char_repeat = 1
            ans = []
        # 如果和前一个字符不同，这是新字符，repeat重置为1
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