import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. NumPy marks analysis


marks = np.array([[80, 75, 90], [65, 70, 72], [90, 88, 95], [72, 80, 85]])

print("Shape:", marks.shape)
print("Student averages:", marks.mean(axis=1))
print("Subject averages:", marks.mean(axis=0))

# Add five grace marks using broadcasting
grace_marks = marks + 5
print("Marks with grace:\n", grace_marks)

# Weighted scores: 30%, 30%, 40%
weights = np.array([0.3, 0.3, 0.4])
weighted_scores = np.dot(marks, weights)

print("Weighted scores:", weighted_scores)


# 2. Load employee data with Pandas


df = pd.read_csv("data/employees.csv")

print("\nData information:")
df.info()

print("\nSalary description:")
print(df.describe())

# loc and iloc
print("\nFirst employee name:")
print(df.loc[0, "name"])

print("\nFirst three employees:")
print(df.iloc[0:3])

# Filter salaries above 50000
print("\nHigh earners:")
print(df[df["salary"] > 50000])


# ----------------------------------
# 3. Create dirty data for cleaning
# ----------------------------------

dirty = df.copy()

# Add two missing salaries
dirty.loc[0, "salary"] = np.nan
dirty.loc[2, "salary"] = np.nan

# Add one duplicate row
dirty = pd.concat([dirty, dirty.iloc[[0]]], ignore_index=True)

dirty.to_csv("data/employees_dirty.csv", index=False)


# 4. Clean the data


clean = pd.read_csv("data/employees_dirty.csv")

# Remove duplicate rows
clean = clean.drop_duplicates()

# Convert salary to numeric and fill missing values
clean["salary"] = pd.to_numeric(clean["salary"], errors="coerce")

median_salary = clean["salary"].median()

clean["salary"] = clean["salary"].fillna(median_salary)
clean["salary"] = clean["salary"].astype(int)

# Correct column types
clean["id"] = clean["id"].astype(int)
clean["name"] = clean["name"].astype(str)
clean["department"] = clean["department"].astype(str)
clean["city"] = clean["city"].astype(str)

print("\nClean rows:", len(clean))
print("Missing salaries:", clean["salary"].isna().sum())
print("Duplicate rows:", clean.duplicated().sum())


# 5. Department data


departments = pd.DataFrame(
    {
        "department": ["Sales", "HR", "IT", "Finance", "Marketing"],
        "head": ["Ravi", "Anu", "Kiran", "Meera", "John"],
        "budget": [200000, 150000, 400000, 250000, 100000],
    }
)

departments.to_csv("data/departments.csv", index=False)


# 6. Groupby and aggregation


summary = clean.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max"),
)

print("\nDepartment summary:")
print(summary)


# 7. Inner, left and outer joins


inner = clean.merge(departments, on="department", how="inner")

left = clean.merge(departments, on="department", how="left")

outer = clean.merge(departments, on="department", how="outer")

print("\nInner join rows:", len(inner))
print("Left join rows:", len(left))

print("\nOuter join:")
print(outer)

# Find departments without employees
employee_departments = set(clean["department"])

empty_departments = departments[~departments["department"].isin(employee_departments)]

print("\nDepartments with no employees:")
print(empty_departments["department"].tolist())

# Save reports
summary.to_csv("reports/department_summary.csv")
outer.to_csv("reports/outer_join.csv", index=False)


# 8. Bar chart


summary["average_salary"].plot(kind="bar", color="skyblue", label="Average salary")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("reports/bar_chart.png")
plt.close()


# 9. Histogram


plt.hist(clean["salary"], bins=5, color="orange", label="Employees")

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()
plt.savefig("reports/histogram.png")
plt.close()


# 10. Scatter plot


plt.scatter(clean["id"], clean["salary"], label="Salary")

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("reports/scatter.png")
plt.close()


# 11. Line chart


ordered = clean.sort_values("id")

plt.plot(ordered["id"], ordered["salary"], marker="o", label="Salary")

plt.title("Salary by Employee ID")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("reports/line_chart.png")
plt.close()


# 12. Finish


print("\nAll four charts saved in reports/")

print("Insight 1: IT has the highest average salary.")
print("Insight 2: The histogram shows salary distribution.")
print("Insight 3: Salaries vary across employee IDs.")
print("Insight 4: The line chart compares salaries by ID.")
