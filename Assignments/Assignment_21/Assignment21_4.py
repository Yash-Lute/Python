import threading
lock=threading.Lock()
def Sum(Numbers):
    
    Sum=0
    for i in Numbers:
        Sum=Sum+i
    return Sum
        
               
            
       

def Multiply(Numbers):
   
    Ans=1
    for i in Numbers:
        Ans=Ans*i
    return Ans
       
                
                
                
            
            
        
def main():
    Size=int(input("Enter no of elements :"))
    data=[]
    for i in range(Size):
        No=int(input("enter the number : "))
        data.append(No)
        
        
    
    t1=threading.Thread(target=Sum,args=(data,))
    t2=threading.Thread(target=Multiply,args=(data,))
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    
    
if __name__=="__main__":
    main()
    