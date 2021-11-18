def add(a,b):
    # 无进位相加
    c=a^b
    # 进位
    cur=(a&b)<<1
    while(cur!=0):
        