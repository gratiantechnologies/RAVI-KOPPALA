#class myclass:
 #   def __init__(self,name):
       # self.name=name
#c1=myclass("python")

#print(c1.name)

class myclass:
    def __init__(self):
        self.name='no name'

    def printname(self):
        self.name=input("enter your name: ")
        print("your name is: "+self.name)

c1=myclass()
c1.printname()