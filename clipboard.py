#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 28-01-2023 11:13 am
# @Author  : bhaskar.uprety
# @File    : clipboard.py

"""clipboard File created on 28-01-2023"""
from time import sleep, time

from pyperclip import paste


class Clipboard:
    """Implemented Clipboard class"""

    def __init__(self):
        self.data = ''
        self.file_name = ''
        self.limit = 200
        self.update_file_name()

    def update_file_name(self):
        """Implemented Clipboard.update_file"""
        self.file_name = str(time()).replace(".", "_") + ".txt"

    def update(self, data):
        """Implemented Clipboard update"""

    def monitor(self):
        """Monitor the clipboard"""
        while True:
            data = paste()
            if data != self.data:
                self.update(data)
            else:
                sleep(0.1)
