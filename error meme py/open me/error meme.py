import tkinter as tk
import random
import subprocess
import winsound
import threading

# Play error sound
def play_sound():
    winsound.MessageBeep(winsound.MB_ICONHAND)

# Launch real apps
def launch_apps():
    apps = ["notepad.exe", "calc.exe", "mspaint.exe"]
    for app in apps:
        try:
            subprocess.Popen(app)
        except:
            pass

# Create error popups
def error_popup():
    for _ in range(10):
        win = tk.Toplevel()
        win.geometry(f"300x100+{random.randint(0, 1000)}+{random.randint(0, 700)}")
        win.title("Fatal Error")
        tk.Label(win, text="A virus has been detected!", fg="red", font=("Arial", 12)).pack()
        tk.Button(win, text="OK", command=win.destroy).pack()

# Flying shapes and text
def animate(canvas):
    colors = ["red", "blue", "green", "yellow", "purple"]
    for _ in range(50):
        x, y = random.randint(0, 800), random.randint(0, 600)
        text = canvas.create_text(x, y, text="ERROR!", fill=random.choice(colors), font=("Arial", 16))
        shape = canvas.create_oval(x, y, x+30, y+30, fill=random.choice(colors))
        move(canvas, text)
        move(canvas, shape)

def move(canvas, item):
    dx = random.choice([-3, -2, -1, 1, 2, 3])
    dy = random.choice([-3, -2, -1, 1, 2, 3])
    def step():
        canvas.move(item, dx, dy)
        canvas.after(50, step)
    step()

# Fake logout glitch
def fake_glitch():
    glitch = tk.Toplevel()
    glitch.attributes("-fullscreen", True)
    glitch.configure(bg="black")
    for _ in range(100):
        x, y = random.randint(0, 1920), random.randint(0, 1080)
        tk.Label(glitch, text="GL!TCH", fg=random.choice(["red", "green", "blue"]), bg="black", font=("Courier", 24)).place(x=x, y=y)
    glitch.after(3000, glitch.destroy)

# Main chaos window
def start_chaos():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    canvas = tk.Canvas(root, bg="black")
    canvas.pack(fill="both", expand=True)

    threading.Thread(target=play_sound).start()
    threading.Thread(target=launch_apps).start()
    threading.Thread(target=error_popup).start()
    animate(canvas)

    # Trigger fake glitch after 10 seconds
    root.after(10000, fake_glitch)

    root.mainloop()

start_chaos()