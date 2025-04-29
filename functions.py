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
    canvas.create_line((last_x, last_y, event.x, event.y), fill=pen_color, width=2)
    last_x, last_y = event.x, event.y

def change_pen_color(color):
    global pen_color
    pen_color = color