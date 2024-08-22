import tkinter as tk
from tkinter import messagebox
import random as r
class MemoryQuizGame:
    def __init__(self,root):
        self.root = root
        self.root.title("Memory Quiz Game")
        self.score=0
        self.questions= [
            {"Question": "How many planets are there?","Answer": "8"},
            {"Question": "What is the biggest star in the universe?","Answer": "Sun"},
            {"Question": "What is the capital of Canada?", "Answer": "Ottowa"},
            {"Question": "How many states are there in the USA?", "Answer" : "52"},
            {"Question": "In what galaxy is our solar system located in?", "Answer": "Milky Way"},
            {"Question": "What is the shortest month of the year?", "Answer": "February"},
            {"Question": "What language contains the most words?", "Answer": "English"},
            {"Question": "How many Continents are there?", "Answer": "7"},
            {"Question": "What is the tallest mountain on Earth?", "Answer": "Mount Everest"},
            {"Question": "What is the name of a shape with 6 sides?", "Answer": "Hexagon"},
            ]

        self.current_question= None
        self.create_widgets()
  
    def show_question(self):
        self.current_question = r.choice(self.questions)
        self.question_label.config(text=self.current_question["Question"])
        self.answer_entry.delete(0, tk.END)
    
    def check_answer(self):
        user_answer = self.answer_entry.get()
        correct_answer = self.current_question["Answer"]
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            messagebox.showinfo("Correct","Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"Sorry, the correct answer is {correct_answer}")
            
        self.score_label.config(text=f"Score: {self.score}")
        self.show_question()

    def create_widgets(self):
        menubar= tk.Menu(self.root)
        self.root.config(menu=menubar)

        filemenu= tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label= "Exit", command=self.root.quit)

        self.question_label = tk.Label(self.root, text="", font=("Times New Roman", 16))
        self.question_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
         
        self.answer_label = tk.Label(self.root, text="Your Answer:", font=("Times New Roman", 12))
        self.answer_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")

        self.answer_entry = tk.Entry(self.root, font=("Times New Roman", 12))
        self.answer_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        self.check_button = tk.Button(self.root, text="Check Answer", font=("Times New Roman", 12), command=self.check_answer)
        self.check_button.grid(row=2, column=0, columnspan=2, pady=20)

        self.score_label = tk.Label(self.root, text="Score: 0", font=("Times New Roman", 14, "bold"))
        self.score_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.show_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryQuizGame(root)
    root.mainloop()
