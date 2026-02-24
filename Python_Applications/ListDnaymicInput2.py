
def main():
    Size=0
    Value=0
    
    print("enter the no of elements :")
    Size=int(input())
    
    Data=list()
    print("enter the elements :")
    for i in range(Size):
        Value=int(input())
        Data.append(Value)   #it's like giving the money/memory when needed  not giving montly pocket money 
    print(Data) 
    Sum=0
    for i in range(Size):
        Sum=Sum+Data[i]
    
    print("Addition of elements :",Sum)
       
    
        
if __name__=="__main__":
    main()