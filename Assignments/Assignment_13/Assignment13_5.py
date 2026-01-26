def DisplayGrade(No):
    if No>=75:
        print("Distinction")
    elif No>=60:
        print("First class")
    elif No>=50:
        print("Second class")
    else:
        print("Fail")
                 
def main():
    Value1=int(input("Enter Number : "))
    DisplayGrade(Value1)
   
        
   
    
if __name__=="__main__":
    main()