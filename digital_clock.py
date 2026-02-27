import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x220")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (500 // 2)
y = (screen_height // 2) - (220 // 2)

root.geometry(f"500x220+{x}+{y}")

def start_move(event):
    root.x = event.x
    root.y = event.y

def do_move(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

root.bind("<Button-1>", start_move)
root.bind("<B1-Motion>", do_move)

root.bind("<Escape>", lambda e: root.destroy())

root.resizable(False,False)
root.eval('tk::PlaceWindow .  center')
root.configure(background="#000000")
root.overrideredirect(True)

def update_time():
    current_time = strftime("%H:%M:%S")
    current_date = strftime("%A %d %B %Y")
    clock_label.config(text=current_time)
    date_Label.config(text=current_date)
    clock_label.after(1000,update_time)

clock_label = tk.Label(
    root,
    font=("Consolas",64),
    background="#000000",
    foreground="#EAEAEA"
)
clock_label.pack(pady=(60,15))

date_Label = tk.Label(
    root,
    font=("Consolas",18),
    background="#000000",
    foreground="#888888"
)
date_Label.pack(pady=(0,40))



update_time()
root.mainloop()