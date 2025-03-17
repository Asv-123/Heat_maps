import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random


# Sample health-related data
data = {
    "Age": [25, 34, 45, 52, 23, 41, 36, 29, 50, 60],
    "BMI": [22.5, 27.3, 30.1, 24.6, 21.8, 28.4, 26.1, 23.9, 31.2, 29.7],
    "Blood Pressure": [120, 135, 140, 130, 118, 138, 132, 125, 145, 142],
    "Cholesterol": [180, 200, 220, 190, 175, 210, 195, 185, 230, 225]
}

# Convert to DataFrame
df = pd.DataFrame(data)

color1 = plt.colormaps()

random1 = random.choice(color1)

# Save as CSV
csv_filename = "health.csv"
df.to_csv(csv_filename, index=False)

# Load the CSV file
df = pd.read_csv(csv_filename)

# Generate correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap=random1, fmt=".2f")
plt.title(f"Correlation Heatmap of Health Data \n color maps:{random1} ")
plt.show()
