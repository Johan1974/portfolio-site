from question_model import Question
from data import question_data2
from quiz_brain import QuizBrain

question_bank = []

for question in question_data2["results"]:
    question_bank.append(Question(question["question"], question["correct_answer"]))


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the Quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
