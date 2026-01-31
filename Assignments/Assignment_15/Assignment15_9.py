from functools import reduce

def main():
    length=int(input("Enter the length of list : "))
    data=list()
    for i in range(length):
        No=int(input("Enter the Number : "))
        data.append(No)
        
        
    
    Number=reduce(lambda x,y:x*y,data)
    print("Product of all elements : ",Number)
    
    
if __name__ == '__main__':
    main()
    
    