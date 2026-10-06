nums = [15, 33, 99, 111, 75, 90, 43, 65, 23, 47, 58, 95, 45, 85]
odd_nums = []
for num in nums:
  if num % 2 == 1 and num % 5 == 0:
    odd_nums.append(num)

print(odd_nums)
odd_nums2 = [num for num in nums if num % 2 == 1 and num % 5 == 0]
print(odd_nums2)