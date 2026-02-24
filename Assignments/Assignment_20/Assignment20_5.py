import threading
lock=threading.Lock()
def Display():
    with lock:
        for i in range(1,51) :
            
                print(i)
            
        

def revDisplay():
    with lock:
        for i in range(50,0,-1):
            print(i)
        
        
    


            
        
def main():
    
    
    
    
    t1=threading.Thread(target=Display)
    t2=threading.Thread(target=revDisplay)
    
    t1.start()
    t2.start()
   
    t1.join()
    t2.join()
    
    print("Exit of main")
     
if __name__ == '__main__':
    main()
    