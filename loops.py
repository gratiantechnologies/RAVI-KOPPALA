

#l=['jp',123,190035]

#j=list(range(5))
#print(j)
#for i in range(5):
  #  print(i)
 #   print(i*'*')

#for i in range(5):
 #   for j in range(4):
  #      print((i,j))

#for i in range(5):

 #   if i==4:
  #      break
   # print(i)
#print('you completed at 4')

#i=0
#while True:
 #   print('hey')
  #  i+=1
   # if i==5:
    #    break


#c=0
#while c<5:
 #   print(c)
  #  c+=1

#for i in range(10):
 #   print("python")

#ch=int(input("enter number: "))
#n1=0
#n2=1
#next=0
#for i in range(1, ch):
 #   if i==1:
  #      print(n1,end=',')
   # if i==2:
    #    print(n2,end=',')
    #next=n1+n2
    #n1=n2
    #n2=next
    #print(next,end=',')

#ch=int(input("enter number: "))
#i=1
#sum=0
#while i<=ch:
 #   sum=sum+i
  #  i+=1
#print(f"sum: {sum}")

#num1=float(input("enter first number: "))
#num2=float(input("enetr second number: "))

#if num1 > num2:
    #largest=num1
#elif num2 > num1:
   # largest=num2
#print("the largest no is: ",largest)

nl=[]
for x in range (1500,2000):
    if x%7==0 and x%5==0 :
        nl.append(str(x))
print(','.join(nl))

for i in range(10):
    print(str(i)*i)