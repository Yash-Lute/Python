def DisplayPattern(Value):
    for i in range(Value):
        for j in range(1,Value+1):
            print(j,end=" ")
        print("\n")
            
        
    
    
    
def main():
    No=int(input("Enter  Number :"))
    
    DisplayPattern(No)
    
    
    
if __name__ == '__main__':
    main()
    