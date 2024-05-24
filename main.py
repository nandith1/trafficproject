from TrafficLight import TrafficLightGUI
from objectDetect import VehicleCounterYOLO
import tkinter as tk

class TrafficSimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Light Simulation")
        self.frames = []
        self.traffic_lights = []
        self.images = ['im1.jpg', 'im2.jpg', 'foggy.jpg', 'night.jpg']   ## list of images, eg. self.imgs = ["img1", "img2", "img3", "img4"] ##
        obj1 = VehicleCounterYOLO() 
        self.obj1 = obj1

        for i in range(4):
            self.frames.append(tk.Frame(root))
            self.frames[i].pack(side=tk.LEFT)
            traffic_light = TrafficLightGUI(self.frames[i])
            self.traffic_lights.append(traffic_light)

        self.run_button = tk.Button(root, text='Start', command=self.start_simulation)
        self.run_button.pack()

    def start_simulation(self):
        # Start updating the traffic lights recursively
        self.update_traffic_light(0)

    def update_traffic_light(self, index):
        if index < len(self.traffic_lights):
            gLTiming = self.obj1.count_vehicles(self.images[index])
            self.traffic_lights[index].run(gLTiming)
            # Schedule the update of the next traffic light after the current one has finished
            self.root.after(gLTiming + 3000, lambda: self.update_traffic_light(index + 1))

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficSimulationApp(root)
    root.mainloop()
