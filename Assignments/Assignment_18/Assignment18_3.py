def Min(Numbers):
    Min=Numbers[1]
    for i in Numbers:
        if Min>i:
            Min=i
    return Min
                      
def main():
    Size=int(input("Enter  no of elements  : "))
    data=list()
    for i in range(Size):
        No=int(input("Enter  elements  : "))
        data.append(No)
            
    Ret=0
    Ret=Min(data)
    print(Ret)
    
    
    
if __name__ == '__main__':
    main()
    