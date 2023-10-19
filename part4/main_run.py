def run():
  #exercise 2 - filtering even numbers
  list_of_strings = input("Enter a serie of numbers divided by ',': ").split(',')
  #todo: use list comprehension to convert the strings to integer
  numbers = [int(number) for number in list_of_strings]
  #todo: use list comprehension to filter out the odd number and store the even numbers in a list called 'result'
  result = [number for number in numbers if number % 2 == 0]
  print(result)