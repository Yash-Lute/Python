from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,ConfusionMatrixDisplay,confusion_matrix,classification_report

import matplotlib.pyplot as plt
import pandas as pd

#Step 1: Dataset loading
datapath="student_performance_ml.csv"

dataframe=pd.read_csv(datapath)


# Step 2 : data analysis
print("No of blank values")
print(dataframe.isnull().sum())



features=["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]
X=dataframe[features]
Y=dataframe[["FinalResult"]]


#Step 4: Train test split

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
print("train test split done")
print(X_train)


model=DecisionTreeClassifier(random_state=42)

# Step 5: Model training
model.fit(X_train,Y_train)
print("training done")


#Step 6: Prediction
sample=[[6,85,66,7,7]]
Predicted=model.predict(X_test)
Predicted_sample=model.predict(sample)
         
print("Testing done")

print("Predicted values :")
print(Predicted)

print("actual values :")
print(Y_test)


# Step 7: Accuracy calculation
accuracy=accuracy_score(Y_test,Predicted)

print("Accuracy of model is : ",accuracy*100)


# Step 8: Confusion matrix generation
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

#  Step 9 : Conclusion
print("training accuracy is : ",training_accuracy*100)


if Predicted_sample==1:
    print("Output of given sample the predicted output is : Pass")
else:
    print("Output of given sample the predicted output is : fail")
    
    
print(model.feature_importances_) 
    

    
    




















