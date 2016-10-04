import logging
import re
from time import sleep
from subprocess import check_output, call

upper_bound = 100
lower_bound = 30

logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(message)s")
logging.info("Starting Battery Monitor")

def notify(num):
    osa_script_command = """
    tell application "System Events" to display notification
    "Battery Charge at {0}%"
    """
    call(["osascript", "-e", osa_script_command.format(num)])

while True:
    logging.info("Checking battery...")
    results = check_output(["pmset", "-g", "batt"])
    remaining_percent = int(re.search(r"(\d{1,3})%", results).group(1))
    if remaining_percent == upper_bound or remaining_percent <= lower_bound:
        notify(remaining_percent)
    sleep(150)
