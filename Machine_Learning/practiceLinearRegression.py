import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error

def headbrain(filename):
    
    
    df=pd.read_csv(filename)
    
    print("Missing values count : ",df.isnull().sum())
    
    X=df[["Gender","Age Range","Head Size(cm^3)"]]
    Y=df["Brain Weight(grams)"]
    
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,train_size=0.8,random_state=42)
    print("train test split done")
    
    model=LinearRegression()
    
    model.fit(X_train,Y_train)
    print("Training done")
    
    Y_pred=model.predict(X_test)
    print("Testing done ")
    
    Result=pd.DataFrame({"Actual weight" :Y_test,"Predicted weight ":Y_pred})
    
    print(Result)
    
    MSE=mean_squared_error(Y_test,Y_pred)
    RMSE=np.sqrt(MSE)
    r2=r2_score(Y_test,Y_pred)
    
    
    print("Mean square error : ",MSE)
    print("Root Mean square error : ",RMSE)
    print("r square value : ",r2)
    
    
  
  
def main():
    filename="MarvellousHeadBrain.csv"
    headbrain(filename)
    
    
    
if __name__ =="__main__":
    main()
    