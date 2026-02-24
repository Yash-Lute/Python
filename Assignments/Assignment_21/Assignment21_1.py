import threading
lock=threading.Lock()
def ChkPrime(Numbers):
    with lock:
        print("Prime Numbers are : ")
        
            
        for i in Numbers:
            Count=0
            for j in range(1,i+1):
                if i%j==0:
                    Count=Count+1
            if Count==2:
                
                print(i)

def ChkNonPrime(Numbers):
    with lock:
        print("Non Prime Numbers are  : ")
        
        
        for i in Numbers:
            Count=0
            for j in range(1,i+1):
                if i%j==0:
                    Count=Count+1
            if Count!=2:
                
                print(i)
                
                
                
            
            
        
def main():
    data=[11,12,13,14,15,16,17,18,19,20]
    
    t1=threading.Thread(target=ChkPrime,args=(data,))
    t2=threading.Thread(target=ChkNonPrime,args=(data,))
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    
if __name__=="__main__":
    main()
    