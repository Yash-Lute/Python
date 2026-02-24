class Arithematic:
    def __init__(self,A,B):
        self.No1=A
        self.No2=B
        print("Object gets greated successfully")
    
    def Addition(self):
        Ans=0
        Ans=self.No1+self.No2
        return Ans
    def Subtraction(self):
        Ans=0
        Ans=self.No1-self.No2
        return Ans
    
    
obj1=Arithematic(10,11) #Arithematic(id(obj1),11,10)  -> __init__(id(obj1),11,10)
obj2=Arithematic(21,20) #Arithematic(id(obj2),21,20)  -> __init__(id(obj2),21,10)

Ret=obj1.Addition()  #Addition(id(obj1))  -> Addition(1000)
print("Addition is : ",Ret)

Ret=obj2.Subtraction()  #Subtarction(id(obj2))  -> Subtraction(2000)
print("Subtraction is : ",Ret)