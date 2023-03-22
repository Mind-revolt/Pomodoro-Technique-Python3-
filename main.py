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
reps = 0
# create a global variable for timer
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer
    global label_1
    global marks
    global reps
    window.after_cancel(timer)
    # reset numbers
    canvas.itemconfig(count_down_text, text='00:00', font=(FONT_NAME, 30, 'bold'))
    #reset sign
    label_1.config(text='Timer', font=(FONT_NAME, 40, 'normal'))
    #reset checkmark
    check_marks_label.config(text='', bg=YELLOW, highlightthickness=0)
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_seconds)
        label_1.config(text='Break', fg=RED, font=(FONT_NAME, 40, 'normal'))
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        label_1.config(text='Break', fg=PINK, font=(FONT_NAME, 40, 'normal'))
    else:
        count_down(work_seconds)
        label_1.config(text='Work', fg=GREEN, font=(FONT_NAME, 40, 'normal'))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(count_down_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_session = math.floor(reps/2)
        for rep in range(work_session):
            marks += '✔️'

        check_marks_label.config(text=marks)
        # if reps % 2 == 0:
        #     check_mark_label = Label(text='✔️', fg=GREEN, bg='white')
        #     check_mark_label.grid(column=1, row=3)
        # else:
        #     check_mark_label = Label(text='', fg=GREEN, bg=YELLOW)
        #     check_mark_label.grid(column=1, row=3)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
# set up a canvas

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
label_1 = Label(text='Timer', font=(FONT_NAME, 40, 'normal'), bg=YELLOW, fg=GREEN, highlightthickness=0)
label_1.grid(column=1, row=0)
# to read a particular image file that's not gif us PhotoImage

tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
count_down_text = canvas.create_text(101, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# create Buttons
start_button = Button()

start_button.config(text='Start', command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button()
reset_button.config(text='Reset', command=reset)
reset_button.grid(column=2, row=2)

# create checkmark
check_marks_label = Label(text='', bg=YELLOW, highlightthickness=0)
check_marks_label.grid(column=1, row=2)



# create continue button
# continue_button = Button(text='Continue', command=continue_clock)
# continue_button.grid(column=0, row=4)







window.mainloop()
