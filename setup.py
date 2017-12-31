"""
Uses cx_Freeze to create an executable file.
"""

import sys
from cx_Freeze import setup, Executable

setup(
    name = "Word Flash",
    version = "Dev.2",
    description = "A simple phonics and sight reading flash card tool.",
    executables = [Executable("Main.py")])