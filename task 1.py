questions = ("Who developed python programming language? : ",
             "Which type of programming does python support? : ",
             "Which of the following is the correct extension of the python file? :",
             "Which keyword is used for function in python language? :",
             "Which of the following character is used to give single-line comments in python? :") 

options = (("A. Wick Van Rossum", "B. Rasmus Lerdorf", "C. Guido Van Rossum", "D. Niene Stom"),
            ("A. Object-oriented", "B. Structure", "C. functional", "D. All of the above"),
            ("A. .python", "B. .pi", "C. .py", "D. .p"),
            ("A. Function", "B. def", "C. Fun", "D. Define"),
            ("A. //", "B. #", "C. !", "D. /*"))              
               
answers = ("C", "D", "C", "B", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("**********************************")
    print(question)
    for option in options[question_num]:
        print(option)
 
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
       score += 1
       print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------------------")
print("      Result           ")
print("----------------------------------")

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
