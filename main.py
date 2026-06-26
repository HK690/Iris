# Iris Dataset Data Visualization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
# Replace the path below with your local dataset path
iris = pd.read_csv("filepath/Iris.csv")

# Display basic information
print("Dataset Information")
print(iris.info())

print("\nUnique Species")
print(np.unique(iris["Species"]))

print("\nMaximum Values")
print(iris.max())

print("\nMinimum Values")
print(iris.min())

print("\nStatistical Summary")
print(iris.describe())

# -------------------------------
# Histograms
# -------------------------------

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

axes[0, 0].set_title("Sepal Length Distribution")
axes[0, 0].hist(iris["SepalLengthCm"])

axes[0, 1].set_title("Sepal Width Distribution")
axes[0, 1].hist(iris["SepalWidthCm"])

axes[1, 0].set_title("Petal Length Distribution")
axes[1, 0].hist(iris["PetalLengthCm"])

axes[1, 1].set_title("Petal Width Distribution")
axes[1, 1].hist(iris["PetalWidthCm"])

plt.tight_layout()
plt.show()

# Histogram using Seaborn

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

sns.histplot(iris["SepalLengthCm"], ax=axes[0, 0])
sns.histplot(iris["SepalWidthCm"], ax=axes[0, 1])
sns.histplot(iris["PetalLengthCm"], ax=axes[1, 0])
sns.histplot(iris["PetalWidthCm"], ax=axes[1, 1])

plt.tight_layout()
plt.show()

# -------------------------------
# Boxplots
# -------------------------------

fig, axes = plt.subplots(2, 2, figsize=(16, 8))

sns.boxplot(data=iris, x="Species", y="PetalLengthCm", ax=axes[0, 0])
sns.boxplot(data=iris, x="Species", y="PetalWidthCm", ax=axes[0, 1])
sns.boxplot(data=iris, x="Species", y="SepalLengthCm", ax=axes[1, 0])
sns.boxplot(data=iris, x="Species", y="SepalWidthCm", ax=axes[1, 1])

plt.tight_layout()
plt.show()
