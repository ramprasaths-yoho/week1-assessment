import csv
import json
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("API_KEY")

print("API key loaded:", bool(api_key))


# Read employees.csv
with open("data/employees.csv", newline="") as file:
    employees = list(csv.DictReader(file))

print("Rows read:", len(employees))


# Write employees.json
with open("data/employees.json", "w") as file:
    json.dump(employees, file, indent=4)


# Write high_earners.csv
high_earners = [e for e in employees if int(e["salary"]) > 50000]

with open("data/high_earners.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=employees[0].keys())
    writer.writeheader()
    writer.writerows(high_earners)

print("High earners:", len(high_earners))


# Call the users API
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
    response.raise_for_status()
    users = response.json()

    for user in users[:3]:
        print(user["id"], "-", user["name"], "-", user["email"])

    # Read a nested JSON field using get()
    company = users[0].get("company", {})
    company_name = company.get("name", "Unknown")

    with open("data/users.json", "w") as file:
        json.dump({"users": users, "first_company": company_name}, file, indent=4)

except requests.exceptions.Timeout:
    print("Error: Request timed out")

except requests.exceptions.ConnectionError:
    print("Error: Connection failed")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)


# Test a missing user endpoint
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999", timeout=5
    )

    if response.status_code == 404 or response.json() == {}:
        print("/users/9999 -> 404 Not found")
    else:
        response.raise_for_status()
        print("Unexpected response:", response.status_code)

except requests.exceptions.Timeout:
    print("Error: Request timed out")

except requests.exceptions.ConnectionError:
    print("Error: Connection failed")

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
