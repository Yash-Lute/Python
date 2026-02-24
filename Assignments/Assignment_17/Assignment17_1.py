import Arithematic


def main():
    No1=int(input("Enter 1st Number :"))
    No2=int(input("Enter 1st Number :"))
    Ret=0
    Ret=Arithematic.Add(No1,No2)
    print("Addition is : ",Ret)
    
    Ret=Arithematic.Sub(No1,No2)
    print("Subtraction is : ",Ret)
    
    Ret=Arithematic.Mult(No1,No2)
    print("Multiplication is : ",Ret)
    
    Ret=Arithematic.Div(No1,No2)
    print("Division is : ",Ret)
if __name__ == '__main__':
    main()
    