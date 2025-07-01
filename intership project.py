import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the dataset
df = pd.read_csv("C:\\Users\\Yashika malik\\Downloads\\Titanic-Dataset.csv")
print(df)

sns.set(style="whitegrid")
plt.style.use("ggplot")

# Display the first 5 rows
print(df.head())

# Display the last 5 rows
print(df.tail())

# Step 3: Dataset overview
print("Shape of dataset:", df.shape)
print(df.info())

# Step 4: Basic statistics of numerical columns
print(df.describe())

# Step 5: Check missing values
print(df.isnull().sum())


#Step 6: Data Cleaning
# Fill missing Age values with median
df['Age'] = df['Age'].fillna(df['Age'].median())
print(df['Age'])
print (df['Embarked'].fillna(df['Embarked'].mode()[0]))
print(df['Embarked'])
print(df.drop('Cabin', axis=1))
print(df.dropna())
print(df.dropna(inplace=True))


#Step 7: Age Distribution
bins = [0, 20, 64, 100]
labels = ['0-20 Years', '21-64 Years', '65+ Years']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
grouped = df['AgeGroup'].value_counts().sort_index()
colors = ['#ffe600', '#008cff', '#ff2cb4']

plt.figure(figsize=(10, 6))
plt.bar(grouped.index, grouped.values, color=colors, width=0.6)

for i, val in enumerate(grouped):
    pct = (val / grouped.sum()) * 100
    plt.text(i, val + 10, f'{val} ({pct:.1f}%)', ha='center', fontsize=12, fontweight='bold')

plt.title("Titanic Passenger Distribution by Age Group", fontsize=16, fontweight='bold')
plt.xlabel("Age Group")
plt.ylabel("Passenger Count")
plt.tight_layout()
plt.show()

#Step 8: Exploratory Data Analysis (EDA)
# 1. Survival Count
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()

# 2. Survival by Gender
sns.countplot(x='Survived', hue='Pclass', data=df)
plt.title("Survival by Gender")
plt.xlabel("Survived")
plt.ylabel("Count")
plt.show()

# 3. Survival by Passenger Class
sns.countplot(x='Survived', hue='Embarked', data=df)
plt.title("Survival by Passenger Class")
plt.xlabel("Survived")
plt.ylabel("Count")
plt.show()

# 4. Age Distribution
sns.histplot(df['Age'], kde=True, bins=30)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
# 5. Boxplot: Age vs Survived
sns.boxplot(x='Survived', y='Age', data=df , color='red')
plt.title("Age vs Survival")
plt.xlabel("Survived")
plt.ylabel("Age")
plt.show()

# Step 9: Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.show()

# Step 10: Donut chart of Survival distribution
survival_counts = df['Survived'].value_counts()
labels = ['Did Not Survive', 'Survived']
colors = ['#ff9999','#66b3ff']

fig, ax = plt.subplots()
ax.pie(survival_counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
centre_circle = plt.Circle((0,0),0.70,fc='White')
fig.gca().add_artist(centre_circle)

ax.axis('equal')  
plt.title('Survival Distribution - Donut Chart')
plt.show()

#Scatter Plot: Age vs Fare colored by Survival
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df, palette='colorblind')
plt.title("Scatter Plot: Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

# Group by survival and show average values
df.groupby('Survived').mean(numeric_only=True)






