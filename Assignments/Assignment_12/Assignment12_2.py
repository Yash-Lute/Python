def Factor(No):
    for i in range(1,No+1):
        if No%i==0:
            print(i)
            
def main():
    Value=int(input("Enter the number : "))
    
    Factor(Value)
     
if __name__=="__main__":
    main()