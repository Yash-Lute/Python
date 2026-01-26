from functools import reduce

CheckEven=lambda No:(No%2==0)
Increment=lambda No:No+1
Add=lambda A,B:A+B
def filterX(task,elements):
    Result=list()     
    
    for no in elements:
        Ret=task(no)
        if Ret==True:
            Result.append(no)
    
    return Result

def mapx(Task,Elements):
    Result=list()
    
    for no in Elements:
        Ret=Task(no)
        Result.append(Ret)
    
    return Result

def reduce(task,Element):
    Sum=0
    
    for no in Element:
        Sum=task(Sum,no)
    
    return Sum
                 
    
def main():
    Data=[11,10,15,20,22,27,30]
    print("Actual data is :",Data)
    FData=list(filterX(CheckEven,Data))   
    
    print("Data after filter is : ",FData)
    
    Mdata=list(map(Increment,FData))
    print("Data after Map is : ",Mdata)
    
    Rdata=reduce(Add,Mdata)
    print("Data after Reduce is : ",Rdata)
    
    

if __name__=="__main__":
    main()    