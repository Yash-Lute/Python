import threading

def DisplayEven():
    for i in range(1,11):
        if i%2==0:
            print(i)
            
def DisplayOdd():
    for i in range(1,11):
        if i%2!=0:
            print(i)


            
        
def main():
    
    t1=threading.Thread(target=DisplayEven)
    t2=threading.Thread(target=DisplayOdd)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
     
if __name__ == '__main__':
    main()
    