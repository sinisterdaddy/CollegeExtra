import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv("bank.csv")
df = pd.DataFrame(data)
data.head()

# Define a function to transform marital status column
def transformMarital(column, value):
    data[column] = np.where(data[column].str.contains(value), 0, 1)

# Call the function to transform marital status column
transformMarital("marital", "single")

# Additional transformation of columns
df['housing'] = df['housing'].map({'no': 0, 'yes': 1})
df['loan'] = df['loan'].map({'no': 0, 'yes': 1})

# Job mapping
job_mapping = {'unknown': np.nan, 'management': 0, 'technician': 1, 'entrepreneur': 2, 
               'blue-collar': 3, 'retired': 4, 'admin.': 5, 'services': 6, 'self-employed': 7,
               'unemployed': 8, 'housemaid': 9, 'student': 10}
df['job'].replace(job_mapping, inplace=True)

# Education mapping
education_mapping = {'unknown': np.nan, 'tertiary': 0, 'secondary': 1, 'primary': 2}
df['education'].replace(education_mapping, inplace=True)

# Default mapping
df['default'] = df['default'].map({'no': 0, 'yes': 1})

# Contact mapping
contact_mapping = {'unknown': np.nan, 'telephone': 0, 'cellular': 1}
df['contact'].replace(contact_mapping, inplace=True)

# Month mapping
month_mapping = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8,
                 "sep": 9, "oct": 10, "nov": 11, "dec": 12}
df['month'].replace(month_mapping, inplace=True)

# Poutcome mapping
df['poutcome'].replace({'failure': 0, "unknown": np.nan, 'success': 2, 'other': 1}, inplace=True)

# Target variable mapping
df['y'] = df['y'].map({'no': 0, 'yes': 1})

# Saving processed data to a new CSV file
df.to_csv('processed_bank_Q1.csv', index=False)

# Function for min-max normalization
def minmax(df, column):
    df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    return df

# Function for z-score normalization
def zscore(df, column):
    mean = np.mean(df[column])
    std = np.std(df[column])
    threshold = 3
    outlier = []
    for i in df[column]:
        z = (i - mean) / std
        if z > threshold:
            outlier.append(i)
    return outlier

# Plotting and normalization
fig, axs = plt.subplots(3, figsize=(10, 8))
fig.suptitle('Data Normalization')

axs[0].scatter(df.index, df["duration"])
axs[0].set_title("Before min-max norm")
df = minmax(df, "duration")

axs[1].scatter(df.index, df["pdays"])
axs[1].set_title("Before min-max norm")
df = minmax(df, "pdays")

axs[2].scatter(df.index, df["balance"])
axs[2].set_title("Before min-max norm")
df = minmax(df, "balance")

# Applying z-score normalization
outliers_duration = zscore(df, "duration")
outliers_pdays = zscore(df, "pdays")
outliers_balance = zscore(df, "balance")

plt.show()
