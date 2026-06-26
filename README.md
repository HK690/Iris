# 🌸 Iris Dataset Data Visualization

A simple Data Visualization project using the famous Iris dataset. This project demonstrates how to perform exploratory data analysis (EDA) by visualizing feature distributions and identifying outliers using Python.

---

## 📌 Project Overview

The notebook performs the following tasks:

- Load the Iris dataset
- Display dataset information
- Identify feature types
- Generate statistical summaries
- Plot histograms for each numerical feature
- Plot boxplots to detect outliers
- Compare feature distributions across species

---

## 📂 Dataset

The project uses the **Iris Dataset**, which contains measurements of iris flowers from three different species.

### Features

| Feature | Type |
|---------|------|
| SepalLengthCm | Numeric |
| SepalWidthCm | Numeric |
| PetalLengthCm | Numeric |
| PetalWidthCm | Numeric |
| Species | Categorical |

---

## 📊 Visualizations

### Histograms
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

These plots show the distribution of each numerical feature.

### Boxplots
Boxplots are created for all numerical features grouped by species to identify:

- Median
- Quartiles
- Spread
- Outliers

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 📦 Installation

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

---

## ▶️ Run the Project

1. Download the Iris dataset.
2. Update the dataset path in the script.

```python
iris = pd.read_csv("filepath/Iris.csv")
```

3. Run:

```bash
python iris_data_visualization.py
```

---

## 📈 Expected Output

- Dataset information
- Statistical summary
- Histograms of all numerical features
- Boxplots grouped by species
- Identification of potential outliers

---

## 📚 Learning Objectives

- Exploratory Data Analysis (EDA)
- Data Visualization using Matplotlib
- Data Visualization using Seaborn
- Understanding feature distributions
- Outlier Detection using Boxplots

---

## 👨‍💻 Author

Created as a Data Visualization assignment using the Iris dataset.
