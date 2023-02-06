# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

df = pd.read_csv('Allrounder.csv')

df.dropna(inplace=True)

#Converting words to integer values
ground=pd.get_dummies(df['Ground'])
pitch=pd.get_dummies(df['Pitch'])
opponent=pd.get_dummies(df['Opponent'])
weather=pd.get_dummies(df['Weather'])
homeaway=pd.get_dummies(df['Home Away'])

df.drop([' Sr.No.','Home Away','Name','Ground','Pitch','Home Strike Rate','Away Strike Rate','Home Average','Away Average','Opponent','Weather'],axis=1,inplace=True)

df=pd.concat([df,ground,pitch,opponent,weather,homeaway],axis=1)

X=df.drop('Result',axis=1)

y=df['Result']

from sklearn.ensemble import RandomForestClassifier
rfmodel=RandomForestClassifier()

#Fitting model with training data
rfmodel.fit(X, y)

# Saving model to disk
pickle.dump(rfmodel, open('allrounder_model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('allrounder_model.pkl','rb'))
