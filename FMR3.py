from functools import reduce


def CheckEven(No):
    return (No%2==0)

def Increment(No):
    return No+1
def Add(A,B):
    return A+B
def main():
    Data=[11,10,15,20,22,27,30]
    print("Actual data is :",Data)
    FData=list(filter(CheckEven,Data))   
    
    print("Data after filter is : ",FData)
    
    Mdata=list(map(Increment,FData))
    print("Data after Map is : ",Mdata)
    
    Rdata=reduce(Add,Mdata)
    print("Data after Reduce is : ",Rdata)
    
    

if __name__=="__main__":
    main()    