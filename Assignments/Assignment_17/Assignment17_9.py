def CountDigits(Value):
    Count=0
    while Value!=0:
        Count=Count+1
        Value=int(Value/10)
    return Count
    
             
def main():
    No=int(input("Enter  Number :"))
    Ret=0
    Ret=CountDigits(No)
    print(Ret)
    
    
    
if __name__ == '__main__':
    main()
    