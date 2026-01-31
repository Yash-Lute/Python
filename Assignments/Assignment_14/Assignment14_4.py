Min=lambda x,y:x<y
    

def main():
    No1=int(input("Enter the 1st number :"))
    No2=int(input("Enter the 2nd number :"))
    Ret=Min(No1,No2)
    if Ret==True:
        print(No1,"is smaller")
    else:
        print(No2,"is smaller")
        
    
if __name__ == '__main__':
    main()
    