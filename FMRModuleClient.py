from MarvellousFMR import filterX,mapx,reduceX

CheckEven=lambda No:(No%2==0)
Increment=lambda No:No+1
Add=lambda A,B:A+B
                 
    
def main():
    Data=[11,10,15,20,22,27,30]
    print("Actual data is :",Data)
    FData=list(filterX(CheckEven,Data))   
    
    print("Data after filter is : ",FData)
    
    Mdata=list(map(Increment,FData))
    print("Data after Map is : ",Mdata)
    
    Rdata=reduceX(Add,Mdata)
    print("Data after Reduce is : ",Rdata)
    
    

if __name__=="__main__":
    main()    