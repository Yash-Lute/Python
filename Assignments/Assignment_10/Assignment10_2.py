def Summation(No):
    sum=0
    for i in range(1,No+1):
        sum=sum+i
    
    return sum
        
    

def main():
    Value=int(input("Enter the number : "))
    Ret=0
    Ret=Summation(Value)
    print(Ret)
    
if __name__=="__main__":
    main()