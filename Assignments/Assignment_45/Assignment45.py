import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#step 1 : load the data

df=pd.read_csv("WinePredictor.csv")
print("First 5 records : ")
print(df.head())

#step 2: clean the data

print("empty values : ")
print(df.isnull().sum())

#step 3:train the data

X=df.drop(columns="Class")
Y=df["Class"]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)


model=DecisionTreeClassifier()
model.fit(X_train,Y_train)


#step 4: test the data

Y_pred=model.predict(X_test)

print("Predicted records are :")
print(Y_pred)

print("Actual records are : ")
print(Y_test)

acc=accuracy_score(Y_test,Y_pred)
print("Accuracy is : ",acc)