def PerfectNumber(No):
    Cnt=int(No/2)
    iFact=0
    for i in range(1,Cnt+1):
        if No%i==0:
            iFact=iFact+i
    
    if iFact==No:
        return True
        
            
    
    
              
def main():
    Value1=int(input("Enter Number : "))
    Ret=False
    Ret=PerfectNumber(Value1)
    if Ret==True:
        print("Perfect Number")
    else:
        print("Not a perferct Number")
        
   
    
if __name__=="__main__":
    main()