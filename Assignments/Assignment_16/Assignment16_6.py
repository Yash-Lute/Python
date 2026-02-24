def ChkNum(No):
    if No>0:
        print("Positive number")
    elif No==0:
        print("Zero")
    else:
        print("Negative number")    
    
    
        
    
def main():
    Value=int(input("Enter number :"))
    ChkNum(Value)
    
    
    
    
if __name__=="__main__":
    main()