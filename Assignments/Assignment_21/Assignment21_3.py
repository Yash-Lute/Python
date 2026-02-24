import threading

i=10
lock=threading.Lock()
def Update():
    global i
    with lock:
        for j in range(3):
            i=i+1
        print(i)
        
    
    
               
            
       

def Update2():
    global i
    with lock:
        for j in range(3):
            i=i+1
        print(i)
   
    
       
                
                
                
            
            
        
def main():
    
        
        
    
    t1=threading.Thread(target=Update)
    t2=threading.Thread(target=Update2)
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    
if __name__=="__main__":
    main()
    