def ChkPalindrome(No):
    iDigit=0
    temp=No
    rev=0
    while No!=0:
        iDigit=No%10
        rev=rev*10+iDigit
        No=int(No/10)
    if rev==temp:
        return True
        
        
    

def main():
    Value=int(input("Enter the number : "))
    Ret=False
    Ret=ChkPalindrome(Value)
    if Ret==True:
        print("It is palindrome")
    else:
        print(" not a palindrome")
        
    
    
    
    
if __name__=="__main__":
    main()