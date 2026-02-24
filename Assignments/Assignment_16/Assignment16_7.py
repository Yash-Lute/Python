def Chkdivisible(No):
    if No%5==0:
        return True
        
    else:
        return False
        
    
    
        
    
def main():
    Value=int(input("Enter number :"))
    Ret=Chkdivisible(Value)
    if Ret==True:
        print(Ret)
        
    else:
        print(Ret)
        
    
    
    
if __name__=="__main__":
    main()