from tkinter import *
import time
import random

window = Tk()
window.title("Typing Speed Test")
window.config(padx=30, pady=30)

sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing tests help improve your accuracy and speed.",
    "Practice makes perfect, so keep typing every day.",
    "Python is a powerful and beginner-friendly language.",
    "Never give up because great things take time.",
    "Consistency and dedication lead to mastery.",
    "Hard work beats talent when talent doesn’t work hard.",
    "Stay focused and never stop learning.",
    "Discipline is the bridge between goals and success.",
    "Small steps every day build up to big results."
]

start_time = 0
curr_text = ""

def start_test():
    global start_time, curr_text
    text.delete("1.0", END)
    rslt_txt.config(text="")

    curr_text = random.choice(sample_texts)
    label.config(text=curr_text)
    start_time = time.time()

def end_test():
    end_time = time.time()
    typed_text = text.get("1.0", END).strip()
    time_taken = end_time - start_time

    words = typed_text.split()
    wpm = round(len(words) / (time_taken / 60)) if time_taken > 0 else 0

    original = curr_text.split()
    correct = sum(1 for i in range(min(len(words), len(original))) if words[i] == original[i])
    accuracy = (correct / len(original)) * 100 if original else 0

    rslt_txt.config(text=f"WPM: {wpm} | Accuracy: {accuracy:.2f}%")

# UI Elements
label = Label(text="Click 'Start' to begin typing test", wraplength=400, font=("Arial", 14))
label.grid(row=0, column=0, columnspan=2, pady=10)

text = Text(height=5, width=40, font=("Arial", 14))
text.grid(row=1, column=0, columnspan=2)

rslt_txt = Label(text="", font=("Arial", 14))
rslt_txt.grid(row=3, column=0, columnspan=2, pady=10)

start_button = Button(text="Start", command=start_test)
start_button.grid(row=2, column=0, pady=20)

done_button = Button(text="Done", command=end_test)
done_button.grid(row=2, column=1, pady=20)


window.mainloop()