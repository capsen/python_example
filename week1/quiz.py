question1 = {
    "description" : "What's the answer of 1+3?",
    "options" : [1, 2, 3, 4],
    "correct_answer" : 4
}
question2 = {
    "description" : "What's the answer of 8*3?",
    "options" : [21, 24, 12, 3],
    "correct_answer" : 24
}

question3 = {
    "description" : "What's the third planet in the solar system?",
    "options" : ["Jupiter", "Mars", "Earth", "Saturn"],
    "correct_answer" : "Earth"
}

question4 = {
    "description" : "What are the factors for 12",
    "options" : [2,3,6,9],
    "correct_answer" : [2,6,3]
}

ques = [question1, question2, question3]

class Quiz():
    # def __init__(self, questions) :
    #     self.questions = questions

    def ask_question(self, question):
        print(question["description"])
        options = question["options"]
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer: "))
        while user_answer not in range(1, len(options) + 1):
            print(f"Invalid answer. Please enter a number between 1 and {len(options)}.")
            user_answer = int(input("Enter your answer: "))
        return options[user_answer - 1]

    def check_question(self, question, answer):
        if answer == question["correct_answer"]:
            return True
        else :
            return False
    
quiz = Quiz()

for q in ques:
    answer1 = quiz.ask_question(q)
    if quiz.check_question(q, answer1) : 
        print("You are correct")
    else:
        print (f"Incorrect answer: {answer1}")