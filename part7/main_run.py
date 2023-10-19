""" Dictionary Comprehension """
import random


def run():
  #new_dict = {new_key:new_value for item in list}
  #new_dict = {new_key:new_value for (key, value) in dict.items()}
  #example 1
  names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
  students_scores = {student:random.randint(1,100) for student in names}
  print(students_scores)

  #example 2
  passed_students = {student:score for (student, score) in students_scores.items() 
                     if score >= 60}
  print(passed_students)