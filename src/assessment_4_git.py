from pathlib import Path

files = [
    "data/employees.csv",
    "data/employees.json",
    "data/high_earners.csv",
    "data/users.json",
    "data/departments.csv",
    "reports/department_summary.csv",
    "reports/bar_chart.png",
    "reports/histogram.png",
    "reports/scatter.png",
    "reports/line_chart.png",
    "notebooks/assessment_3_analysis.ipynb",
    "README.md"
]

print("Assessment 4: Project File Check")

for file in files:
    if Path(file).exists():
        print("Found:", file)
    else:
        print("Missing:", file)
