from subprocess import check_output, call
from parser import Parser

class Monitor:
    upper_bound = 100
    lower_bound = 30

    @classmethod
    def check_battery(cls):
        result = check_output(["pmset", "-g", "batt"])
        return Parser(result, cls.upper_bound, cls.lower_bound)

    @staticmethod
    def notify(percent):
        message = "Battery Charge at {0}%".format(percent)
        osa_script_command = """
        tell application "System Events" to display notification "{0}"
        """
        call(["osascript", "-e", osa_script_command.format(message)])
