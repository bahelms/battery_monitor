import re

class Parser():
    regex = r"(\d{1,3})%; (.+);"

    def __init__(self, string, upper_bound, lower_bound):
        match = re.search(self.regex, string)
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.percent = int(match.group(1))
        self.battery_status = match.group(2)

    def has_crossed_threshold(self):
        return self.is_charging_at_upper_bound() or \
            self.is_discharging_at_lower_bound()

    def is_charging_at_upper_bound(self):
        return self.battery_status == "charging" and \
            self.percent == self.upper_bound

    def is_discharging_at_lower_bound(self):
        return self.battery_status == "discharging" and \
            self.percent <= self.lower_bound
