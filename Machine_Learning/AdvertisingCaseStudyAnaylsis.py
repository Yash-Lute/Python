import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousAdvertise(Datapath):
    border="-"*40
    #-----------------------------------
    #Step 1 : load dataset
    #-----------------------------------
    print(border)
    print("Step 1 : load dataset")
    print(border)
    df=pd.read_csv(Datapath)
    
    print("few records from dataset :")
    print(df.head())
    #-----------------------------------
    #Step 2 : Remove unwanted columns
    #-----------------------------------
    
    print(border)
    print("Step 2 : unwanted columns")
    print(border)
    print("Shape of dataset before removal :",df.shape)
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)
    print("Shape of dataset after removal :",df.shape)
    
    print(border)
    print("Clean dataset is : ")
    print(border)
    
    
    print(df.head())
    #-----------------------------------
    #Step 3 : Check missing values 
    #-----------------------------------
    
    print(border)
    print("Step 3 : Check missing values")
    print(border)
    
    
    print("Missing values count : ",df.isnull().sum())
    
    #-----------------------------------
    #Step 4 : Display Statistical Summary
    #-----------------------------------
    
    print(border)
    print("Step 4 : Display Statistical Summary")
    print(border)
    
    
    print(df.describe())
    
     #-----------------------------------
    #Step 5 : Corealation between columns
    #-----------------------------------
    
    print(border)
    print("Step 5 : Corealation between  columns")
    print(border)
    print("Correlation matrix")
    print(df.corr())
    

     
        
    
    
    
    
def main():
    MarvellousAdvertise("Advertising.csv")
    
    
    
    

    
    
    
if __name__ =="__main__":
    main()
