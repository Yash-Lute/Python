

def main():
    length=int(input("Enter the length of list : "))
    data=list()
    for i in range(length):
        No=int(input("Enter the Number : "))
        data.append(No)
        
        
    
    Numbers=list(filter(lambda x:x%2==0,data))
    
    print("Total even numbers are : ",len(Numbers))
    
    
if __name__ == '__main__':
    main()
    
    