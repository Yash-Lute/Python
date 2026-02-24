def AddDigits(Value):
    digits=0
    Sum=0
    while Value!=0:
        digits=Value%10
        Sum=Sum+digits
        Value=int(Value/10)
    return Sum
    
             
def main():
    No=int(input("Enter  Number :"))
    Ret=0
    Ret=AddDigits(No)
    print(Ret)
    
    
    
if __name__ == '__main__':
    main()
    