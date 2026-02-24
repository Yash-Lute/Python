class Arithematic:
    def Addition(self,A,B):
        return A+B

    def Subtraction(self,A,B):
        return A-B
No1=0
No2=0
Ans=0

No1=int(input("Enter 1st number : "))
No2=int(input("Enter 2nd number : "))

Ans=Arithematic().Addition(No1,No2)
print("Addition is : ",Ans)

Ans=Arithematic().Subtraction(No1,No2)
print("Subtraction is : ",Ans)