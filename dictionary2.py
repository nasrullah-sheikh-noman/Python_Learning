personInfo = {"name": "Noman", "age": 18, "district": "Sirajganj", "job": "Bekar"}
personInfo2 = [("name", "Nasrullah"), ("age", 24), ("district", "Tokeyo")]
personInfo2 = dict(personInfo2)

print(personInfo)
print(personInfo["job"])
print(personInfo.keys())
print(personInfo.values())
personInfo["language"] = "Python"
print(personInfo)
personInfo["name"] = "Nasrullah"
print(personInfo)
del personInfo["age"]
print(personInfo)
print(list(personInfo))
print(sorted(personInfo))
print(type(personInfo))
print(personInfo2)
print(type(personInfo2))

for x, y in personInfo2.items():
  print(x, y)

print(personInfo2)
del personInfo2["age"]
print(personInfo2)
personInfo2["Job"] = "Bekar"
print(personInfo2)