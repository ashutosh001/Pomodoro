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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    count_down(5)
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

def count_down(count):
    if count>0:
        window.after(1000,count_down,count-1)
        canvas.itemconfig(canvas_text,text=f"{count}")

start_button = tkinter.Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

reset_button = tkinter.Button(text="Reset")
reset_button.grid(column=2,row=2)

tick_mark = tkinter.Label(text="✓",font=(FONT_NAME,20),fg=GREEN,bg=YELLOW)
tick_mark.grid(column=1,row=3)




window.mainloop()