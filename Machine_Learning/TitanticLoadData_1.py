import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
#----------------------------------------
#
#  Function Name : DisplayInfo
#  Description :   It displays the formatted title
#  Parameters  :   title(str)
#  Return      :  None
#  Date        :  14/03/2026
#  Author      :  Yash Lute
#---------------------------------------------

def DisplayInfo(title):
    print("\n"+"="*70)
    print(title)
    print("="*70)

#----------------------------------------
#
#  Function Name : ShowData
#  Description :   It shows basic information of dataset 
#  Parameters  :   df
#                  df ->      Pandas dataframe object
#                  message
#                  message->  Heading text to display
#  Return      :  None
#  Date        :  14/03/2026
#  Author      :  Yash Lute
#---------------------------------------------

def ShowData(df,message):
    DisplayInfo(message)
    
    print("\nFirst five rows of dataset : ")
    print(df.head())
    
    print("\n Shape of dataset : ")
    print(df.shape)
    
    print("\n Column names : ")
    print(df.columns.tolist())
    
    print("\n Missing values in each column")
    print(df.isnull().sum())
    
    

#----------------------------------------
#
#  Function Name : MarvellousTitanicLogistic
#  Description :   This is main pipeline controller
#                  It loads the dataset shows raw data
#                  It preprocess the dataset  and train the model
#  Parameters  :   Data path of dataset file
#  Return      :  None
#  Date        :  14/03/2026
#  Author      :  Yash Lute
#---------------------------------------------
def MarvellousTitanicLogistic(Datapath):
    
    DisplayInfo("Step1 : Loading the dataset")
    df=pd.read_csv(Datapath)
    ShowData(df,"Initial dataset ")
    
    

#----------------------------------------
#
#  Function Name : main
#  Description :   Starting point of the application
#  Parameters  :  None
#  Return      :  None
#  Date        :  14/03/2026
#  Author      :  Yash Lute
#---------------------------------------------
def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")
    
    
    
    
if __name__ =="__main__":
    main()