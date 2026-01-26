def Addition(No1,No2):
    Ans=0
    Ans=No1+No2
    return Ans

def Subtraction(No1,No2):
    Ans=0
    Ans=No1-No2
    return Ans

def Multiplication(No1,No2):
    Ans=0
    Ans=No1*No2
    return Ans

def Division(No1,No2):
    Ans=0
    Ans=No1/No2
    return Ans

    
    
            
def main():
    Value1=int(input("Enter the 1st number : "))
    Value2=int(input("Enter the 2nd number : "))
    Ret=0
    Ret=Addition(Value1,Value2)
    print("Addition is : ",Ret)
    
    Ret=Subtraction(Value1,Value2)
    print("Subtraction is : ",Ret)
    
    Ret=Multiplication(Value1,Value2)
    print("Multiplication is : ",Ret)
    
    Ret=Division(Value1,Value2)
    print("Division is : ",Ret)
    
if __name__=="__main__":
    main()