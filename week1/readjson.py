import json

# open the JSON file
with open('week1/quiz_questions.json', 'r') as f:
    # load the data from the file
    quiz_data = json.load(f)

# print the loaded data
print(quiz_data)
