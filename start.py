import logging
from time import sleep
from bm.monitor import Monitor

logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(message)s")
logging.info("Starting Battery Monitor")

while True:
    logging.info("Checking battery...")
    result = Monitor.check_battery()

    if result.has_crossed_threshold():
        Monitor.notify(result.percent)
    sleep(Monitor.wait_period)
