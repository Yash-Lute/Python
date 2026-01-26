def Factorial(No):
    Ans=1
    for i in range(1,No+1):
        Ans=Ans*i
    
    return Ans
        
    

def main():
    Value=int(input("Enter the number : "))
    Ret=0
    Ret=Factorial(Value)
    print(Ret)
    
if __name__=="__main__":
    main()