# index 0   1   2   3    4   5   6
nums = [32, 97, 43, 12, 534, 87, 54]
# index -7  -6  -5  -4   -3  -2    -1 

print(nums[3], nums[-4])

# n = len(nums)
# print(nums[0:len(nums)])

# print(nums[0:len(nums): 2])

# print(nums[len(nums)-1: : -1])

# print(nums[-len(nums): :1])

print(nums[:])
print(nums[::-1])


marks = [23, 87, 43, 12, 80, 45, 63, 71]
print(marks)
print(type(marks))

all = [32, 'c', True, "noman", 43.43]
print(all)

print(all[0:len(all):2])
print(all[3])

for val in all:
  print(val)

all2 = [51, True, "string", 64.87, 'c']

all2.append("Nasrullah")
all2.append(75)
all2.extend([90,21])
all2 += [76, 61]
all2.insert(2, 38)
print(51 in all2)
all2.clear()
print(all2,   len(all2))

