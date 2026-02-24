import threading
from functools import reduce

def EvenList(Numbers):
    Sum=0
    data=list(filter(lambda x:x%2==0,Numbers))
    Sum=reduce(lambda x,y:x+y,data)
    print(Sum)        
            
def OddList(Numbers):
    Sum=0
    data=list(filter(lambda x:x%2!=0,Numbers))
    Sum=reduce(lambda x,y:x+y,data)
    print(Sum)


            
        
def main():
    
    data=[10,11,12,1,31,78,34,89,90]
    
    t1=threading.Thread(target=EvenList,args=(data,))
    t2=threading.Thread(target=OddList,args=(data,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Exit of main")
     
if __name__ == '__main__':
    main()
    