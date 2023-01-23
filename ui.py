from tkinter import *
from quiz_brain import QuizBrain

BACKGROUND_COLOUR = "#145369"


class userInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("True or False Trivia")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOUR)
        self.canvas = Canvas(width=400, height=300)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=10, pady=10)
        self.score_label = Label(text='Score: 0', fg='white', bg=BACKGROUND_COLOUR, font=("Arial", 15, 'bold'))
        self.score_label.grid(column=1, row=0)
        self.question = self.canvas.create_text(200, 150, text="The Question will appear here",
                                                font=("Arial", 20, "normal"),
                                                width=380)
        correct_image = PhotoImage(file='Images/correct.png')
        self.correct_button = Button(image=correct_image, command=self.correct, highlightthickness=0, height=150, width=150)
        self.correct_button.grid(column=1, row=2)
        incorrect_image = PhotoImage(file='Images/incorrect.png')
        self.incorrect_button = Button(image=incorrect_image, command=self.incorrect, highlightthickness=0, height=150,
                                  width=150)
        self.incorrect_button.grid(column=0, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg='white')
        if self.quiz.question_number < 10:
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question, text= f"The Quiz is over, you scored {self.quiz.score}/10")
            self.correct_button.config(state='disabled')
            self.incorrect_button.config(state='disabled')

    def correct(self):
        is_right = self.quiz.check_answer('True')
        self.feedback(is_right)

    def incorrect(self):
        is_right = self.quiz.check_answer('False')
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')

        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
