numbers_dictionary = {}

while True:
     number_as_string = input()

     if number_as_string == "Search":
          break

     try:
          number = int(input())
          numbers_dictionary[number_as_string] = number

     except ValueError:
          print("The variable number must be an integer")

while True:
     searched_num = input()

     if searched_num == "Remove":
          break

     try:
          print(numbers_dictionary[searched_num])

     except KeyError:
          print("Number does not exist in dictionary")

while True:
     number_for_del = input()

     if number_for_del == "End":
         print(numbers_dictionary)
         break

     try:
          del numbers_dictionary[number_for_del]

     except KeyError:
          print("Number does not exist in dictionary")


