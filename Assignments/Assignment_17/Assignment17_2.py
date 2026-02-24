def DisplayPattern(Value1,Value2):
    
    for i in range(Value1):
        print("*",end=" ")
        for j in range(Value2-1):
            print("*",end=" ")
        print("\n")
            
            
        


def main():
    No1=int(input("Enter  Number of rows :"))
    No2=int(input("Enter  Number of columns :"))
    DisplayPattern(No1,No2)
    
    
    
    
if __name__ == '__main__':
    main()
    