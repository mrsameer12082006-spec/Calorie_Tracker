#------------------------------Self introduction----------------------------------------------------------------------------------------------------------------------------
"""Name=Sameer Mishra is god isnot it 
   Date=5 october 2025
   project= A Calorie Tracking Console App"""

import datetime
# ---------------- Task 1: Setup & Introduction ----------------
print("=======================================================")
print("     Welcome to Daily Calorie Tracker")
print("=======================================================")
print("This tool helps you record your meals, track calories,")
print("and compare against your daily calorie limit.")
print("It wil also save your meals records with date.")

# ---------------- Task 2: Input & Data Collection ----------------
meals = []
calories = []

# Taking the no of meal input from the user.
num_meals = int(input("how many meals did you have today? "))

for i in range(num_meals):
    meal_name = input(f"Enter meal {i+1} name: ")
    meal_calories = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(meal_calories)

# ---------------- Task 3: Calorie Calculations ----------------
total_calories = sum(calories)
average_calories = total_calories / len(calories)

# Ask for daily limit
daily_limit = float(input("\nEnter your daily calorie limit: "))

# ---------------- Task 4: Exceed Limit Warning System ----------------
if total_calories > daily_limit:
    status_message = " Warning: You have exceeded your daily calorie limit!"
else:
    status_message = " Great job! You are within your daily calorie limit."

# ---------------- Task 5: Neatly Formatted Output ----------------
print("\n=========== Daily Calorie Summary ===========")
print(f"{'Meal Name':<15}{'Calories':<10}")
print("-" * 30)
for meal, cal in zip(meals, calories):
    print(f"{meal:<15}{cal:<10.2f}")
print("-" * 30)
print(f"{'Total:':<15}{total_calories:<10.2f}")
print(f"{'Average:':<15}{average_calories:<10.2f}")
print(status_message)
print("=============================================\n")

# ---------------- Task 6 (Bonus): Save Session Log ----------------
save_option = input("Do you want to save this report to a file? (yes/no): ").strip().lower()

if save_option in ["yes", "y"]:
    filename = "Meal_record.txt"
    with open(filename, "a") as f:
        f.write("Daily Calorie Tracker Log\n")
        f.write(f"Date: {datetime.datetime.now()}\n\n")
        f.write(f"{'Meal Name':<15}{'Calories':<10}\n")
        f.write("-" * 30 + "\n")
        for meal, cal in zip(meals, calories):
            f.write(f"{meal:<15}{cal:<10.2f}\n")
        f.write("-" * 30 + "\n")
        f.write(f"{'Total:':<15}{total_calories:<10.2f}\n")
        f.write(f"{'Average:':<15}{average_calories:<10.2f}\n")
        f.write(status_message + "\n")
    print(f" Report saved successfully in {filename}")
else:
    print("Report not saved. Exiting program.")

