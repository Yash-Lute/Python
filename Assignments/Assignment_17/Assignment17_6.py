def DisplayPattern(Value):
    for i in range(Value):
        for j in range(Value-i):
            print("*",end=" ")
        print("\n")
            
        
    
    
    
def main():
    No=int(input("Enter  Number :"))
    
    DisplayPattern(No)
    
    
    
if __name__ == '__main__':
    main()
    