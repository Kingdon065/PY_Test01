

def Sum(count, num):
    result = 0
    pre_num = 0
    for i in range(count):
        value = num * 10**i + pre_num
        print(value, end=' ')
        result += value
        pre_num = value
    
    print(f'30 {result} {result}')
    
s = input()
c, n = s.split()

Sum(int(c), int(n))