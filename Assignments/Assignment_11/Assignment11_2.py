def CountDigits(No):
    iDigit=0
    iCount=0
    while No>=1:
        iDigit=No%10
        iCount=iCount+1
        No=No/10
        
    return iCount

def main():
    Value=int(input("Enter the number : "))
    Ret=False
    Ret=CountDigits(Value)
    print("No of digits : ",Ret)
    
    
    
if __name__=="__main__":
    main()