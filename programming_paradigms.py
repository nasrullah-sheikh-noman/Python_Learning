# Procedural Programming
nums = [32, 43, 12, 8, 45, 63]
result = []

for n in nums:
  if n % 2 == 0:
    result.append(n*2)

print(result)

# # Functional Programming
nums = [32, 43, 12, 8, 45, 63]

result = list(
  map(lambda n: n*2,
    filter(lambda n: n % 2 == 0, nums)
  ) 
)

print(result)

# Object Oriented Programming (OOP)
class NumberProcessor:
  def process(self, nums):
    return [
      n * 2 for n in nums
      if n % 2 == 0
    ]

processor = NumberProcessor()
print(processor.process([32, 43, 12, 8, 45, 63]))