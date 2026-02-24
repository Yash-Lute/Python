def ChkPrime(Numbers):
    Count=0
    ListPrime=list()
    for i in Numbers:
        Count=0
        for j in range(1,i+1,1):
            if i%j==0:
                Count=Count+1
        if Count==2:
            ListPrime.append(i)
    
    return ListPrime
            
            
    
    
        
                
                
            
            
        