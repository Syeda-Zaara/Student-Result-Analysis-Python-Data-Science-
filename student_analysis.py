import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

# Calculate Average Marks
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

# Identify Top Performer
top_student = df.loc[df["Average"].idxmax()]

# Display Results
print("\n📊 Student Data:\n", df)
print("\n🏆 Top Performer:")
print(top_student)

# Class Average
class_avg = df["Average"].mean()
print(f"\n📈 Class Average: {class_avg:.2f}")

# Plot Graph
df.plot(x="Name", y=["Maths", "Science", "English"], kind="bar")
plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()