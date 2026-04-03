from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd


datapath="student_performance_ml.csv"

dataframe=pd.read_csv(datapath)

print(dataframe.head())

print("No of blank values")
print(dataframe.isnull().sum())

features=["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]
X=dataframe[features]
Y=dataframe[["FinalResult"]]




X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.8,random_state=42)
print("train test split done")

model=DecisionTreeClassifier(max_depth=3,random_state=42)

model.fit(X_train,Y_train)
print("training done")

Predicted=model.predict(X_test)
print("Testing done")

print("Predicted values :")
print(Predicted)

print("actual values :")
print(Y_test)


accuracy=accuracy_score(Y_test,Predicted)

print("Accuracy of model is : ",accuracy*100)












