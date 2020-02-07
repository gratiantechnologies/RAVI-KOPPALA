str1="my age "
str2= 18
print(str1+str (str2))

a=25
b=56
print("i am "+ str (a) + " and you are " + str (b))

print(f"i am {a} and you are {b} ")

s="python"
print(s[-1::-1])

str="python"
print(len(str))

str="python"
print(str.lower())

str='python'
print(str.upper())

str='i like python'
print(str.replace("like" , "love"))

str='i like python like'
print(str.replace("like","love",1))

str='python , java , php'
a,b,c=str.split(",")
print(a)
print(b)
print(c)

str="a"
if str.isalpha():
    print("this is a alphabet.")
else:
    print("not")

a="5"
if a.isdigit():
    print("this is a digit.")
else:
    print("not")

a="py"
if a.isspace():
    print("this is a spece.")
else:
    print("not")

a=5
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
if num1>num2:
    print("number 1 is greater.")
elif num1<num2:
    print("number 1 is smaller.")
elif num1<=num2:
    print("number 1 is equal to or smaller then 2")
elif num1==num2:
    print("both numbers are equal.")
else:
    print("enter correct number.")

