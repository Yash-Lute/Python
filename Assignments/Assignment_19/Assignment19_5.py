from functools import reduce
def ChkPrime(No):
    Count=0
    for i in range(1,No+1):
        if No%i==0:
            Count=Count+1
    
    if Count==2:
        return No

def Maximum(x,y):
    if x>y:
        return x
    else:
        return y
             
    
def main():
    
    Size=int(input("Enter the  no of elements :"))
    data=list()
    
    for i in range(Size):
        No=int(input("enter the elements "))
        data.append(No)
        
    data=list(filter(ChkPrime ,data))
    print(data)
    data=list(map(lambda x:x*2,data))
    print(data)
    Ret=reduce(Maximum,data)
    print(Ret)
    
        
    
     
if __name__ == '__main__':
    main()
    