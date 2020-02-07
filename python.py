a=10
b=15
print(a-b)
print(a**b)

a=10
a+=a
print(a)

x,y,z=7,5,9
if x>y and x>z:
    print("X is greaterthan y and z")
elif y>x and y>z:
    print("Y is greaterthan x and z")
else:
    print("Z is greaterthan x and y")

if x>y or y>z:
    print("X is greaterthan y and z")
else:
    print("Y is greaterthan x and z")

a=10
b=30
list1=[10,23,15,70,18]
if (a in list1):
    print("a is in list ")
else:
    print("a is not in list")

a=35
b=35
if (a is b):
    print("both are equal")
else:
    print("both are not equal")


a=8
b=7
c=a&b
print(c)

c=a|b
print(c)