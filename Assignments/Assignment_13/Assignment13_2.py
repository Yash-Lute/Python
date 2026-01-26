def Area(Radius):
    Area=0
    Area=Radius*Radius
    return Area
    
    
              
def main():
    Value1=int(input("Enter radius : "))
    Ret=0
    Ret=Area(Value1)
    print("Area of circle is : ",Ret)
   
    
if __name__=="__main__":
    main()