import unittest
from bm.monitor import Monitor

class MonitorTest(unittest.TestCase):
    def test_check_battery_returns_a_result(self):
        result = Monitor.check_battery()
        self.assertTrue(result.percent > 0)

if __name__ == "__main__":
    unittest.main()
