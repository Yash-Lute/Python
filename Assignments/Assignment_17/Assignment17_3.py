def Factorial(Value):
    Ans=1
    for i in range(Value,0,-1):
        Ans=Ans*i
    return Ans
    
    
    
def main():
    No=int(input("Enter  Number of rows :"))
    Ret=0
    Ret=Factorial(No)
    print(Ret)
    
    
    
if __name__ == '__main__':
    main()
    