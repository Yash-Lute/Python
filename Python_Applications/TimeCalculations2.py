import time

def Factorial(No):
    iFact=1
    for i in range(1,No+1):
        iFact=iFact*i
    
    return iFact    
    
def main():
    Value=int(input("Enter number : "))
    Ret=0
    start_time=time.time()
    Ret=Factorial(Value)
    print("Factorial is :",Ret)
    
    end_time=time.time()
    print("Total execution time is : ",end_time-start_time)
    

    
if __name__ == '__main__':
    main()
    