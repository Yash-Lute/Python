import MarvellousNum

def Add(Numbers):
    Sum=0
    for i in Numbers:
        Sum=Sum+i;
    return Sum
                      
def main():
    Size=int(input("Enter  no of elements  : "))
    data=list()
    for i in range(Size):
        No=int(input("Enter  elements  : "))
        data.append(No)
    
    data=MarvellousNum.ChkPrime(data)
    print(data)
    Ret=0
    Ret=Add(data)
    print(Ret)
       
    
if __name__ == '__main__':
    main()
    