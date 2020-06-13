"""
Case:1
>>> truck = Truck(color="Red", max_speed=250, acceleration=10, tyre_friction=3, max_cargo_weight=100)
>>> truck.load_cargo(50)
>>> truck.load_cargo(100)
Cannot load cargo more than max limit: 100

Case:2
>>> truck = Truck(color="Red", max_speed=250, acceleration=10, tyre_friction=3, max_cargo_weight=100)
>>> truck.start_engine()
>>> truck.load_cargo(50) # Prints
Cannot load cargo during motion

Case:3
>>> truck = Truck(color="Red", max_speed=250, acceleration=10, tyre_friction=3, max_cargo_weight=100)
>>> truck.load_cargo(50)
>>> truck.start_engine()
>>> truck.unload_cargo(50) # Prints
Cannot unload cargo during motion
"""


class Truck:
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.current_speed=0
        self.max_cargo_weight=max_cargo_weight
        self.load=0
        self.is_engine_started=False
    def start_engine(self):
        self.is_engine_started=True
    def stop_engine(self):
        self.is_engine_started=False
    def accelerate(self):
        if self.is_engine_started:
            self.current_speed+=self.acceleration
    def apply_brakes(self):
        if self.is_engine_started:
            if self.current_speed<tyre_friction:
                self.current_speed=0
            else:
                self.current_speed-=tyre_friction
    def sound_horn(self):
        if self.is_engine_started:
            print("Beep Beep")
        else:
            print("Car not started yet")
    def load_cargo(self,additional_load):
        if self.is_engine_started:
            print("Cannot load cargo during motion")
        else:
            if self.load+additional_load>max_cargo_weight:
                print("Cannot load cargo more than max limit: {}".format(self.max_cargo_weight))
            else:
                self.load+=additional_load
    def unload_cargo(self,load_removed):
        if self.is_engine_started:
            print("Cannot unload cargo during motion")
        else:
            if self.load<load_removed:
                self.load=0
            else:
                self.load-=load_removed


if __name__ == "__main__":
    import json
    detail = json.loads(input())

    color = detail["color"]
    max_speed = float(detail["max_speed"])
    acceleration = float(detail["acceleration"])
    tyre_friction = float(detail["tyre_friction"])
    max_cargo_weight = float(detail["max_cargo_weight"])
    load_1, load_2, load_3 = [float(each) for each in detail["loads"]]

    truck = Truck(color=color, max_speed=max_speed, acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    truck.load_cargo(load_1)
    print(truck.load)
    truck.start_engine()
    truck.load_cargo(load_2)

    truck.unload_cargo(load_3)
