#DATA TYPES
two_digit_number = input('type a two dogot number')
print(int(two_digit_number[0]) + int(two_digit_number[1]))


#BMI CALCULATOR
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#correct the data types
w = int(weight)
h = float(height)

#calculate
result =  w / h ** 2
print(round(result))

#LIVE IN WEEKS
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_left = 90 - int(age)

days_left = years_left * 365
weeks_left = years_left * 52
mounts_left = years_left * 12
print(f"You have {days_left} days, {weeks_left} weeks, and {mounts_left} months left.")


