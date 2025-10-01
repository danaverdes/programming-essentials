# ex 7.1
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(num, "*", i, "=", num * i)

# ex 7.2
# num = int(input("Enter a number: "))
# i = 1
# while 0 < i < 11:
#     print(num, "*", i, "=", num * i)
#     i+=1

# ex 7.3
# num = int(input("Enter a number: "))
# smallest = num
# largest = num
# countOfDivisibleBy3 = 0
# for i in range(1,10):
#     num = int(input("Enter a number: "))
#     if num < smallest:
#         smallest = num
#     elif num > largest:
#         largest = num
#     if num % 3 == 0:
#         countOfDivisibleBy3 += 1
# print("The smallest number is:", smallest)
# print("The largest number is:", largest)
# print("The count of divisible by 3 is:", countOfDivisibleBy3)

# ex 7.4
# startBottle = 0
# endBottle = 99
# for i in range(startBottle,endBottle):
#     endBottle -=1
#     if endBottle == 2:
#         print(endBottle, "bottles of beer on the wall,", endBottle, "bottles of beer.")
#         print("Take one down, drink it up,", endBottle - 1, "bottle of beer on the wall.")
#     elif endBottle:
#         print(endBottle, "bottle of beer on the wall,", endBottle, "bottle of beer.")
#         print("Take one down, drink it up,", endBottle - 1, "bottles of beer on the wall.")
#     else:
#         print(endBottle, "bottles of beer on the wall,", endBottle, "bottles of beer.")
#         print("Take one down, drink it up,", endBottle - 1, "bottles of beer on the wall.")

# ex 7.5
# num1 = 1
# num2 = 1
# oldOne = 1
# print(num1)
# while num2 < 1000:
#     print(num2)
#     oldOne = num1
#     num1 = num2
#     num2 = oldOne + num1

# ex 7.6
word1 = input("Enter a word: ").lower()
word2 = input("Enter a word: ").lower()
