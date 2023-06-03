#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 28-01-2023
# @Time    : 11:11 am
# @Author  : bhaskar.uprety
# @File    : variables.py

"""variables.py File created on 28-01-2023"""

from time import time

# Path for project file
local_path = "/Documents/Python_Advance_Concept/Clipboard_History"
git_path = "https://github.com/JRudransh/Clipboard_History.git"

# Location variables
folder = "clipboard_data"
error_folder = ".error_log"
dynamic_filename = str(time()).replace(".", "") + ".txt"
limit = 100
