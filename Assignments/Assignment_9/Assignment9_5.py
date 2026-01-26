def Divisible(No):
    if No%3==0 and No%5==0:
        return True
    else:
        return False
    
        
     
def main():
    Value=int(input("Enter 1st number"))
    Ret=False
    
    Ret=Divisible(Value)
    if Ret==True:
        print("Divisible by 3 & 5")
    else:
        print("Is not divisible ")
    
    
if __name__=="__main__":
    main()