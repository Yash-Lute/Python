from functools import reduce

def main():
    Data=[11,10,15,20,22,27,30]
    print("Actual data is :",Data)
    FData=list(filter((lambda No:(No%2==0)),Data))   
    
    print("Data after filter is : ",FData)
    
    Mdata=list(map((lambda No:No+1),FData))
    print("Data after Map is : ",Mdata)
    
    Rdata=reduce((lambda A,B:A+B),Mdata)
    print("Data after Reduce is : ",Rdata)
    
    

if __name__=="__main__":
    main()    