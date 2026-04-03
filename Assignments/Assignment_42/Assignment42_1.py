
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

def Equation(m,C,testdata):
    Y=(m*testdata)+C
    return Y
    
    
        
    
    

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

testdata=6
Predicted=Equation(m,C,testdata)
print("Predicted Y for X=",testdata,":",Predicted)


