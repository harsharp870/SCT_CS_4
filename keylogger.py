from pynput import keyboard
import tkinter as tk
from datetime import datetime

# Global variables
logging_status = False
log_data = ""

# Function to handle key press
def on_press(key):
    global log_data
    if logging_status:
        try:
            log_data += key.char
        except AttributeError:
            log_data += f" [{key}] "

        text_box.insert(tk.END, str(key) + " ")
        text_box.see(tk.END)

# Start logging
def start_logging():
    global logging_status
    logging_status = True
    status_label.config(text="Status: Logging Started", fg="green")

# Stop logging
def stop_logging():
    global logging_status
    logging_status = False
    status_label.config(text="Status: Logging Stopped", fg="red")

# Save logs to file
def save_logs():
    global log_data
    filename = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as file:
        file.write(log_data)
    status_label.config(text=f"Saved to {filename}", fg="blue")

# Clear logs
def clear_logs():
    global log_data
    log_data = ""
    text_box.delete("1.0", tk.END)

# GUI setup
root = tk.Tk()
root.title("Keyboard Activity Logger (Educational Use)")
root.geometry("500x400")
root.config(bg="#1e1e2f")

# Title
title = tk.Label(
    root,
    text="Keyboard Activity Logger",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=10)

# Text box
text_box = tk.Text(root, height=10, width=50)
text_box.pack(pady=10)

# Status label
status_label = tk.Label(
    root,
    text="Status: Idle",
    bg="#1e1e2f",
    fg="yellow"
)
status_label.pack()

# Buttons frame
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

tk.Button(frame, text="Start", command=start_logging, bg="green", fg="white", width=10).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Stop", command=stop_logging, bg="red", fg="white", width=10).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Save", command=save_logs, bg="blue", fg="white", width=10).grid(row=0, column=2, padx=5)
tk.Button(frame, text="Clear", command=clear_logs, bg="orange", fg="white", width=10).grid(row=0, column=3, padx=5)

# Start keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Run GUI
root.mainloop()
