# -*- coding: utf-8 -*-
"""Age_Calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zrzuk0QMtdQe1MlYNn5DGaHzONC-b7fD

# Import Libraries
"""

from datetime import datetime, timedelta
import time

"""# Age Calculator Function"""

def calculate_age(birth_datetime):
    today = datetime.now()
    age = (today - birth_datetime).total_seconds() / (365.25 * 24 * 60 * 60)
    return round(age, 9)

"""# Main Function"""

def main():
    try:
        year = int(input("Enter the year of your birthday (YYYY): "))
        month = int(input("Enter the month of your birthday (1-12): "))
        day = int(input("Enter the day of your birthday (1-31): "))
        hour = int(input("Enter the hour of your birthday (0-23): "))
        minute = int(input("Enter the minute of your birthday (0-59): "))

        birthday = datetime(year, month, day, hour, minute)
        while True:
            age = calculate_age(birthday)
            print("{:.9f}".format(age))
            time.sleep(3)
    except ValueError:
        print("Please enter valid date and time components.")
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()

"""# Age-Calculator

### There is a simple code for **show your age exact**. This code get your exact time of birthady like 3.10.2002, 12:00, and calculate your age and update it each 3 seconds. You can run Age_Calculator.py file to look your age online :)
"""