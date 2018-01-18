# -*- coding:utf-8 -*-
# @Time   : 2018/1/18 22:27
from src.homework import CaptureSignal

cap = CaptureSignal()
if __name__ == '__main__':
    print(cap.get_signal_info("plane", 4))
