import tkinter as tk
from tkinter import messagebox
import time
import threading
from playsound import playsound

class BreakReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Break Reminder")
        self.root.geometry("400x300")
        
        self.label = tk.Label(root, text="Break Reminder", font=("Helvetica", 16))
        self.label.pack(pady=10)
        
        self.interval_label = tk.Label(root, text="Break Interval (minutes):")
        self.interval_label.pack()
        self.interval_entry = tk.Entry(root)
        self.interval_entry.pack()
        
        self.message_label = tk.Label(root, text="Break Message:")
        self.message_label.pack()
        self.message_entry = tk.Entry(root)
        self.message_entry.pack()
        
        self.sound_var = tk.BooleanVar()
        self.sound_check = tk.Checkbutton(root, text="Enable Sound", variable=self.sound_var)
        self.sound_check.pack()
        
        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(pady=10)
        
        self.running = False

    def start_timer(self):
        self.running = True
        self.timer_thread = threading.Thread(target=self.timer)
        self.timer_thread.start()

    def stop_timer(self):
        self.running = False

    def timer(self):
        try:
            interval = int(self.interval_entry.get()) * 60  # Convert minutes to seconds
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the interval.")
            return
        
        message = self.message_entry.get() or "Time to take a break!"
        
        while self.running:
            time.sleep(interval)
            if self.running:
                if self.sound_var.get():
                    playsound('alert.mp3')  # Play sound
                messagebox.showinfo("Break Reminder", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = BreakReminderApp(root)
    root.mainloop()