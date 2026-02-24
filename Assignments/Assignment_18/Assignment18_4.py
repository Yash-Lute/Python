def Frequency(Numbers,find):
    frequency=0
    for i in Numbers:
        if i==find:
            frequency=frequency+1
    return frequency
            
            
        
    
                      
def main():
    Size=int(input("Enter  no of elements  : "))
    data=list()
    for i in range(Size):
        No=int(input("Enter  elements  : "))
        data.append(No)
    No2=int(input("Element to search : "))
            
    Ret=0
    Ret=Frequency(data,No2)
    print(Ret)
    
    
    
if __name__ == '__main__':
    main()
    