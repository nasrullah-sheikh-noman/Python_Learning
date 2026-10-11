nums = [32, 89, 10, 34, 56, 90, 32, 46, 34, 8]

print(nums)

nums_set = set(nums)

print(nums_set)
nums_set.add(34)
print(nums_set)
nums_set.add(76)
print(nums_set)
nums_set.remove(8);
print(nums_set)

a = {3, 4, 8, 1, 32, 90}
b = {87, 4, 1, 76, 43}
print(a & b)
print(a not in b)
print(a in b)
print(a or b)
print(b or a)
print(a | b)