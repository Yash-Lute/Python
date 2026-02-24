import threading

def Small(str):
    SCount=0
    
    print("Thread ID :",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)
    for i in str:
        if i>='a' and i<='z':
            SCount=SCount+1
    print("Small letters : ",SCount) 
              
            
def Captial(str):
    CCount=0
    print("Thread ID :",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)
    for i in str:
        if i>='A' and i<='Z':
            CCount=CCount+1
    print("Captial letters : ",CCount)   
        
   
    
def Digits(str):
    DCount=0
    print("Thread ID :",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)
    for i in str:
        if i>='0'and i<='9':
            DCount=DCount+1
    print("Digits : ",DCount)
        
    


            
        
def main():
    
    str=input("Enter the string : ")
    
    t1=threading.Thread(target=Small,args=(str,))
    t2=threading.Thread(target=Captial,args=(str,))
    t3=threading.Thread(target=Digits,args=(str,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("Exit of main")
     
if __name__ == '__main__':
    main()
    