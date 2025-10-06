# # ex 4.1
# colour = input("What's your favourite colour: ")
# print(colour[0]+colour[2])
# print("This colour consist of", len(colour), "letters.")
# print()
# for i in range(len(colour)):
#     print(colour[i], "=", ord(colour[i]))
#
# for i in range(len(colour)):
#     if i % 2 == 0:
#         print("#" + str(colour[i]) + "#")
#     else:
#         print("**" + str(colour[i]) + "**")

# ex 4.2
# word = input("Enter a word: ")
# number = int(input("Enter a number: "))
# newWord = word[0] + word[-number:]
# print(newWord)

# ex 4.3
# word = input('Enter a word: ')
# start = len(word)
#
# if start < 3 or start % 2 == 0:
#     print("This word doesn't fulfill the requirements.")
# else:
#     num = int((start/2))
#     print(word[num-1]+word[num]+word[num+1])

# ex 4.4
# word = input('Enter a word: ').lower()
# if word == word[::-1]:
#     print(word[0].upper()+word[1:], "is a palindrome")
# else:
#     print(word[0].upper()+word[1:], "is not a palindrome")

# ex 4.5
# text = input("Enter any text: ")
# triple = 0
#
# for i in range(len(text)-2):
#     if text[i] == text[i+1] == text[i+2]:
#         triple += 1
# if triple == 1:
#     print("There is 1 triple in this text.")
# elif triple == 0:
#     print("There are no triples in this text.")
# else:
#     print(f"There are {triple} triples in this text.")


# ex 4.6
# word = input('Enter a word: ')
# num = len(word)
# newWord = ""
# for i in range(0,num,3):
#     group =word[i:i+3]
#     if len(group) == 3:
#         newWord += group[1:] + group[0]
#     else:
#         newWord += group
#
# print(newWord)

# ex 4.7
# text = input("Enter a text: ").lower()
# length = len(text)
# block = 0
# curr_block = 1
# for i in range(length):
#     if text[i] == text[i-1]:
#         curr_block +=1
#         block = max(curr_block, block)
#     else:
#         curr_block = 1
# block = max(curr_block, block)
# print("The length of the largest block in this text is", block)

# ex. 4.8
# word = input('Enter a word: ').lower()
# wordIn = "in"
#
# if wordIn in word:
#     if wordIn == word[0] + word[1] or wordIn == word[1] + word[2]:
#         print("\'in\' appears in the first or second place")
#     else:
#         print("\'in\' appears in the word, but not in the front")
# else:
#     print("this word does not contain \'in\'")

# ex 4.9
# lunch = input("What do you eat for lunch: ").lower()
# location = lunch.find("sandwich")
# lunch = lunch[location:]
# nospace = lunch.replace(" ", "")
# sandwichCount = nospace.count("sandwich")
# if sandwichCount >= 2:
#     topping = lunch.replace("sandwich", "")
#     print("You have", topping, "between your sandwich")
# else:
#     print()

# ex 4.10
# sentence = ""
# for i in range(1,6):
#     word = input("Enter word " + str(i) + ": ").capitalize()
#     sentence += " "+word
#
# sentence = " ".join(sentence.split(" ")[::-1])
# print(sentence)

# ex 4.12
# sentence = input("Enter a string: ")
# result = ""
# i = 0
# while i < len(sentence):
#     if sentence[i] == "*":
#         i +=2
#         if len(result) > 0:
#             result = result[:-1]
#     else:
#         result += sentence[i]
#         i +=1
# print(result)

# name = input("Enter your name: ")
# if name == "":
#     print("Please enter a name")
# else:
#     name = name
#
# print("Menu:")
# print("*****")
# print("U Uppercase")
# print("L Lowercase")
# print("A Alternate")
#
# choice = input("Make your choice (U-L-A): ").lower()
# while choice != "u" and choice != "l" and choice !="u":
#     choice = input("Make your choice (U-L-A): ").lower()
# altName = ""
# if choice == "u":
#     print(name.upper())
# elif choice == "l":
#     print(name.lower())
# else:
#     for i in range(len(name)):
#         if i % 2 == 0:
#             altName += name[i].lower()
#         else:
#             altName += name[i].upper()
#     print(altName)