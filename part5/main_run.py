def run():
  #exercise 3 - data overlap
  with open("part5/File1.txt") as file1:
    list1 = file1.readlines()

  with open("part5/File2.txt") as file2:
    list2 = file2.readlines()

  result = [int(num) for num in list1 if num in list2]

  print(result)