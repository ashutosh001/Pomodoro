import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#5CB338"
YELLOW = "#EAD196"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    reps = 0
    canvas.itemconfig(canvas_text,text=f"00:00")
    window.after_cancel(timer)
    timer_text.config(text="Timer",fg=GREEN)
    tick_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps %8 == 0:
        count_down(60*LONG_BREAK_MIN)
        timer_text.config(text="Break",fg=GREEN)
    elif reps %2 == 0:
        count_down(60*SHORT_BREAK_MIN)
        timer_text.config(text="Break",fg=PINK)
    else:
        count_down(60*WORK_MIN)
        timer_text.config(text="Work",fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown_timer(time_in_seconds):
    minutes_left = int(time_in_seconds // 60)
    seconds_left = int(time_in_seconds % 60)
    if seconds_left < 10:
        seconds_left = "0"+str(seconds_left)
    return str(minutes_left) + ":" + str(seconds_left)

def count_down(count):
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
        canvas.itemconfig(canvas_text,text=f"{countdown_timer(count)}")
    else:
        start_timer()
        if reps%2 == 0:
            tick_mark.config(text="✓")
        else:
            tick_mark.config(text="")
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

timer_text = tkinter.Label(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
timer_text.grid(column=1,row=0)

canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="images/tomato.png")
canvas_image = canvas.create_image(100,112,image=tomato_image)
canvas_text = canvas.create_text(100,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button = tkinter.Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

reset_button = tkinter.Button(text="Reset",command=timer_reset)
reset_button.grid(column=2,row=2)

tick_mark = tkinter.Label(text="",fg=GREEN,bg=YELLOW)
tick_mark.grid(column=1,row=3)




window.mainloop()