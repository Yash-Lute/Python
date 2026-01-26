import threading

def SumEven(No):
    sum=0
    for i in range(2,No+1,2):
        sum=sum+i
    
    print("Even Sum is : ",sum)
        
        
def main():
    SumEven(10)
   
    
if __name__ == '__main__':
    main()
    