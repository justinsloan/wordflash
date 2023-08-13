# !/usr/bin/env python3
'''
This is a simple flash card program I wrote to help my
second-grade daughter study sight reading  and phonics
words. It allows for multiple users and keeps statistics
on frequently missed words, allowing for trends to be seen
over time.

What's the big idea?
If the words the student frequently misses use the same or
similar phonics sounds then you can more precisely remedy
reading and spelling difficulties.
'''
__version__ = "Dev.2"

# To_Do for my Branch (should be empty before every Push/Pull request)
# -----------------------------------------------------------------------

# -----------------------------------------------------------------------


import tkinter as tk
from tkinter import *
import time
import logging
from configparser import ConfigParser

from class_WordFlash import *
from class_SettingsWindow import *
from class_SelectStudentWindow import *


def loadSettings():
    """
    Loads all settings from the .ini file.
    Loads student info from the .ini file.
    """
    settings = ConfigParser()
    settings.read("word_flash.ini")

    stats = ConfigParser()

    # Checks for which student key is set to True  in the settings
    # .ini and reads the appropriate student .ini file.
    for eachKey in settings["Student"].keys():
        if settings.getboolean("Student", eachKey):
            fileDirectory = os.path.dirname(os.path.realpath(__file__))
            studentFilePath = f"{fileDirectory}/students/{str(eachKey)}.ini"
            stats.read(studentFilePath)
            break

    return settings, stats


def createLog():
    """
    Implements Python logging and returns the log object.
    """
    # Set the logging format as (s) strings
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

    # Create and configure the logger
    logging.basicConfig(filename = "log.txt",
                        level = logging.DEBUG,
                        format = LOG_FORMAT,
                        filemode = "w")
    logger = logging.getLogger()
    return logger


def countAll(settings):
    """
    Returns a word count and summary of all word lists
    available. This function has no effect on the program
    and is only used for analysis.
    """
    listCount = 0
    plural = "lists;"
    wordList = []

    for eachKey in settings["WordList"].keys():
        wordFile = settings.get("WordFiles", f"{eachKey}File")
        fileDirectory = os.path.dirname(os.path.realpath(__file__))
        wordFilePath = f"{fileDirectory}/word_lists/{wordFile}"

        with open(wordFilePath) as f:
            for line in f.readlines():
                newWord = line.strip()
                wordList.append(newWord)
                newWord = ""
        listCount = listCount + 1

    if listCount <= 1:
        plural = "list;"

    wordCount = len(wordList)
    summary = f"Reading from {str(listCount)} {plural} {str(wordCount)} words total."

    return wordCount, summary


# Prepare the Application objects
settings, stats = loadSettings()
log = createLog()

# Initiate the log file
a, b = countAll(settings)
log.info(b)               # Word List data summary

win.resizable(False, False) #makes window not resizeable

# Run the Application
root = Tk()
app = wordFlash(root, settings, stats, log)
root.mainloop()
