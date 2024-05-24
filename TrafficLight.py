import tkinter as tk

class TrafficLightGUI:
    def __init__(self, frame):
        self.frame = frame
        self.remaining_time = 0

        self.canvas = tk.Canvas(frame, width=150, height=400, bg='white')
        self.canvas.pack()

        self.red_light = self.canvas.create_oval(50, 50, 100, 100, fill='red', outline='black')
        self.yellow_light = self.canvas.create_oval(50, 150, 100, 200, fill='gray', outline='black')
        self.green_light = self.canvas.create_oval(50, 250, 100, 300, fill='gray', outline='black')

        self.time_label = tk.Label(frame, text="", font=("Arial", 12))
        self.time_label.pack()

    def change_light(self, color):
        if color == 'Red':
            self.canvas.itemconfig(self.red_light, fill='red')
            self.canvas.itemconfig(self.yellow_light, fill='gray')
            self.canvas.itemconfig(self.green_light, fill='gray')
        elif color == 'Yellow':
            self.canvas.itemconfig(self.red_light, fill='gray')
            self.canvas.itemconfig(self.yellow_light, fill='yellow')
            self.canvas.itemconfig(self.green_light, fill='gray')
        elif color == 'Green':
            self.canvas.itemconfig(self.red_light, fill='gray')
            self.canvas.itemconfig(self.yellow_light, fill='gray')
            self.canvas.itemconfig(self.green_light, fill='green')
            # Start counting down the remaining green light time
            self.update_remaining_time(self.remaining_time)

    def update_remaining_time(self, remaining_time):
        if remaining_time >= 0:
            self.time_label.config(text="Timer: {}s".format(remaining_time//1000))
            self.remaining_time = remaining_time - 1000
            self.frame.after(1000, lambda: self.update_remaining_time(self.remaining_time))


    def run(self, gLTime):
        self.remaining_time = gLTime
        self.change_light('Yellow')
        self.frame.after(2000, lambda: self.change_light('Green'))
        self.frame.after(2000 + gLTime, lambda: self.change_light('Yellow'))
        self.frame.after(2000 + gLTime + 1000, lambda: self.change_light('Red'))
