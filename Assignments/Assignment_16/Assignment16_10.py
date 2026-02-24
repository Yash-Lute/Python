def Lengthofstring(str):
    Count=0
    for i in str: 
        Count=Count+1
        
    return Count  
def main():
    str=input("Enter the name :")
    
    Ret=Lengthofstring(str)
    print(Ret)
    
    
    
    
if __name__=="__main__":
    main()