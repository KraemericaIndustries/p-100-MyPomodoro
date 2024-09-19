from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_clicked():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    global rep
    rep = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_clicked():
    global rep
    rep += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if rep % 2 != 0:
        count_down(work_sec)
    elif rep / 2 == 4:
        count_down(long_break_sec)
    else:
        count_down(short_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif 10 > count_sec > 0:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        start_clicked()
        mark = ""
        for _ in range(math.floor(rep/2)):
            mark += "✔"
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Label
timer_label = Label(text="Timer", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_clicked)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_clicked)
reset_button.grid(column=2, row=2)

#Label
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()