# def double(x):
#   return x*2;

double = lambda num : num * 2;
squred = lambda num : num ** 2;
add = lambda a, b : a + b;

res = double(4)
sqrt = squred(4)
sum = add(8, 4)
print(res, sqrt, sum)

nums = [32, 43, 12, 53, 64, 98, 76]

nums_map = map(double, nums)
print(nums)
print(list(nums_map))

actors = [
  {"name": "Sakib khan", "age": 50},
  {"name": "Arifin Shuvo", "age": 38},
  {"name": "Siam Ahmed", 'age': 34},
  {"name": "Afran Nisho", "age": 43}
]

juniors = filter(lambda actor: actor["age"] < 40, actors)
print(list(juniors))

seniors = filter(lambda actor: actor["age"] >= 40, actors)
print(list(seniors))