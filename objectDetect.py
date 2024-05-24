from ultralytics import YOLO

class VehicleCounterYOLO:
    def __init__(self):
        self.model = YOLO('yolov8n.pt')

    def count_vehicles(self, image_paths):
        results = self.model(image_paths)
        vehicle_classes = ["car", "truck", "bus", "motorcycle"]
        self.vehicle_classes = vehicle_classes
        self.vehicle_counts = {cls: 0 for cls in vehicle_classes}
        
        for r in results:
            for clsid in r.boxes.cls:
                class_name = r.names[clsid.item()]
                if class_name in self.vehicle_counts:
                    self.vehicle_counts[class_name] += 1

        timings = { 'car' : 2 , 'bus' : 3 , 'truck' : 3 , 'motorcycle' : 1 }
        time = 0
        #print("Vehicle Counts:")
        for vehicle_class, count in self.vehicle_counts.items():
            time += timings[vehicle_class] * count
        if time < 10:
            time = 10
            #print(f"{vehicle_class}: {count}")
        #print(time)
        return time*1000

# Example usage:
# vehicle_counter = VehicleCounterYOLO()
# vehicle_counter.count_vehicles(['im2.jpg'])
