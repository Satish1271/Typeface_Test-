def base3(num):
    sign = '-' if num<0 else ''
    num = abs(num)
    st=''
    if num < 3:
        return str(num)
        st = ''
    while num != 0:
        st = str(num%3) + st
        num = num//3
    return sign+st
print(base3(10))
