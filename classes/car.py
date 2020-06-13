"""
>>> car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
>>> car.start_engine()
>>> car.is_engine_started
True
>>> car.stop_engine()
>>> car.is_engine_started
False
"""


class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.current_speed=0
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


if __name__ == "__main__":
    import json
    detail = json.loads(input())

    color = detail["color"]
    max_speed = float(detail["max_speed"])
    acceleration = float(detail["acceleration"])
    tyre_friction = float(detail["tyre_friction"])

    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)

    car.start_engine()
    print(str(car.is_engine_started))
    car.stop_engine()
    print(str(car.is_engine_started))