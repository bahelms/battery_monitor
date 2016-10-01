import logging
import re
from time import sleep
from subprocess import check_output
from pync import Notifier

logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(message)s")
logging.info("Starting Battery Monitor")

def notify(num):
    Notifier.notify("Battery life at {0}%".format(num))

while True:
    logging.info("Checking battery...")
    results = check_output(["pmset", "-g", "batt"])
    remaining_percent = int(re.search(r"(\d{1,3})%", results).group(1))
    if remaining_percent > 95 or remaining_percent <= 30:
        notify(remaining_percent)
    sleep(10)
