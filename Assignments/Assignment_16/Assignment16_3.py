def Add(No1,No2):
    Ans=0
    Ans=No1+No2
    return Ans
def main():
    Value1=int(input("Enter 1st Number : "))
    Value2=int(input("Enter 2nd Number : "))
    Ret=0
    Ret=Add(Value1,Value2)
    print("Addition is : ",Ret)
    
    
if __name__=="__main__":
    main()