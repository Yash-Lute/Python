def DisplayPattern(Value):
    for i in range(Value+1):
        for j in range(1,Value+1):
            if i>=j:
                print(j,end=" ")
        print("\n")
            
        
    
    
    
def main():
    No=int(input("Enter  Number :"))
    
    DisplayPattern(No)
    
    
    
if __name__ == '__main__':
    main()
    