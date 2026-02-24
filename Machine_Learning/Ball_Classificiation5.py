

from sklearn import tree

#Rough =1
#smooth =0


#tennis =1
#cricket =2


def main():
    print("Ball classification case study ")
    #Independent variables
    X=[[35,1],[47,1],[90,0],[48,0],[90,1],[35,0],[92,1],[35,0],[35,0],[35,0],[96,1],[43,0],[110,1],[35,0],[95,1]]
    #Dependent varibales
    Y=[1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
    
    #Independent Variables for training
    Xtrain=[[35,1],[47,1],[90,0],[48,0],[90,1],[35,0],[92,1],[35,0],[35,0],[35,0],[96,1],[43,0],[110,1]]
    
    #Independent Variables for testing
    Xtest= [[35,0],[95,1]]
    
    #dependent varibles  for training
    Ytrain=[1,1,2,1,2,1,2,1,1,1,2,1,2]
    
    #dependent variables for testing
    Ytest=[1,2]
    
    modelobj=tree.DecisionTreeClassifier()

    trainedmodel=modelobj.fit(Xtrain,Ytrain)
   
    Result=trainedmodel.predict(Xtest) 
    
    print("Model predicts the object as : ",Result)
    
    
if __name__=="__main__":
    main()
    

#Dataset size : 15

