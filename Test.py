# * dff
# ! 错误
# TODO 待做
# ？
# // 暂时不用
# python3.10测试

def cumsum(nums: list):
    result = []
    for i in range(len(nums)):
        value = sum(nums[:i+1])
        result.append(value)
    return result


lst = [1, 3, 5, 6]
print(cumsum(lst))

day = input()
if day.isdigit():
    day = int(day)
    total  = 1
    for i in range(day-1, 0, -1):
        total = (total + 1) * 2
    print(f'Day={day} Total={total}')