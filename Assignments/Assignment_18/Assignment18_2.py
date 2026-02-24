def Max(Numbers):
    Max=Numbers[1]
    for i in Numbers:
        if Max<i:
            Max=i
    return Max
                      
def main():
    Size=int(input("Enter  no of elements  : "))
    data=list()
    for i in range(Size):
        No=int(input("Enter  elements  : "))
        data.append(No)
            
    Ret=0
    Ret=Max(data)
    print(Ret)
    
    
    
if __name__ == '__main__':
    main()
    