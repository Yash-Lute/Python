def SumDigits(No):
    iDigit=0
    Sum=0
    while No!=0:
        iDigit=int(No%10)
        Sum=Sum+iDigit
        No=No/10
        
    return Sum

def main():
    Value=int(input("Enter the number : "))
    Ret=False
    Ret=SumDigits(Value)
    print("Sum of digits : ",Ret)
    
    
    
if __name__=="__main__":
    main()