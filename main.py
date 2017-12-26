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
__version__ = "DEV.2"

# Dev.2
# -----------------------------------------------------------------------
# TODO: Track frequency of missed words by list, i.e. student has a more
#      difficul time with the 'third grade' list or 'ai' phonics list.
# TODO: Show a Student Stats window
# TODO: Adjust word list based on prior sessions; easier or harder words
# TODO: Keep track of multiple students.
# TODO: Implement 'Instant Feedback' feature
# TODO: Implement the Select Student window
# TODO: If no student is set to True, open the Select Student window
# TODO: Error Detection for bad .ini entries like "Flase" instead of "False"
# -----------------------------------------------------------------------

# Bug Fixes
# -----------------------------------------------------------------------
# TODO: Status bar does not stretch across the entire window
# TODO: Settings do not affect status bar showing
# TODO: Buttons on the Main window should all be the same size
# -----------------------------------------------------------------------


import tkinter as tk
from tkinter import *
import time
import logging
from configparser import ConfigParser

from class_wordFlash import *
from class_settingsWindow import *


def loadSettings():
    """
    Loads all settings from the .ini file.
    Loads student in from the .ini file.
    """
    settings = ConfigParser()
    settings.read("word_flash.ini")

    stats = ConfigParser()

    # Checks for which student key is set to True  in the settings
    # .ini and reads the appropriate student .ini file.
    for eachKey in settings["Student"].keys():
        if settings.getboolean("Student", eachKey):
            fileDirectory = os.path.dirname(os.path.realpath(__file__))
            studentFilePath = fileDirectory + "/students/" + str(eachKey) + ".ini"
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
    plural = " lists; "
    wordList = []

    for eachKey in settings["WordList"].keys():
        wordFile = settings.get("WordFiles", eachKey + "File")
        fileDirectory = os.path.dirname(os.path.realpath(__file__))
        wordFilePath = fileDirectory + "/word_lists/" + wordFile

        with open(wordFilePath) as f:
            for line in f.readlines():
                newWord = line.strip()
                wordList.append(newWord)
                newWord = ""
        listCount = listCount + 1

    if listCount <= 1:
        plural = " list; "

    wordCount = len(wordList)
    summary = "Reading from " + str(listCount) + plural + str(wordCount) + " words total."

    return wordCount, summary


# Prepare the Application
settings, stats = loadSettings()
log = createLog()

# Initiate the log file
a, b = countAll(settings)
log.info(b)

# Run the Application
root = Tk()
app = wordFlash(root, settings, stats, log)
root.mainloop()
