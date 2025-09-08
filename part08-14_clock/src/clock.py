# Write your solution here:
class Clock:
    def __init__(self, hours: int = 0, mins: int = 0, secs: int = 0):
        self.hours = hours
        self.minutes = mins
        self.seconds = secs
    
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0
    
    def set(self, hours: int, mins: int):
        self.hours = hours
        self.minutes = mins
        self.seconds = 0

    def __str__(self):
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'
