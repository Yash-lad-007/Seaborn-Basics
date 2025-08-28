import seaborn as sns
import matplotlib.pyplot as plt

# Load a sample dataset from Seaborn
tips = sns.load_dataset("tips")

# Show the first 5 rows
print("Sample Data:")
print(tips.head())

# 1. Simple scatter plot
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
plt.title("Scatter Plot: Total Bill vs Tip")
plt.show()

# 2. Histogram of total_bill
sns.histplot(tips["total_bill"], bins=20, kde=True)
plt.title("Histogram: Total Bill")
plt.show()

# 3. Boxplot for day vs total_bill
sns.boxplot(data=tips, x="day", y="total_bill", palette="Set2")
plt.title("Boxplot: Total Bill by Day")
plt.show()

# 4. Heatmap of correlation
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
