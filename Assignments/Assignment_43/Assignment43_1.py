import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#step 1: load the dataset
df=pd.read_csv("PlayPredictor.csv")
print("first 5 records : ")
print(df.head())

#step 2: Clean & Manipulate the data
df=df.drop(df.columns[0],axis=1)

lobj=LabelEncoder()
df["Weather_encoded"]=lobj.fit_transform(df["Whether"])
df["Temperature_encoded"]=lobj.fit_transform(df["Temperature"])

print(df.head())

#Step 3: train the data

X=df.drop(columns=["Play","Whether","Temperature"])
Y=df["Play"]
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

model=KNeighborsClassifier(n_neighbors=3)

model.fit(X,Y)


#step 4 : test the data

Y_pred=model.predict(X_test)

print("predicted values are : ")
print(Y_pred)


#step 5: Calculate the accuracy 

def CheckAccuracy(Y_pred,Y_test):
    numerator=0
    Y_test=Y_test.reset_index(drop=True)
    for i in range(len(Y_pred)):
        if Y_pred[i]==Y_test[i]:
            numerator=numerator+1
    
    acc=(numerator/len(Y_pred))*100
    return acc

acc=CheckAccuracy(Y_pred,Y_test)
print("Accuracy is : ",acc)

                
                



