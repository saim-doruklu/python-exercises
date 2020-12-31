class Clock:
    def __init__(self, hour, minute):
        self.hour, self.minute = self.convert_to_real_time(hour, minute)

    def __repr__(self):
        return f"{'0' if self.hour < 10 else ''}{self.hour}:{'0' if self.minute < 10 else ''}{self.minute}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)

    def convert_to_real_time(self, hour, minute):
        hours_in_minute_removed = minute % 60
        hours_in_minute = (minute - hours_in_minute_removed) // 60
        minute = hours_in_minute_removed
        hour += hours_in_minute
        hour %= 24
        return hour, minute
