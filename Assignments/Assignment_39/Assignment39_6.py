from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,ConfusionMatrixDisplay,confusion_matrix,classification_report
import matplotlib.pyplot as plt
import pandas as pd


datapath="student_performance_ml.csv"

dataframe=pd.read_csv(datapath)



print("No of blank values")
print(dataframe.isnull().sum())

features=["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]
X=dataframe[features]
Y=dataframe[["FinalResult"]]




X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
print("train test split done")

model=DecisionTreeClassifier(random_state=42)

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



con=confusion_matrix(Y_test,Predicted)
print("Confusion matrix ")
print(con)

print("True positive : ",con[0,0])
print("True Negative : ",con[1,1])
print("False  positive : ",con[1,0])
print("False negative : ",con[0,1])



data=ConfusionMatrixDisplay(confusion_matrix=con,display_labels=model.classes_)

data.plot()
plt.title("Confusion matrix of Student Performance")
plt.show()


training_accuracy=model.score(X_train,Y_train)

print("training accuracy is : ",training_accuracy*100)


















