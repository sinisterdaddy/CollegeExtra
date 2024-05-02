import numpy as np
import matplotlib.pyplot as plt

# Generate 100 random numbers for the salary attribute (100K-1000K)
randomlist = np.random.randint(100000, 1000000, size=100)

# Plot equal-width histogram (10 bins)
n, bins, patches = plt.hist(randomlist, bins=10, edgecolor='black')
plt.title('Equal-Width Histogram')
plt.show()

# Function to compute equal-frequency bins
def equalObs(x, nbin):
    nlen = len(x)
    return np.interp(np.linspace(0, nlen, nbin + 1), np.arange(nlen), np.sort(x))

# Plot equal-frequency histogram (20 values)
n, bins, patches = plt.hist(randomlist, equalObs(randomlist, 20), edgecolor='black')
plt.title('Equal-Frequency Histogram')
plt.show()

# Sampling techniques
from random import choices, sample

strata = ["low", "medium", "high"]
randomlist2 = np.random.randint(100, 1000, size=100)  # Assuming 100 values for demonstration

# Simple random sampling without replacement
srs_wr = choices(randomlist2, k=5)
print("Simple Random Sampling with Replacement:", srs_wr)

# Simple random sampling with replacement
srs_wo_wr = sample(randomlist2, 5)
print("Simple Random Sampling without Replacement:", srs_wo_wr)

# Stratified sampling
stratum = np.random.choice(strata, size=100, p=[0.3, 0.4, 0.3])  # Assuming stratification for demonstration
stratified_sample = [sample(randomlist2[stratum == s], 1)[0] for s in strata]
print("Stratified Sampling:", stratified_sample)



import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np
import matplotlib.pyplot as plt
# a.
df = pd.read_csv('crx.data', header=None)
df.columns = ['A'+str(i) for i in range(1, 17)]  # Assigning column names A1 to A16
df = df.replace('?', np.nan)
df['A2'] = df['A2'].astype(float)
df['A14'] = df['A14'].astype(float)
df['A16'] = df['A16'].map({'+': 1, '-': 0})
df.to_csv('Transformed_crx.csv', index=False)

# b.
df1 = pd.read_csv('Transformed_crx.csv')
print("Percentage of missing values for each variable:\n", (df1.isnull().sum() / len(df1)).sort_values())

df2 = df1.dropna()
print("Original dataset size:", df1.shape)
print("Complete case dataset size:", df2.shape)

# c.
num_vars = ['A2', 'A3', 'A8', 'A11', 'A15']
imputer_mean = SimpleImputer(strategy='mean')
imputer_median = SimpleImputer(strategy='median')

df_mean = pd.DataFrame(imputer_mean.fit_transform(df1[num_vars]), columns=num_vars)
df_median = pd.DataFrame(imputer_median.fit_transform(df1[num_vars]), columns=num_vars)

# d.
cat_vars = ['A4', 'A5', 'A6', 'A7']
imputer_mode = SimpleImputer(strategy='most_frequent')

df_mode = pd.DataFrame(imputer_mode.fit_transform(df1[cat_vars]), columns=cat_vars)

# e.
from sklearn.linear_model import LinearRegression

for var in num_vars:
    df_missing = df1[df1[var].isnull()]
    df_complete = df1.dropna(subset=[var])

    lr = LinearRegression()
    lr.fit(df_complete[['A3', 'A8', 'A11', 'A15']], df_complete[var])
    predicted_values = lr.predict(df_missing[['A3', 'A8', 'A11', 'A15']])
    df1.loc[df1[var].isnull(), var] = predicted_values

print("Attributes 'A3', 'A8', 'A11', 'A15' have been imputed using linear regression.")
print(df1.isnull().sum())
