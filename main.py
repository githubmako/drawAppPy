import os
os.environ["PATH"] += os.pathsep + r"C:\Program Files\gs\gs10.00.0\bin"

import tkinter as tk 
from tkinter import ttk 
from tkinter import filedialog, messagebox
from PIL import Image

root = tk.Tk()

pen_color = "black"
last_x, last_y = None, None

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y


brush_style = tk.StringVar(value="solid")


def change_brush_style(style):
    brush_style.set(style)

def draw(event, canvas):
    global last_x, last_y, pen_color
    if last_x is not None and last_y is not None:
        size = brush_size.get()
        style = brush_style.get()
        if style == "solid":
            canvas.create_line(last_x, last_y, event.x, event.y, width=size, fill=pen_color, capstyle=tk.ROUND, smooth=True)
        elif style == "dotted":
            canvas.create_line(last_x, last_y, event.x, event.y, width=size, fill=pen_color, dash=(1, 5), capstyle=tk.ROUND, smooth=True)
        elif style == "dashed":
            canvas.create_line(last_x, last_y, event.x, event.y, width=size, fill=pen_color, dash=(5, 5), capstyle=tk.ROUND, smooth=True)
    last_x, last_y = event.x, event.y

def change_pen_color(color):
    global pen_color
    pen_color = color

def use_eraser():
    change_pen_color("white")



# test_of_connection

root.title("Draw app")

windowHeight = 900
windowWidth = 1200

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

centerX = int(screenWidth/2 - windowWidth/2)
centerY = int(screenHeight/2 - windowHeight/2)

root.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY}')

root.minsize(400,400)

root.attributes('-topmost',1)


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

colors = ["firebrick2", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "gray", "black"]


buttons = []


for i, color in enumerate(colors):
    button = tk.Button(
        button_frame,
        text=f"Color {i+1}",
        bg=color,
        fg="white" if color in ["black", "blue", "purple", "brown"] else "black",
        command=lambda c=color: change_pen_color(c),
        width=10,  
        height=2   
    )
    button.pack(ipadx=5, ipady=5, pady=2)
    buttons.append(button)


eraser_button = tk.Button(
    button_frame,
    text="Eraser",
    bg="white",
    fg="black",
    command=use_eraser,  
    width=10, 
    height=2   
)
eraser_button.pack(ipadx=5, ipady=5, pady=2)



brush_size = tk.IntVar(value=2)
last_x, last_y = None, None

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event, canvas):
    global last_x, last_y, pen_color
    if last_x is not None and last_y is not None:
        size = brush_size.get()
        style = brush_style.get()
        if style == "solid":
            canvas.create_line(last_x, last_y, event.x, event.y, width=size, fill=pen_color, capstyle=tk.ROUND, smooth=True)
        elif style == "dotted":
            canvas.create_line(last_x, last_y, event.x, event.y, width=size, fill=pen_color, dash=(1, 5), capstyle=tk.ROUND, smooth=True)
        elif style == "dashed":
            canvas.create_line(last_x, last_y, event.x, event.y, width=size, fill=pen_color, dash=(5, 5), capstyle=tk.ROUND, smooth=True)
    last_x, last_y = event.x, event.y

size_label = tk.Label(button_frame, text="Brush size:")
size_label.pack(pady=5)

size_entry = tk.Entry(button_frame, textvariable=brush_size, width=5)
size_entry.pack(pady=5)

style_button = tk.Menubutton(
    button_frame,
    text="Brush Style",
    bg="white",
    fg="black",
    width=10,
    height=2,
    relief=tk.RAISED
)
style_menu = tk.Menu(style_button, tearoff=0)
style_menu.add_command(label="Solid", command=lambda: change_brush_style("solid"))
style_menu.add_command(label="Dotted", command=lambda: change_brush_style("dotted"))
style_button.config(menu=style_menu)
style_button.pack(ipadx=5, ipady=5, pady=2)


menu_bar = tk.Menu(root)


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

options_menu = tk.Menu(menu_bar, tearoff=0)
options_menu.add_command(label="Settings")
options_menu.add_command(label="Help")
menu_bar.add_cascade(label="Options", menu=options_menu)


root.config(menu=menu_bar)

def save_canvas():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )
    if file_path:
        try:
            # Eksportowanie zawartości płótna do pliku PNG
            canvas.postscript(file="temp_canvas.ps", colormode='color')
            img = Image.open("temp_canvas.ps")
            img.save(file_path, "PNG")
            messagebox.showinfo("Save", f"File saved successfully as {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the file: {e}")

file_menu.delete(0, "end")  
file_menu.add_command(label="New")  
file_menu.add_command(label="Open")  
file_menu.add_command(label="Save", command=save_canvas)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()








