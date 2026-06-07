# 🥗 Daily Calorie Tracker

A simple Python program that helps users track their daily calorie intake by recording meal details, calculating totals, and optionally saving a neatly formatted report to a text file.

---

## 📘 Project Overview

This project was created as part of a Python programming assignment.  
It demonstrates user input handling, lists, loops, conditionals, formatted string output, and file handling with timestamps.

---

## ⚙️ Features

- Input multiple meals and their calorie counts  
- Calculate total and average daily calories  
- Compare total calories with a daily limit  
- Display results in a neatly formatted table  
- Option to save the session summary to a `.txt` file  

---

## 🧩 Tasks Implemented

### **Task 1:** User Input  
Prompt the user to enter meal names and calorie values.

### **Task 2:** Store & Calculate  
Store meal data in lists and compute the total and average calories.

### **Task 3:** Calorie Limit Check  
Ask for the daily calorie limit and compare it with total calories.

### **Task 4:** Display Result Message  
Show a message indicating whether the user is within or above their limit.

### **Task 5:** Neatly Formatted Output  
Use formatted strings (`f-strings`) to display data in a table format.

### **Task 6 (Bonus): Save Session Log to File**  
Ask if the user wants to save the report.  
If yes, use `open("calorie_log.txt", "w")` to write:
- Timestamp  
- Meal details  
- Total and average calories  
- Limit status  

---
# Sample Output
========== Daily Calorie Summary ==========
Meal Name      Calories  
------------------------------
Breakfast      350.00    
Lunch          600.00    
Dinner         500.00    
------------------------------
Total:         1450.00   
Average:       483.33    
Great job! You are within your daily calorie limit!
===========================================


# Acknowledgment 
Help has been taken from
*W3 School 
*Python offical documentation
*Youtube

# All the meal record will be saved in Meal_record.txt file to store the data

# Author 
Sameer Mishra