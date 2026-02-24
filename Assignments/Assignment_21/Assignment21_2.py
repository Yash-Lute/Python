import threading

def Max(Numbers):
    
    Max=Numbers[1]
    for i in Numbers:
        if i>Max:
            Max=i
    print("Maximum number is : ",Max)
               
            
       

def Min(Numbers):
   
    Min=Numbers[1]
    for i in Numbers:
        if i<Min:
            Min=i
    print("Minimum number is : ",Min)
       
                
                
                
            
            
        
def main():
    Size=int(input("Enter no of elements :"))
    data=[]
    for i in range(Size):
        No=int(input("enter the number : "))
        data.append(No)
        
        
    
    t1=threading.Thread(target=Max,args=(data,))
    t2=threading.Thread(target=Min,args=(data,))
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    
if __name__=="__main__":
    main()
    