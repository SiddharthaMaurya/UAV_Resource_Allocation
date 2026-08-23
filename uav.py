import csv
class UAV:


    def __init__(self,uav_id, x , y , battery , cpu):
        self.id = uav_id
        self.x = x
        self.y = y
        self.battery = battery
        self.cpu = cpu

    def display(self):
        print(f"UAV: {self.id}")
        print(f"position: ({self.x}, {self.y})")
        print(f"battery: {self.battery}%")
        print(f"cpu: {self.cpu} GHz ")


def save_uavs_to_csv(uavs):

        with open("data/uavs.csv", "w" , newline="") as file:

            writer = csv.writer(file)

            # Header 
            writer.writerow([
                "UAV_ID",
                "X",
                "Y",
                "Battery",
                "CPU"
            ])

            #Data

            for uav in uavs:

                writer.writerow([
                    uav.id,
                    uav.x,
                    uav.y,
                    uav.battery,
                    uav.cpu
                ])


             