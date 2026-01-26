def ConnvertBinary(No):
    Binary=list()
    while(No>=1):
        Bin=int(No%2)
        Binary.append(Bin)
        No=No/2
    for i in range(len(Binary)-1,-1,-1):
        print(Binary[i])
        
        
            
    
    
              
def main():
    Value1=int(input("Enter Number : "))
    Ret=False
    ConnvertBinary(Value1)
        
   
    
if __name__=="__main__":
    main()