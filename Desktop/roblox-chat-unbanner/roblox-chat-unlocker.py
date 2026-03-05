import tkinter as tk
from tkinter import ttk
import threading
import time

VALID_KEY = "ROBLOX-UNBAN-1233"

def start_process():
    username = username_entry.get()
    uid = uid_entry.get()
    key = key_entry.get()

    if username == "" or uid == "" or key == "":
        status_label.config(text="Please fill all fields!", fg="orange")
        return

    if key != VALID_KEY:
        status_label.config(text="Invalid key!", fg="red")
        return

    def run():
        progress["value"] = 0

        steps = [
            "Connecting to Roblox chat servers...",
            "Checking account UID...",
            "Unlocking chat permissions...",
            "Finalizing..."
        ]

        for step in steps:
            status_label.config(text=step)
            for i in range(25):
                progress["value"] += 1
                time.sleep(0.05)
                root.update_idletasks()

        status_label.config(text=f"Chat unlocked for {username}! ", fg="lightgreen")

    threading.Thread(target=run).start()


root = tk.Tk()
root.title("Roblox Chat Unlocker")
root.geometry("420x360")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="Roblox Chat Unlocker",
                 font=("Arial", 18, "bold"),
                 fg="white", bg="#1e1e1e")
title.pack(pady=15)

# Username
tk.Label(root, text="Username", fg="white", bg="#1e1e1e").pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# UID
tk.Label(root, text="UID", fg="white", bg="#1e1e1e").pack()
uid_entry = tk.Entry(root)
uid_entry.pack(pady=5)

# Key
tk.Label(root, text="Key", fg="white", bg="#1e1e1e").pack()
key_entry = tk.Entry(root)
key_entry.pack(pady=5)

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

start_button = tk.Button(root, text="Unlock Chat",
                         bg="#e2231a", fg="white",
                         command=start_process)
start_button.pack(pady=10)

status_label = tk.Label(root, text="Ready", fg="lightgreen", bg="#1e1e1e")
status_label.pack(pady=10)

root.mainloop()