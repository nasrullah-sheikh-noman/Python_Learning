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