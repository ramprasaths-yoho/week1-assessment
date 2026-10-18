import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Locate the project folder
project = Path(__file__).resolve().parent.parent

# Read employee data
df = pd.read_csv(project / "data" / "employees.csv")

# Display the data
print("Employee Details:")
print(df)

# Display basic information
print("\nData Information:")
df.info()

# Find employees earning above 50000
print("\nHigh Earners:")
print(df[df["salary"] > 50000])

# Count employees in each department
print("\nDepartment Headcount:")
print(df.groupby("department")["id"].count())

# Calculate average salary
avg_salary = df.groupby("department")["salary"].mean()

# Create a bar chart
avg_salary.plot(kind="bar", color="skyblue")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend(["Average Salary"])
plt.tight_layout()

# Save the chart
chart_folder = project / "reports" / "charts"
chart_folder.mkdir(parents=True, exist_ok=True)

plt.savefig(chart_folder / "salary_chart.png")
plt.show()