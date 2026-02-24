def AddFactors(Value):
    Ans=0
    
        
    for i in range(1,int((Value/2)+1)):
        if Value%i==0:
            Ans=Ans+i
        
    return Ans
    
    
    
def main():
    No=int(input("Enter  Number :"))
    Ret=0
    Ret=AddFactors(No)
    print(Ret)
    
    
    
if __name__ == '__main__':
    main()
    