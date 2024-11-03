import csv
from faker import Faker
import random

fake = Faker()
departments = ["HR", "Engineering", "Sales", "Marketing", "Customer Support"]

num_records = 100

with open('database.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Hiring Date", "Department", "Birthday"])

    for _ in range(num_records):
        name = fake.name()
        hire_date = fake.date_between(start_date="-10y", end_date="today")
        department = random.choice(departments)
        birthday = fake.date_of_birth(minimum_age=20, maximum_age=60)

        writer.writerow([name, hire_date, department, birthday])

print(f"{num_records} synthetic employee records have been written to database.csv")

