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