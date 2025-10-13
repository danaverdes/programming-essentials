# surname = input("Enter your surname: ")
# first_name = input("Enter your first name: ")
# street = input("Enter your street: ")
# number = input("Enter your number: ")
# zip_code = input("Enter your zip code: ")
# city = input("Enter your city: ")
#
# print(first_name, surname)
# print(street, number)
# print(zip_code, city)

#ex 2
# yes_votes = int(input("How many yes votes? "))
# no_votes = int(input("How many no votes? "))
# blank_votes = int(input("How many blank votes? "))
#
# total_votes = yes_votes + no_votes + blank_votes
# yes_votes = yes_votes/total_votes * 100
# no_votes = no_votes/total_votes * 100
# blank_votes = blank_votes/total_votes * 100
#
# print("Yes: " + str(yes_votes) + " %")
# print("No: " + str(no_votes) + " %")
# print("Blank: " + str(blank_votes) + " %")

# ex 3
# number = float(input("Enter a 3-digit number number: "))
# number1 = number//100
# print(int(number1))
# number2 = (number%100)/10
# print(int(number2))
# number3 = number%10
# print(int(number3))

# ex 4
# first_name = input("First name ")
# second_name = input("Second name ")
# print("Before changing:",first_name, second_name)
# print("After changing:", second_name, first_name)

# ex 5
# dollar_rate = float(input('Enter the current exchange dollar rate for euro: '))
# amount = float(input('Enter your amount in euro: '))
# print(amount, "=", dollar_rate * amount)

# ex 6
# number = int(input("Enter a number: "))
# text = input("Enter a text: ")
# print(number, "times your text:", number*text)

# ex 7
# num = 15
# print("The starting number", "=", num)
# num *= 10
# print(num)
# num += 5
# print(num)
# num -= 7
# print(num)
# num += 1
# print(num)
# num *= 100
# print(num)
# num /=2
# print(int(num))1

# ex 8
import datetime
# curr_hour = int(input("Enter the current hour: "))
# sleep_hours = int(input("How long do you want to sleep: "))
# start = datetime.datetime(100, 1, 1, curr_hour)
# end = start + datetime.timedelta(hours=sleep_hours)
# result = str(end.time())
# print("The alarm will sound at:", result, "h")

# ex 8 var 2
# curr_hour = int(input("Enter the current hour: "))
# sleep_hours = int(input("How long do you want to sleep: "))
# hour = curr_hour + sleep_hours
# def awake_time(temp):
#     if curr_hour+sleep_hours >= 24:
#         temp -= 24
#         print(str(temp) + ":00")
#     else :
#         print(str(temp) + ":00")
# awake_time()

#ex 8 var 3
# curr_hour = int(input("Enter the current hour: "))
# sleep_hours = int(input("How long do you want to sleep: "))
# hour = (curr_hour + sleep_hours) % 24
# print(str(hour) + ":00")

# ex 9
# degreeC = float(input("Enter the number of degree in Celsius: "))
# degreeF = degreeC * 9/5 + 32
# print(degreeC, "degrees Celsius", "=", degreeF, "F")

# ex 10
# width = float(input("Width: "))
# breadth = float(input("Breadth: "))
# length = 2*(width+breadth)
# print("You need", length, "metres of wire and", length/3, "poles." )

# ex 11
# fixed_amount = 83.6
# night_rate = 0.073
# day_rate = 0.146
# VAT = 6
# day_power = int(input("Power consumption during the day (kilowatt per hour): "))
# night_power = int(input("Power consumption during the night (kilowatt per hour): "))
# print("Invoice")
# print("**********")
# print("€", fixed_amount)
# print("Daily consumption: €" + str(day_rate*day_power))
# print("Nightly consumption: €" + str(night_rate*night_power))
# print("Total excluding VAT: €" + str(fixed_amount+day_rate*day_power+night_rate*night_power))
# print("Total including VAT: €" + str((fixed_amount+day_rate*day_power+night_rate*night_power)*106/100))

# additional exercises
# odd number verificator
# num = int(input("Enter a number: "))
# def oddness(x):
#     if x % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# oddness(num)

# fibonacci sequence
# num = int(input("Enter a number: "))
# def FibonacciNum(n):
#         if n<=1: return n
#         return FibonacciNum(n-2)+FibonacciNum(n-1)
# print(FibonacciNum(num))

# Check if PIN is only numbers
# pin = input("Type your password: ")
# if pin.isdigit():
#     pin = int(pin)
#     print("Your password is", pin)
# else:
#     print("Denied Access")

# test result (selects results equal to 8 or above, sorts them in desc order)
# result = [10,8,9,8,7,7]
# result.sort(reverse=True)
# for i in result:
#     if i >= 8:
#         print(str(i))