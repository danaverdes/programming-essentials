# ex 5.1
# original_list = ["birth", "teen", "adult", "elder", "gravestone"]
# first_element = original_list.pop(0)
# last_element = original_list.pop(-1)
#
# original_list.insert(0, last_element)
# original_list.append(first_element)
# print(original_list)

# EX 5.2
# original_list = [9, 17, 25, 4, 12, 7]
# new_list = []
# num = 0
# while num < len(original_list):
#     if original_list[num] % 2 != 0:
#         new_list.append(original_list[num])
#         original_list.pop(num)
#     else:
#         num += 1
# original_list += new_list
# print(original_list)

# ex 5.3
# og_list = ['cat', 'dog', 'mouse', 'rat', 'squirrel', 'owl', 'rabbit']
# slide_list = og_list[1:] + [og_list[0]]
# print(slide_list)

# ex 5.4
# og_tuple = (1, 2, 3, 4, 5, 6, 4, 7, 8)
# r_og_tuple = og_tuple[::-1]
# last_four = r_og_tuple.index(4)
# new_list = r_og_tuple[:last_four][::-1]
# print(new_list)

# ex 5.5
# first_list = [0, 42, 18, 17, 0, 2, 19, 10, 5, 14]
# index = 0
#
# while index < len(first_list):
#     if first_list[index] == 0:
#         odd = 0
#         r_index = index+1
#         while r_index < len(first_list):
#             if first_list[r_index] % 2 != 0:
#                 if first_list[r_index] > odd:
#                     odd = first_list[r_index]
#             r_index += 1
#
#         first_list[index] = odd
#     index += 1
# print(first_list)

# ex 5.6 a
# text = input("Enter a text: ").replace(" ", "")
# letter = ""
# list_chara = []
# for letter in text:
#     list_chara.append(letter)
# print(list_chara)
# print(*list_chara, sep=" ")
# print(*list_chara, sep="\t")
# b
# text = input("Enter a text: ").replace(" ", "")
# list_chara = []
# for letter in text:
#     if not letter in list_chara:
#         list_chara.append(letter)
# list_chara.sort()
# print(*list_chara, sep=" ")
# print(*list_chara, sep="\t")

# ex 5.7
# old_list = [2, 4, 5, 9]
# index = len(old_list)*2
# new_list = []
# for i in range(index):
#     new_list.append(0)
#
# new_list.append(old_list[-1])
# print(new_list)

# ex 5.8
# scores = float(input("Enter the test scores. Use -1 if you wanna finish: "))
# orders = [scores]
# while scores != -1:
#     scores = float(input("Enter the test scores. Use -1 if you wanna finish: "))
#     orders.append(scores)
# orders.sort()
# orders.pop(0) # because in this list we add -1 and sort, -1 will always be the smallest value when sorted thus we can just remove it
# print("The scores (ordered):", orders)
# print("The average of these", len(orders), "scores is", sum(orders)/len(orders))

# ex  5.9
# print("Enter your name and the distance to school.")
# print("Type stop when you want to close the entry")
# names = []
# distances = []
# name = ""
# while name != "stop":
#     name = input("Your name: ")
#     if name == "stop":
#         break
#     names.append(name)
#     distance = float(input("Enter your distance: "))
#     distances.append(distance)
# index = 0
# while index < len(names):
#     print(names[index], "\t", distances[index])
#     index += 1
# farthest = max(distances)
# farthest_index = distances.index(farthest)
# print(names[farthest_index], "lives the farthest, namely", farthest, "km")
# print("The average distance is", sum(distances) / len(distances))