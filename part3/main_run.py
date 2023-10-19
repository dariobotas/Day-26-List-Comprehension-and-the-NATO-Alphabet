def run():
  #exercise 1 - squared each number in the list bellow
  numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

  squared_numbers = [number * number for number in numbers]

  print(squared_numbers)