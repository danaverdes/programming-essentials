# ex 1
num = int(input("Enter a number: "))
if num % 3 == 0:
    print(num, "is a triple")
else:
    print(num, "is not divisable by 3")

# ex 2
birth_year = int(input("Enter your year of birth: "))
if 2025 > birth_year >= 0:
    age = 2025 - birth_year
    if age >= 18:
        print("Your age =", age)
        print("So you're an adult")
    else:
        print("Your age =", age)
        print("You're not an adult yet. Stop drinking!")
else:
    print("Do you even exist?")

# ex 3
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))

if n1 < n2 and n1 < n3:
    print(n1)
elif n2 < n1 and n2 < n3:
    print(n2)
else:
    print(n3)

# ex 4
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))

if n1 + n2 == n3 or n1 + n3 == n2 or n2 + n3 == n1:
    print("This works")
else:
    print("This won't work")

# ex 5
num = int(input("Enter a number: "))
digit = int(input("What final digit do you want to test with: "))

if num > 0:
    if num % 10 == digit:
        print(num, "ends in", digit)
    else:
        print(num, "doesn't end in", digit)

# ex 6
is_morning = True
is_mother = True
is_asleep = False

if is_morning:
    if is_mother:
        print("Answering my phone.")
    else:
        print("I'm not answering my phone.")
elif is_asleep:
    print("I'm not answering my phone")

# ex 7
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

num1 = abs(num1)
num2 = abs(num2)

if num1%5 == 0 and num2%5 == 0:
        if num1 > num2:
            print(num2)
        else:
            print(num1)
elif num1 == num2:
        print(0)
else:
    if num1 > num2:
        print(num1)
    else:
        print(num2)

# ex 8
wine = int(input("How many bottles of wie are there: "))
pizza = int(input("How many pizzas? are there: "))
judge = "temp"

if wine >= 5 and pizza >= 5:
    if pizza >= 2*wine or wine >= 2*pizza:
        judge = "fantastic"
    else:
        judge = "good"
else:
    judge = "stupid"

print("This is a", judge, "party")

# ex 9
num1 = int(input("number 1 (0,1 or 2): "))
num2 = int(input("number 2 (0,1 or 2): "))
num3 = int(input("number 3 (0,1 or 2): "))

if num1 == num2 == num3 == 2:
    print(10)
elif num1 == num2 == num3 != 2:
        print(5)
else:
        if num2 != num1 and num3 != num1:
            print(1)
        else:
            print(0)

# ex 10
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

if 30 <= num1 <= 40 and 30 <= num2 <= 40:
    print("Both numbers are ok")
elif num1 in [65,72,83,90] and num2 in [65,72,83,90]:
    print("Both numbers are ok")
else:
    print("They are NOT ok")

# ex 11
weight = float(input("Your weight in kilograms: "))
length = float(input("Your length in centimeters: "))
BMI = (weight / (length * length))*10000
result = ""
match BMI:
    case BMI if BMI < 18:
        result = "underweight"
    case BMI if 18 <= BMI < 25:
        result = "normal weight"
    case BMI if 25 <= BMI < 27:
        result = "slightly overweight"
    case BMI if 27 <= BMI < 30:
        result = "moderate overweight"
    case BMI if 30 <= BMI < 40:
        result = "obese"
    case BMI if 40 >= BMI:
        result = "sickly obese"

print("A person of", weight," kg with a length of", length,"cm has as BMI", BMI)
if result == "underweight" or result == "obese":
    print("This is an", result, "weight.")
else:
    print("This is a", result, "weight.")

# # ex 12
age = int(input("Your age: "))
result = ""
match age:
    case age if 6 <= age <= 7:
        result = "Beavers"
    case age if 8 <= age <= 10:
        result = "Cubs"
    case age if 11 <= age <= 13:
        result = "Scouts"
    case age if 14 <= age <= 18:
        result = "Explorers"
    case age if 18 < age:
        result = "Leaders"
    case age if 5 >= age:
        result = "too young"
    case age if age < 0:
        result = "Nope."

if result == "too young":
    print("You're too young")
else:
    print("You'll be assigned to the", result)

# ex 13
import random
my_choice = input("Enter your choice: ")
list = ["rock", "paper", "scissors"]
pc_choice = random.choice(list)
print("I choose", pc_choice)
if my_choice == pc_choice:
    print("It's a tie")
elif (my_choice == "paper" and pc_choice == "rock") or (my_choice == "rock" and pc_choice == "scissors") or (my_choice == "scissors" and pc_choice == "paper"):
    print("You win :3")
else:
    print("You lose :3")

# ex 14
curr_day = input("Enter the current day: ").capitalize() # added capitalization so monday or Monday either work
work_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
value = ""

match curr_day:
    case curr_day if curr_day in work_day:
        value = "weekday"
    case curr_day if weekend in weekend:
        value = "weekend"
    case _:
        value = "invalid"

nth = ""
match curr_day:
    case "Monday":
        nth = "1st"
    case "Tuesday":
        nth = "2nd"
    case "Wednesday":
        nth = "3rd"
    case "Thursday":
        nth ="4th"
    case "Friday":
        nth ="5th"
    case "Saturday":
        nth = "6th"
    case "Sunday":
        nth ="7th"
    case _:
        nth = "Invalid"

if curr_day in work_day or curr_day in weekend:
    print("This is a " + value + ". It is the " + nth + " day of the week.")
else:
    print(nth,"entry")

