

def main():
    length=int(input("Enter the length of list : "))
    data=list()
    for i in range(length):
        No=int(input("Enter the number : "))
        data.append(No)
        
        
    
    Numbers=list(filter(lambda x:x%2==0,data))
    print("List of even numbers are : ",Numbers)
    
    
if __name__ == '__main__':
    main()
    
    