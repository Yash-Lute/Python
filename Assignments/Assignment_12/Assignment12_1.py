def ChkPalindrome(No):
    if No=='a' or No=='e' or No=='i' or No=='o' or No=='u' or No=='A' or No=='E' or No=='I' or No=='O' or No=='U':
        return True
        
    
        
        
    

def main():
    Value=(input("Enter the character : "))
    Ret=False
    Ret=ChkPalindrome(Value)
    if Ret==True:
        print("It is a Vowel")
    else:
        print(" It's not a Vowel")
        
    
    
    
    
if __name__=="__main__":
    main()