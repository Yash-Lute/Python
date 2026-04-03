
def MeanofX(X):
    iSum=0
    for i in X:
        iSum=iSum+i
    iAvg=iSum/(X.__len__())
    return iAvg

def MeanofY(Y):
    iSum=0
    for i in Y:
        iSum=iSum+i
    iAvg=iSum/(Y.__len__())
    return iAvg

def slope(mean_x,mean_y,X,Y):
    size=len(X)
    numerator=0
    denominator=0
    for i in range(size):
    
        numerator=numerator+((X[i]-mean_x)*(Y[i]-mean_y))
        denominator=denominator+((X[i]-mean_x)**2)
    m=numerator/denominator
    return m

def Y_intercept(m,mean_x,mean_y):
    C=mean_y-(m*mean_x)
    return C

def Equation(m,C,X):
    Ypred=[]
    for i in range(len(X)):
        Y=(m*X[i])+C
        Ypred.append(Y)
        print("Predicted Y for X=",X[i],":",Y)
    return Ypred
    
def MeanSquareError(Y,Ypred):
    n=len(Y)
    result=0
    for y in Y:
        for y_pred in Ypred:
            result=result+((y-y_pred)**2)
    MSE=(1/n)*(result)
    return MSE 

def rsqaure(y_mean,Y,Y_predicted):
    numerator=0
    denoimator=0
    for Yp in Y_predicted:
        numerator=numerator+((Yp-y_mean)**2)
    for yactual in Y:
            denoimator=denoimator+((yactual-y_mean)**2 )
    
    r_square=numerator/denoimator
    return r_square
            
    
        
    
    
    
    

# load dataset
X=[1,2,3,4,5]
Y=[3,4,2,4,5]

iRet1=MeanofX(X)
print("Avgerage of X : ",iRet1)
iRet2=MeanofY(Y)
print("Avgerage of Y : ",iRet2)

m=slope(iRet1,iRet2,X,Y)

print("Slope (m): ",m)

C=Y_intercept(m,iRet1,iRet2)

print("Intercept (c): ",C)


Ypred=Equation(m,C,X)

MSE=MeanSquareError(Y,Ypred)

print("MSE : ",MSE)

r_square=rsqaure(iRet2,Y,Ypred)

print("R square : ",r_square)



