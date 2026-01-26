import os

def Factorial(No):
    iFact=1
    for i in range(1,No+1):
        iFact=iFact*i
    
    return iFact    
    
def main():
    Value=int(input("Enter number : "))
    Ret=0
    Ret=Factorial(Value)
    print("Factorial is :",Ret)
    


    
if __name__ == '__main__':
    main()
    