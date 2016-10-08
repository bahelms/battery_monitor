import unittest
from parser import Parser

class ParserTest(unittest.TestCase):
    def test_returns_true_if_has_crossed_upper_bound_threshold(self):
        parser = Parser("xxxx 99%; charging; xxxxh", 98, 30)
        self.assertTrue(parser.has_crossed_threshold())

    def test_returns_true_if_has_crossed_lower_bound_threshold(self):
        parser = Parser("xxxx 30%; discharging; xxxxh", 100, 30)
        self.assertTrue(parser.has_crossed_threshold())

    def test_returns_true_when_upper_bound_is_charged(self):
        parser = Parser("xxxx 100%; charged; xxxxh", 100, 30)
        self.assertTrue(parser.is_charging_at_upper_bound())

    def test_returns_false_when_upper_bound_is_discharging(self):
        parser = Parser("xxxx 100%; discharging; xxxxh", 100, 30)
        self.assertFalse(parser.is_discharging_at_lower_bound())

    def test_returns_false_when_lower_bound_is_charging(self):
        parser = Parser("xxxx 17%; charging; xxxxh", 57, 22)
        self.assertFalse(parser.is_charging_at_upper_bound())

    def test_is_battery_charging(self):
        parser = Parser("xxxx 17%; charging; xxxxh", 57, 22)
        self.assertTrue(parser.is_battery_charging())
        parser = Parser("xxxx 100%; charged; xxxxh", 57, 22)
        self.assertTrue(parser.is_battery_charging())
        parser = Parser("xxxx 100%; discharging; xxxxh", 57, 22)
        self.assertFalse(parser.is_battery_charging())

if __name__ == "__main__":
    unittest.main()
