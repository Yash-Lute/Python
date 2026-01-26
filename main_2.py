def Multiplication(Value1,Value2):
    Ans=0     #local variable
    Ans=Value1*Value2
    return Ans


def main():
    
    
    No1=0
    No2=0
    Result=0

    No1=int(input("Enter 1st number : "))
    No2=int(input("Enter 2nd number : "))

    Result=Multiplication(No1,No2)
    print("Multiplication is :",Result) 

#Starter       
if __name__=="__main__":
    main()
    


   