def ChkPrime(No):
    iCount=0
    for i in range(1,No+1):
        if No%i==0:
            iCount=iCount+1
             
           
    
    
    if iCount==2:
        return True
        
    

def main():
    Value=int(input("Enter the number : "))
    Ret=False
    Ret=ChkPrime(Value)
    
    if Ret==True:
        print("Prime Number")
    else:
        print("Not a Prime Number")
    
    
if __name__=="__main__":
    main()