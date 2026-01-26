class Parent:
    def __init__(self):
        print("Inside parent constructor")
      
        
    def fun(self):
        print("Inside fun method of parent")
    

class child (Parent):
    def __init__(self):
        super().__init__()
        print("Inside child constructor")
        
        
    def fun(self):
        super().fun()
        print("Inside fun method of child ")
        
cobj=child()



cobj.fun()