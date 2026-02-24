from functools import reduce
def main():
    
    Size=int(input("Enter the  no of elements :"))
    data=list()
    
    for i in range(Size):
        No=int(input("enter the elements "))
        data.append(No)
        
    data=list(filter(lambda x:x%2==0 ,data))
    print(data)
    data=list(map(lambda x:x*x,data))
    print(data)
    Ret=reduce(lambda x,y:x+y,data)
    print(Ret)
    
        
    
     
if __name__ == '__main__':
    main()
    