import tkinter as tk

YELLOW = "#f7f5dd"
timer_on = False
reset = False

def reset_timer():
    global reset
    global timer_on
    canvas.itemconfig(clockface, text="00:00")
    timer_on = False
    reset = True

def start_timer():
    global timer_on
    if timer_on:
        return
    timer_on = True
    countdown(1500)

def start_break():
    global timer_on
    if timer_on:
        return
    timer_on = True
    countdown(300)

def countdown(count):
    global reset
    global timer_on
    if reset == True:
        reset = False
        return
    mins = str(count//60)
    secs = str(count % 60)
    if len(secs) < 2:
        secs = '0' + secs

    canvas.itemconfig(clockface, text=f"{mins}:{secs}")
    if count > 0:
        root.after(1000, countdown, count-1)
    else:
        timer_on = False

# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=YELLOW)


canvas = tk.Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
imgSrc = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=imgSrc)
clockface = canvas.create_text(103, 130, text="00:00", font=("helvetica", 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

label1 = tk.Label(text="Pomodoro Timer", font=("helvetica", 25, "bold"), bg=YELLOW)
label1.grid(column=1, row=0)

start_button = tk.Button(text="Start Timer", command=start_timer)
reset_button = tk.Button(text="Reset Timer", command=reset_timer)
break_button = tk.Button(text="Take a Break", command=start_break)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
break_button.grid(column=1, row=2)

root.mainloop()