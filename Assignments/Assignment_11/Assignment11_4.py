def DisplayRev(No):
    iDigit=0
    
    while No!=0:
        iDigit=No%10
        print(iDigit)
        No=int(No/10)
        
    

def main():
    Value=int(input("Enter the number : "))
    DisplayRev(Value)
    
    
    
    
if __name__=="__main__":
    main()