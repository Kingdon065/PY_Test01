
from random import randint

five_nums = []

for i in range(8):
    five_nums.append(randint(10000, 99999))

result = {}

for five_num in five_nums:
    s = str(five_num)
    one_nums = []
    for i in range(len(s)):
        one_nums.append(s[i])
    total = sum(map(int, set(one_nums)))
    if total in result:
        result[total].append(five_num)
    else:
        result[total] = [five_num]

max_key = max(result.keys())
print(five_nums)
print(result)
print(result[max_key])