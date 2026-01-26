
def filterX(task,elements):
    Result=list()     
    
    for no in elements:
        Ret=task(no)
        if Ret==True:
            Result.append(no)
    
    return Result

def mapx(Task,Elements):
    Result=list()
    
    for no in Elements:
        Ret=Task(no)
        Result.append(Ret)
    
    return Result

def reduceX(task,Element):
    Sum=0
    
    for no in Element:
        Sum=task(Sum,no)
    
    return Sum