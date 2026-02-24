def ChkPrime(Value):
    Count=0
    
        
    for i in range(1,Value+1):
        if Value%i==0:
            Count=Count+1
        
    return Count
    
    
    
def main():
    No=int(input("Enter  Number :"))
    Ret=0
    Ret=ChkPrime(No)
    if Ret==2:
        print("It is prime number")
    else:
        print("It is not a prime number ")
    
    
    
if __name__ == '__main__':
    main()
    