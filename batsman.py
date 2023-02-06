# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

df = pd.read_csv('bat.csv')

df.dropna(inplace=True)

#Converting words to integer values
ground=pd.get_dummies(df['Ground'])
pitch=pd.get_dummies(df['Pitch'])
opponent=pd.get_dummies(df['Opponent'])
weather=pd.get_dummies(df['Weather'])
homeaway=pd.get_dummies(df['Home Away'])

df.drop(['Home Away','Name','Sr.No.','Runs','Ground','Pitch','Fours','Sixes','Strike Rate','Opponent','Weather'],axis=1,inplace=True)

df=pd.concat([df,ground,pitch,opponent,weather,homeaway],axis=1)

X=df.drop('Result',axis=1)

y=df['Result']

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.


from sklearn.ensemble import RandomForestClassifier
rfmodel=RandomForestClassifier()

#Fitting model with training data
rfmodel.fit(X, y)

# Saving model to disk
pickle.dump(rfmodel, open('batsman_model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('batsman_model.pkl','rb'))
