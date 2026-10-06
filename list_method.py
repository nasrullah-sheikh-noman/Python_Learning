nums = [23, 42, 64, 84, 14, 93, 56, 72, 49, 62]
nums.append(332)
nums.insert(1, 100)
nums2 = [120, 180]
nums.extend(nums2)
if 1120 in nums:
  nums.remove(1120)
else:
  nums.append(1120)
print(nums.pop())
if 156 in nums:
  idx = nums.index(256)
  print(idx)
sort = sorted(nums)
print(sort)
sort.reverse();
print(sort)
print(nums)
nums.reverse()
print(nums)
