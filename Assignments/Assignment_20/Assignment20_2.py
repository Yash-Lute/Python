import threading

def EvenFactors(No):
    Sum=0
    for i in range(1,No+1):
        if No%i==0:
            if i%2==0:
                Sum=Sum+i;
    print("Addition of even factors is :",Sum)
                
                
            
        
        
            
def OddFactors(No):
    Sum=0
    for i in range(1,No+1):
        if No%i==0:
            if i%2!=0:
                Sum=Sum+i;
    print("Addition of odd factors is :",Sum)


            
        
def main():
    
    t1=threading.Thread(target=EvenFactors,args=(12,))
    t2=threading.Thread(target=OddFactors,args=(12,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Exit of main")
     
if __name__ == '__main__':
    main()
    