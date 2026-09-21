from abc import ABC, abstractmethod

class Question(ABC):

    @abstractmethod
    def evaluate_answer(self):
        pass


class MCQQuestion(Question):
    def evaluate_answer(self):
        answer = "B"
        correct_answer = "B"

        if answer == correct_answer:
            print("MCQ: Correct Answer")
        else:
            print("MCQ: Wrong Answer")


class TrueFalseQuestion(Question):
    def evaluate_answer(self):
        answer = True
        correct_answer = True

        if answer == correct_answer:
            print("True/False: Correct Answer")
        else:
            print("True/False: Wrong Answer")


class DescriptiveQuestion(Question):
    def evaluate_answer(self):
        answer = "Python is a programming language."

        if len(answer) > 10:
            print("Descriptive: Answer Accepted")
        else:
            print("Descriptive: Answer Too Short")


q1 = MCQQuestion()
q1.evaluate_answer()

q2 = TrueFalseQuestion()
q2.evaluate_answer()

q3 = DescriptiveQuestion()
q3.evaluate_answer()