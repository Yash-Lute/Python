from functools import reduce

def main():
    length=int(input("Enter the length of list : "))
    data=list()
    for i in range(length):
        No=int(input("Enter the number : "))
        data.append(No)
        
        
    
    Numbers=reduce(lambda x,y:max(x,y),data)
    print("Maximum is : ",Numbers)
    
    
if __name__ == '__main__':
    main()
    
    