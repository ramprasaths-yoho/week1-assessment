import csv
from pathlib import Path

# Find the project folder automatically
PROJECT_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = PROJECT_DIR / "data" / "employees.csv"


# Function with default arguments, *args and **kwargs
def bonus(salary, rate=0.1, *extras, **options):
    total = salary * rate + sum(extras)

    if "cap" in options:
        total = min(total, options["cap"])

    return total


# Custom exception
class InvalidSalaryError(Exception):
    pass


# Employee class
class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


# Manager inherits Employee
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"Name: {self.name}, Salary: {self.salary}, " f"Team size: {self.team_size}"
        )


# Read employee data
with open(CSV_FILE, newline="", encoding="utf-8") as file:
    employees = list(csv.DictReader(file))


# List comprehension
high_earners = [e["name"] for e in employees if int(e["salary"]) > 50000]

print("Above 50000:", high_earners)


# Map and lambda: add a 10% raise
raised_salaries = list(map(lambda e: int(e["salary"]) * 1.10, employees))

print("Raised salaries:", raised_salaries)


# Filter Chennai employees
chennai_employees = list(filter(lambda e: e["city"] == "Chennai", employees))

print("Chennai:", [e["name"] for e in chennai_employees])


# Test the bonus function
print("Bonus:", bonus(30000, 0.1, 500, cap=3500))


# Test Employee and Manager
employee = Employee("Arun", 30000)
print("Annual salary:", employee.annual_salary())

manager = Manager("Priya", 60000, 5)
print(manager.get_details())


# Exception handling
try:
    Employee("Test", -500)

except InvalidSalaryError as error:
    print("Error:", error)

finally:
    print("Transaction finished")


# Continue and break
for e in employees:
    salary = int(e["salary"])

    if salary == 0:
        continue

    if salary > 85000:
        break

    print("Checked:", e["name"])
