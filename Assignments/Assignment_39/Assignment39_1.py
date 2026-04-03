from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
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









