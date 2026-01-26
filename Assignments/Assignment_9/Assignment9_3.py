def Square(No):
    Ans=0
    Ans=No*No
    return Ans
    
    
    
        
def main():
    Value=int(input("Enter 1st number"))
    Ret=0
    
    Ret=Square(Value)
    print(Ret)
    
if __name__=="__main__":
    main()