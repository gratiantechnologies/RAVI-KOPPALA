dict1={"name":"ravi", "id":111,"branch":"CSE"}
print(dict1)
dict1["name"]="RAVI"
print(dict1)

print(dict1.keys())
print(dict1.values())
print(dict1.items())

dict2=dict1.copy()
print(dict2)


dict1.clear()
print(dict1)

for i in dict2.values():
    print(i)

print(len(dict2))

dict2["job"]="doveloper"
print(dict2)
dict2.popitem()
print(dict2)
