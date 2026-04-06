import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

#Step 1: Load the dataset
df=pd.read_csv("Advertising.csv")
print("First 5 records : ")
print(df.head())

#Step 2 : Clean the dataset

if "Unnamed: 0" in df.columns:
    df.drop(columns=["Unnamed: 0"],inplace=True)
    
print(df.head())


#step 3: train the data

X=df.drop(columns="sales")
Y=df["sales"]

print("independent varibles : ",X)
print("dependent varibles : ",Y)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.5,random_state=42)

model=LinearRegression()

model.fit(X_train,Y_train)

#step 4: test the data

Y_pred=model.predict(X_test)

#step 5: predicted vs actual data 

print("Predicted values are : ",Y_pred)

print("Actual values are : ",Y_test)



