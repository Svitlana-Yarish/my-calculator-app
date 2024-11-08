import csv
from datetime import datetime

file_name = input("Введіть ім'я файлу з даними (наприклад, database.csv): ")
month = int(input("Введіть номер місяця (1-12): "))

with open(file_name, mode='r') as file:
    reader = csv.DictReader(file)
    birthdays = []
    anniversaries = []

    for row in reader:
        name = row["Name"]
        birthday_month = datetime.strptime(row["Birthday"], "%Y-%m-%d").month
        hire_month = datetime.strptime(row["Hiring Date"], "%Y-%m-%d").month

        if birthday_month == month:
            birthdays.append(name)
        
        if hire_month == month:
            anniversaries.append(name)

    print(f"Співробітники з днем народження у місяці {month}: {', '.join(birthdays)}")
    print(f"Співробітники з річницею прийому на роботу у місяці {month}: {', '.join(anniversaries)}")
    print(f"Загальна кількість подарунків: {len(birthdays) + len(anniversaries)}")
