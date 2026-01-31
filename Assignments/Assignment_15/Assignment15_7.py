from functools import reduce

def main():
    length=int(input("Enter the length of list : "))
    data=list()
    for i in range(length):
        str=input("Enter the string : ")
        data.append(str)
        
        
    
    Strings=list(filter(lambda x:len(x)>5,data))
    print("String are : ",Strings)
    
    
if __name__ == '__main__':
    main()
    
    