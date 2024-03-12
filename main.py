import tkinter as tk
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("300x200")

        self.running = False
        self.start_time = None

        self.create_widgets()

    def create_widgets(self):
        self.time_label = tk.Label(self.root, text="00:00:00.000", font=("Helvetica", 24))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_stopwatch)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_stopwatch)
        self.reset_button.pack(side=tk.RIGHT, padx=10)

    def start_stopwatch(self):
        if not self.running:
            self.start_time = time.time() - (self.start_time or 0)
            self.running = True
            self.update()
            self.start_button["text"] = "Stop"
        else:
            self.running = False
            self.start_button["text"] = "Resume"

    def reset_stopwatch(self):
        self.running = False
        self.start_time = None
        self.start_button["text"] = "Start"
        self.update()

    def update(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            formatted_time = self.format_time(elapsed_time)
            self.time_label["text"] = formatted_time
            self.root.after(1, self.update)  # Update every 1 millisecond

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        milliseconds = int((seconds - int(seconds)) * 1000)
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}.{milliseconds:03d}"

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
