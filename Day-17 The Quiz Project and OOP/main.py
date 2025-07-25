from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Part-02 Creating the list of question Objects from the Data
    # Write a for loop to iterate over the question_data.
    # Create a Question object from each entry in question_data.
    # Append each Question object to teh question_bank

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")