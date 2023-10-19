def run():
  #for loop
  numbers = [1, 2, 3]
  new_list = []
  
  for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
    
  print(new_list)

  #List Comprehension
  #new_list = [new_item for item in list]
  #to be like the for loop
  new_list1 = [n + 1 for n in numbers]
  print(new_list1)

  #List Comprehension with strings
  #challenge 1
  name = "Angela"
  new_list2 = [letter for letter in name]
  new_list3 = list(name)
  print(new_list2)
  print(new_list3)

  #Python sequences - list, tuples, strings, range
  #challenge 2 new list from 2 to 5 after list 1 to 4
  #range as list
  range_list = [num * 2 for num in range(1,5)]
  print(range_list)

  #Conditional List Comprehension
  #conditional list
  #new_list = [new_item for item in list if test]
  names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
  short_names = [name for name in names if len(name) <= 4]
  print(short_names)
  #challenge 3 - select names with more than 5 characters and upper case that names
  upper_case_names = [name.upper() for name in names if len(name) > 5]
  print(upper_case_names)
  