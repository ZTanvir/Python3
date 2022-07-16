# start the clock from a given hour,min,second
class Clock:
    def __init__(self, hour: int, min: int, seconds: int):
        self.seconds = seconds
        self.min = min
        self.hour = hour

    # Add 1 second when tick method is called
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.min += 1
            self.seconds = 0
            if self.min == 60:
                self.hour += 1
                self.min = 0
                if self.hour == 24:
                    self.hour = 0

    # set method update hour,min,second 
    def set(self,hour,min):
        self.hour = hour
        self.min = min
        self.seconds = 0 

    def __str__(self) -> str:
        return f"{self.hour:02}:{self.min:02}:{self.seconds:02}"


if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)