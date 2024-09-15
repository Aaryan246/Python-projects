from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import title_art

question_bank = []
for q in question_data:
    q_text = q['text']
    q_answer = q['answer']
    new_q = Question(q_text,q_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

print(title_art)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")