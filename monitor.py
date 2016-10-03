import logging
import re
from time import sleep
from subprocess import check_output, call
from pync import Notifier

logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(message)s")
logging.info("Starting Battery Monitor")

def notify(num):
    osa_script_command = """
    tell application "System Events" to display notification "Hey There"
    """
    call(["osascript", "-e", osa_script_command])
    # Notifier.notify("Battery life at {0}%".format(num))

while True:
    logging.info("Checking battery...")
    results = check_output(["pmset", "-g", "batt"])
    remaining_percent = int(re.search(r"(\d{1,3})%", results).group(1))
    if remaining_percent == 100 or remaining_percent <= 30:
        notify(remaining_percent)
    sleep(300)
