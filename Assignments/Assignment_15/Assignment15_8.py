from functools import reduce

def main():
    length=int(input("Enter the length of list : "))
    data=list()
    for i in range(length):
        No=int(input("Enter the Number : "))
        data.append(No)
        
        
    
    Numbers=list(filter(lambda x:(x%5==0)and(x%3==0),data))
    print("Numbers divisible by 3 and 5 are : ",Numbers)
    
    
if __name__ == '__main__':
    main()
    
    