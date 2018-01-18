# -*- coding:utf-8 -*-
# @Time   : 2018/1/18 22:42
import unittest
from src.homework import CaptureSignal


class TestHomework(unittest.TestCase):
    def test_case1(self):
        cap = CaptureSignal()
        self.assertEqual(cap.get_signal_info("plane", 2), "plane1 2 3 4 5")

    def test_case2(self):
        cap = CaptureSignal()
        self.assertEqual(cap.get_signal_info("plane", 4), "Error:4")

    def test_case3(self):
        cap = CaptureSignal()
        self.assertEqual(cap.get_signal_info("plane", 100), "cannot find 100")
