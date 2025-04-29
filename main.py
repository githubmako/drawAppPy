import tkinter as tk 
from tkinter import ttk 
from ctypes import windll
from tkinter.messagebox import showinfo



pen_color = "black"
last_x, last_y = None, None

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event, canvas):
    global last_x, last_y, pen_color
    if last_x is not None and last_y is not None:
        size = brush_size.get()
        canvas.create_line(last_x, last_y, event.x, event.y, width=size, fill=pen_color, capstyle=tk.ROUND, smooth=True)
    last_x, last_y = event.x, event.y

def change_pen_color(color):
    global pen_color
    pen_color = color

def use_eraser():
    change_pen_color("white")


root = tk.Tk()

root.title("Draw app")

message = tk.Label(root, text = "choose color and draw")
message.config(font=("Helvetica", 16))
message.pack()

windowHeight = 900
windowWidth = 1200

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

centerX = int(screenWidth/2 - windowWidth/2)
centerY = int(screenHeight/2 - windowHeight/2)

root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')

root.minsize(400,400)

root.attributes('-topmost',1)

exitButton = ttk.Button(
    root,
    text = "Exit", 
    command = lambda: root.quit()
)
exitButton.pack(
    ipadx = 5,
    ipady = 5,
    expand = False,
    side = 'bottom',
     anchor = 'center'
)


main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True)

canvas = tk.Canvas(main_frame, width=700, height=600, bg='white')
canvas.grid(row=0, column=0, sticky='nsew')

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", lambda event: draw(event, canvas))
button_frame = tk.Frame(main_frame)
button_frame.grid(row=0, column=1, sticky='ns', padx=10, pady=10)

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=0)
main_frame.rowconfigure(0, weight=1)

colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "gray", "black"]


buttons = []

for i, color in enumerate(colors):
    button = tk.Button(
        button_frame,
        text=f"Color {i+1}",
        bg=color,
        fg="white" if color in ["black", "blue", "purple", "brown"] else "black",
        command=lambda c=color: change_pen_color(c)
    )
    button.pack(ipadx=5, ipady=5, pady=2)
    buttons.append(button)

brush_size = tk.IntVar(value=2)
last_x, last_y = None, None

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event, canvas):
    global last_x, last_y, pen_color
    if last_x is not None and last_y is not None:
        size = brush_size.get()
        canvas.create_line(last_x, last_y, event.x, event.y, width=size, fill=pen_color, capstyle=tk.ROUND, smooth=True)
    last_x, last_y = event.x, event.y

size_label = tk.Label(button_frame, text="Brush size:")
size_label.pack(pady=5)

size_entry = tk.Entry(button_frame, textvariable=brush_size, width=5)
size_entry.pack(pady=5)

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()








