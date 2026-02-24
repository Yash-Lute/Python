
def main():
    Size=0
    Value=0
    
    print("enter the no of elements :")
    Size=int(input())
    
    Data=list()
    print("enter the elements :")
    for i in range(Size):
        Value=int(input())
        Data.append(Value)
    
    print(Data)    
    
        
if __name__=="__main__":
    main()