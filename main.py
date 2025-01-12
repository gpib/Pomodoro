from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20



# ---------------------------- TIMER RESET ------------------------------- # 
def reset_pomodoro():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_pomodoro():
    count_down(5*60)

def exit_pomodoro():
    window.destroy()
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_secs = count % 60
    time_format = f"{count_min}:{count_secs:02d}"
    canvas.itemconfig(timer_count, text = time_format)
    if count > 0:
        window.after(1000, count_down, count -1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text = "Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW, highlightthickness=0)
title_label.grid(column=1, row=0)

button_start = Button(text = "Start", command = start_pomodoro)
button_start.grid(column = 0, row = 2)
button_start.config(padx = 5, pady = 5)

button_reset = Button(text = "Reset", command = reset_pomodoro)
button_reset.grid(column = 2, row = 2)
button_reset.config(padx = 5, pady = 5)

button_exit = Button(text = "Exit", command = exit_pomodoro)
button_exit.grid(column = 1, row = 4)
button_exit.config(padx = 5, pady = 5)

check_label = Label(text = "✔", fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW, highlightthickness=0)
check_label.grid(column=1, row=3)

canvas = Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img )
timer_count = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



window.mainloop()
