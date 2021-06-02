import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Apply the default theme
sns.set_theme()

# Change the name for one of the operations performance datasets
df = pd.read_csv("performance_testing/performance_datasets/p_data_performance.csv")

# Create a visualization grouping by the percentage of constraitns
sns.relplot(data=df, x="Features", y="Seconds", hue="Percent_cons", kind="line", aspect=2)

plt.show()
