class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]       
        current_answer = input(
                f'Q.{self.question_number+1}: '
                f'{current_question.text} (True / False)?'
                )
        self.question_number += 1
        self.check_answer(current_answer, current_question.answer)

    def check_answer(self, current_answer, correct_answer):
        if (current_answer.lower() == correct_answer.lower()):
            self.score += 1
            print('Correct answer!')
        else:
            print('Wrong answer!')
            print(f'The correct answer is {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_number} ')
        print('\n')
        
        

    