def run():
  word = input("Enter a word: ").upper()
  #{new_key:new_value for (index, row) in df.iterrows()}
  student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
  for (key, value) in student_dict.items():
    #Access key and value
      pass

  import pandas
  student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
  for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
      pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
  data = pandas.read_csv("part11/nato_phonetic_alphabet.csv")
  #data = phonetic_alphabet.to_dict() #pandas.DataFrame(phonetic_alphabet)
  #print(type(alphabet_data_frame))
  
  alphabet_dict = {row.letter:row.code for (index, row) in data.iterrows()}
  #print(alphabet_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
  #print(alphabet_dict.items())
  #phonetic_code_words = {key:value for (key, value) in alphabet_dict.items() if key in list(word)}
  result = [alphabet_dict[letter] for letter in list(word)]
  print(result)
  #print(phonetic_code_words)