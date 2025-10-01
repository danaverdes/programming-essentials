# ex 1a
# product = 1
# num = int(input("Enter a number: "))
# while num != 0:
#     product = num * product
#     num = int(input("Enter a number: "))
# print(product)

# ex 1b
# product = 1
# nrOfNr = 0
# num = int(input("Enter a number: "))
# while num != 0:
#     product = num * product
#     nrOfNr += 1
#     num = int(input("Enter a number: "))
# print("The product of the", nrOfNr, "numbers is", product)

# ex 2
# num = int(input("Enter a number: "))
# theSix = 0
# theZero = 0
# while num !=0:
#     rest = num % 10
#     if rest == 6:
#         theSix += 1
#     if rest == 0:
#         theZero += 1
#     num = num // 10
#
# print(theSix, theZero)

# ex 3
# yourAge = int(input("How old are you: "))
# fatherAge = int(input("How old is your father: "))
# i = 0
# if yourAge > fatherAge/2:
#     print("The situation is no longer possible for you")
#
# while yourAge < fatherAge/2:
#     i += 1
#     yourAge += 1
#     fatherAge += 1
#     if fatherAge == yourAge*2:
#         print("Within", i, "your father will be twice your age")
#         print("Your father will be", fatherAge, "and you will be", yourAge)

# ex 4
# import random
# pcNum = random.choice(range(1,101))
#
# userNum = int(input("Enter your positive number: "))
# i = 0
# while 0 < userNum < 100 and userNum != pcNum:
#     i += 1
#     if userNum < pcNum:
#         print("Higher!")
#     elif userNum > pcNum:
#         print("Lower!")
#     userNum = int(input("Enter your positive number: "))
# print("You have guessed the number", userNum, "in", i)

# ex 5
# num = int(input("Enter a number: "))
# if num == 0:
#     print("No numbers entered")
# else:
#     largestNum = num
#     smallestNum = num
#     while num!=0:
#         if num > largestNum:
#             largestNum = num
#         elif num < smallestNum:
#             smallestNum = num
#         num = int(input("Enter a number: "))
#     print("The difference between:"1, largestNum, "and the smallest", smallestNum, "=", largestNum - smallestNum)

# ex 6
# num = int(input("Enter a number: "))
# for i in range(num, -1, -1):
#     print(i, end="...\t")

# ex 7
# theSum = 25
# for i in range(26, 33):
#     theSum += i
#     print("+", i, "-->", theSum)
# b
# initialLimit = int(input("Initial input: "))
# finalLimit = int(input("Final input: "))
# theSum = initialLimit
# if initialLimit > finalLimit:
#     print("The initial limit must be smaller than be final limit!")
# elif initialLimit == finalLimit:
#     print("Sum of numbers from", initialLimit, "till", finalLimit)
#     print(finalLimit)
# else:
#     for i in range(initialLimit, finalLimit+1):
#         theSum +=i
#         print("+", i, "-->", theSum)
# ex 8
# digit = int(input("What final digit do you want to check the numbers on"))
# count = 0
# for i in range(0, 10):
#     num = int(input("Enter a number"))
#     if num % 10 == digit:
#         count += 1
# print(count, "out of 10 numbers end on", digit)

# ex 9 a
# for i in range(10,21):
#     for j in range(i, -1, -1):
#         print(j, end=" ")
#     print()
# b
# for i in range(10,21,2):
#     for j in range(i, -1, -1):
#         print(j, end=" ")
#     print()

# ex 10
# for i in range(1,5):
#     print("Information for member", i)
#     name = input("Name: ")
#     age = int(input("Age: "))
#     nrOfYears = int(input("Nr of Years: "))
#     if nrOfYears >= 5:
#         discount = 0.9
#     else:
#         discount = 1
#     if age < 12:
#         print("Member fee for", name, "=", 20*discount)
#     elif 12 <= age < 18:
#         print("Member fee for", name, "=", 50*discount)
#     else:
#         print("Member fee for", name, "=", 95*discount)
#     print()

