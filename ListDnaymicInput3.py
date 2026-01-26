def Summation(Arr):      #Arr is just topan naav for data  
    Sum=0
    for i in range(len(Arr)):
        Sum=Sum+Arr[i]
    
    return Sum
    
def main():
    Size=0
    Value=0
    Ret=0
    
    print("enter the no of elements :")
    Size=int(input())
    
    Data=list()
    print("enter the elements :")
    for i in range(Size):
        Value=int(input())
        Data.append(Value)   #it's like giving the money/memory when needed  not giving montly pocket money 
    print(Data) 
    
    Ret=Summation(Data)
    print("Addition of elements is :",Ret) 
    
        
if __name__=="__main__":
    main()