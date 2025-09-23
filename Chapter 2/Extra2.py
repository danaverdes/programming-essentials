# ex 1
year = int(input("Enter your year: "))
year_value = ""
if 0 <= year < 1582:
    if year % 4 == 0:
        year_value = "Yes"
    else:
        year_value = "No"
elif year >= 1582:
    match year:
        case year if (year % 4000 == 0) or (year % 100 == 0):
          year_value = "No"
        case year if (year % 400 == 0) or (year % 4 == 0):
          year_value = "Yes"
else:
          year_value = "Invalid"

print("Year | Leap Year?")
print(year, "|", year_value)

# ex 2
name = input("Enter your name: ")
nine_digits = input("Enter first 9 digits of your NN: ")
two_digits = input("Enter the last 2 digits of your NN: ")
gender = ""
if two_digits == "00":
    print("Hello" + name + ", the national name you gave is not correct.")
else:
    if int(nine_digits) % 2 == 0:
        gender = "female"
    else:
        gender = "male"
    print("Hello " + name + ", your gender is " + gender)

month = (int(nine_digits) // 100000) % 100
day = (int(nine_digits) // 1000) % 100
year = (int(nine_digits) // 10000000)
print(f"Your birthday is {day}/{month}/{year}.")

# ex 3
letter = input("Enter your letter: ")
if letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
    print("Vowel")
elif letter == "y":
    print("Exception")
else:
    print("Consonant")


