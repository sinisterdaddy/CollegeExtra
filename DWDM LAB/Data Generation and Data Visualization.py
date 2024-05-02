import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
from sklearn import preprocessing 
from faker import Factory
import random 
import numpy as np
from sklearn.datasets import make_regression, make_classification, make_blobs, make_circles, make_moons

# Read the data from the file "data.csv"
data = pd.read_csv("vgsales.csv")
df = pd.DataFrame(data)

# Q1
plt.subplots(figsize=(10, 6))
plt.title("Game Global Sales - Top Ten")
plt.xlabel("Game Rank")
plt.ylabel("Game Global sales")
x = np.array(df['Rank'].iloc[0:10])
y = np.array(df['Global_Sales'].iloc[0:10])
plt.scatter(x, y, color='red')

# Q2
plt.subplots(figsize=(10, 6))
df1 = df.groupby(['Year'], as_index=False)['Global_Sales'].sum()
plt.title("Global Sales by year")
plt.xlabel("Year")
plt.ylabel("Global sales")
df1 = df1.set_index('Year')
df1['Global_Sales'].plot(kind='bar', color='brown')

plt.subplots(figsize=(10, 6))
df1 = df.groupby(['Platform'], as_index=False)['Global_Sales'].sum()
plt.title("Global Sales by Platform")
plt.xlabel("Platform")
plt.ylabel("Global sales")
df1 = df1.set_index('Platform')

# Q3
df2 = df[['Genre', 'NA_Sales', 'EU_Sales', 'JP_Sales']]
df2 = df2.groupby(['Genre'], as_index=False)[['NA_Sales', 'EU_Sales', 'JP_Sales']].sum()
df2.plot(kind='bar', stacked=True, figsize=(12, 6), color=['red', 'blue', 'green'])

# Q4
label_encoder = preprocessing.LabelEncoder()
df['genre_enc'] = label_encoder.fit_transform(df['Genre'])
df42 = df.groupby('genre_enc', as_index=False)[['Name']].count()

fig = plt.figure(figsize=(12, 6))
plt.subplot(231)
plt.title('NA_Sales')
plt.hist(data=data, x='NA_Sales')

plt.subplot(2, 3, 2)
plt.title("EU_Sales")
plt.hist(data=data, x='EU_Sales')

plt.subplot(2, 3, 4)
plt.title("JP_Sales")
plt.hist(data=data, x="JP_Sales")

plt.subplot(235)
plt.title("Global Sales")
plt.hist(data=data, x='Global_Sales')

# Q5
fig = plt.figure(figsize=(12, 7))
x1 = df['NA_Sales']
x2 = df['EU_Sales']
x3 = df['JP_Sales']
x4 = df['Other_Sales']
x = [x1, x2, x3, x4]
plt.boxplot(x)

fig = plt.figure(figsize=(12, 6))
plt.scatter(x=data['Year'], y=data['Global_Sales'])
plt.xlabel('Year')
plt.ylabel('Global Sales')
plt.title('Global Sales by year')

# Q6
fig = plt.figure(figsize=(12, 6))
X_test, y_test = make_regression(n_samples=150, n_features=1, noise=5)
plt.scatter(X_test, y_test)

fig = plt.figure(figsize=(12, 6))
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")

fig = plt.figure(figsize=(12, 6))
X1, Y1 = make_blobs(n_features=2, centers=3)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")

fig = plt.figure(figsize=(12, 6))
X1, Y1 = make_circles(n_samples=100, factor=0.8)
plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1)

fig = plt.figure(figsize=(12, 6))
X1, Y1 = make_moons(n_samples=100)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")

# Q7
fake = Factory.create()
df_fake = pd.DataFrame(columns=["ID", "Name", "Address", "Date", "Gender", "Blood Type", "Phone Number", "Random Number"])
for _ in range(1000):
    df_fake.loc[len(df_fake)] = [
        random.randint(100, 1000000),
        fake.name(),
        fake.address(),
        fake.date_time(),
        np.random.choice(["M", "F"], p=[0.5, 0.5]),
        np.random.choice(["O+", "O-", "AB+", "AB-", "A+", "A-", "B+", "B-"], p=[0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]),
        fake.phone_number(),
        random.randint(1000, 2000)
    ]
df_fake.to_csv('customer.csv', index=False)

plt.show()
