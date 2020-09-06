import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
df = pd.read_csv(r'C:\Users\10652542\Documents\dataa.csv')
df.head()

df['marriage'].value_counts()

df.replace({"married": 0, "unmarried": 1, "divorced": 2,}, inplace = True)

df['gender'].value_counts()

df.replace({"male": 0, "female": 1}, inplace = True)

df['children'].value_counts()
df.replace({"have": 0, "don't have": 1}, inplace = True)

df['education'].value_counts()
df.replace({"Junior school": 0, "masters": 1, "bachelors": 2}, inplace = True)

df['car'].value_counts()
df.replace({"no": 0, "yes": 1}, inplace = True)

df['house'].value_counts()
df.replace({"own": 0, "rent": 1, "parent's house": 2}, inplace = True)

df['jobtitle'].value_counts()
Jobtitle = pd.get_dummies(df["jobtitle"], drop_first= True)

df = pd.concat([df, Jobtitle], axis = 1)
df.drop(["jobtitle"], axis = 1, inplace = True)
df

df=pd.read_csv(r'C:\Users\10652542\Documents\data1.csv')
X=df.iloc[:,:-1]
y=df['defaulter']

ordered_rank_features = SelectKBest(score_func=chi2,k=20)
ordered_feature = ordered_rank_features.fit(X,y)

dfscores = pd.DataFrame(ordered_feature.scores_,columns=["Score"])
dfcolumns = pd.DataFrame(X.columns)

features_rank=pd.concat([dfcolumns,dfscores],axis=1)

features_rank.columns=['Features','Score']
features_rank

features_rank.nlargest(10,'Score')

from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
model=ExtraTreesClassifier()
model.fit(X,y)

print(model.feature_importances_)

ranked_features=pd.Series(model.feature_importances_,index=X.columns)
ranked_features.nlargest(10).plot(kind='barh')
plt.show()

import seaborn as sns
corr=df.iloc[:,:-1].corr()
top_features=corr.index
plt.figure(figsize=(20,20))
sns.heatmap(df[top_features].corr(),annot=True)

threshold=0.8
def correlation(dataset, threshold):
    col_corr = set()  # Set of all the names of correlated columns
    corr_matrix = df.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold: # we are interested in absolute coeff value
                colname = corr_matrix.columns[i]  # getting the name of column
                col_corr.add(colname)
            return col_corr

s = correlation(df.iloc[:,:-1],threshold)
