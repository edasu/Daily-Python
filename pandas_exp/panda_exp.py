# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.read_csv('/content/sample_data/Automobile.csv')
df.head()

df.isnull()

df.isnull().sum() #there is not null value in data

df.shape

df.index

df.columns

df['horsepower']

df[df["price"]>30000][['make','price']]

df[df["horsepower"]<100][['make','horsepower']]

df[df["horsepower"]<100][['horsepower']].count()

df.describe().T

df['price'].mean

#The **count**  method will show you the number of values for each column in your DataFrame. 

#The **value_count** method will return the number of unique values for a particular column higher to low. 



df["make"].value_counts().head(3)