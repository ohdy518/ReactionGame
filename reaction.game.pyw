import tkinter as tk
import random, time, sys, os
root = tk.Tk()
try: 
    root.iconbitmap("app.ico")
except:
    root.attributes("-toolwindow", True)
root.title("Reaction Game")
root.geometry("800x400")
root.resizable(False, False)
is_changed = False
changetime = 0
nowtime = 0
done = False
gamestart = False
def restart():
    root.destroy()
    root.mainloop()

def ready():
    global gamestart
    start_description.config(bg="red")
    root.configure(bg="red")
    root.update()
    root.after(1000, start_description.config(text="Reaction time: --.---s"))
    gamestart = True
def changebg(_=any):
    global is_changed, changetime
    root.configure(bg="green")
    start_description.config(bg="green")
    is_changed = True
    changetime = time.time()
def bindrtn(_=any):
    global is_changed, done, nowtime, changetime, gamestart
    if is_changed and not done:
        nowtime = time.time()
        root.configure(bg="white")
        start_description.config(text=f"Reaction time: {round((nowtime - changetime), 3)}s", bg="white")
        done = True
    if gamestart and not is_changed:
        root.configure(bg="yellow")
        start_description.config(text="[Enter] pressed before(after) screen change", bg="yellow")
        done = True
        root.update()
        

def start(_=any):
    global gamestart, done
    done = False
    start_description.config(text="Press [Enter] when screen changed")
    root.update()
    root.after(100, ready)
    root.update()
    root.after(random.randrange(1500, 4000), changebg)
start_description = tk.Label(text="Press [Space] to start", font=("Arial", 20))
start_description.pack()
start_description.place(x=20, y=20)
root.bind("<space>", start)
root.bind("<Return>", bindrtn)
root.mainloop()
