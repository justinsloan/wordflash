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

#Dev.2
#-----------------------------------------------------------------------
#TODO: Track frequency of missed words.
#TODO: Track frequency of missed words by list, i.e. student has a more
#      difficul time with the 'third grade' list or 'ai' phonics list.
#TODO: Adjust word list based on prior sessions; easier or harder words
#TODO: Keep track of multiple students.
#TODO: Load words from database instead of .txt files
#TODO: Save student info to .ini so it is transferable and transparent
#TODO: Implement 'Instant Feedback' feature
#TODO: Add phonics word lists
#-----------------------------------------------------------------------

#Bug Fixes
#-----------------------------------------------------------------------
#TODO: Status bar does not stretch across the entire window
#TODO: Settings do not affect status bar showing
#-----------------------------------------------------------------------


import tkinter as tk
from tkinter import *
import time
from configparser import ConfigParser

from class_wordFlash import *
from class_settingsWindow import *


def loadSettings():
    '''
    Loads all settings from the .ini file.
    '''
    settings = ConfigParser()
    settings.read("word_flash.ini")
    
    return settings

def countAll(settings):
    '''
    Returns a word count and summary of all word lists
    available. This function has no effect on the program.
    '''
    listCount = 0
    plural = " lists; "
    wordList = []
    
    for eachKey in settings["WordList"].keys():
        wordFile = settings.get("WordFiles",eachKey + "File")
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

#a, b = countAll(loadSettings())
#print(a)
#print(b)


#Run the Application
settings = loadSettings()
root = Tk()
app = wordFlash(root, settings)
root.mainloop()