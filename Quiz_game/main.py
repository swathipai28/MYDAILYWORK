print("******************************")
print("Welcome to my quiz game!")

question_bank = [
    {"text": "The ability of one class to acquire methods and attributes from another class is called ________.", "answer": "A"},
    {"text": "Which of the following is a type of inheritance?", "answer": "D"},
    {"text": "What type of inheritance has multiple subclasses to a single superclass?", "answer": "C"},
    {"text": "What is the depth of multilevel inheritance in Python?", "answer": "C"},
    {"text": "What does MRO stand for?", "answer": "B"}
]

options = [
    ["A.Inheritance", "B.Abstraction", "C.Polymorphism", "D.Objects"],
    ["A.Single", "B.Double", "C.Multiple", "D.Both A and C"],
    ["A.Multiple inheritance", "B.Multilevel inheritance", "C.Hierarchical inheritance", "D.None of these"],
    ["A.Two level", "B.Three level", "C.Any level", "D.None of these"],
    ["A.Method Recursive Object", "B.Method Resolution Order", "C.Main Resolution Order", "D.Method Resolution Object"]
]

def check_answer(user_guess, correct_answer):
    return user_guess == correct_answer

def play_quiz():
    score = 0
    for question_num in range(len(question_bank)):
        print("******************************")
        print(question_bank[question_num]["text"])
        for option in options[question_num]:
            print(option)

        guess = input("Enter your answer (A/B/C/D): ").upper()
        is_correct = check_answer(guess, question_bank[question_num]["answer"])
        if is_correct:
            print("Correct Answer")
            score += 1
        else:
            print("Incorrect Answer")
            print(f"The correct answer is {question_bank[question_num]['answer']}")
        print(f"Your current score is {score}/{question_num+1}")
    
    print(f"You have given {score} correct answers")
    print(f"Your score is {(score / len(question_bank)) * 100}%")

while True:
    play_quiz()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
