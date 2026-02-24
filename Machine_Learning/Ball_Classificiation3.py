

from sklearn import tree

#Rough =1
#smooth =0


#tennis =1
#cricket =2


def main():
    print("Ball classification case study ")
    #Independent variables
    Features=[[35,1],[47,1],[90,0],[48,0],[90,1],[35,0],[92,1],[35,0],[35,0],[35,0],[96,1],[43,0],[110,1],[35,0],[95,1]]
    #Dependent varibales
    labels=[1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
    
    modelobj=tree.DecisionTreeClassifier()

    trainedmodel=modelobj.fit(Features,labels)
   
    Result=trainedmodel.predict([[37,1],[94,0]]) #1,2
    
    print("Model predicts the object as : ",Result)
    
    
if __name__=="__main__":
    main()
    

#Dataset size : 15

