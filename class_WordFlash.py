# !/usr/bin/env python3
#class_wordFlash.py
#This module is part of the "Word Flash" program

from tkinter import *
from tkinter import messagebox
import numpy
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plot

import os
import random
import time

from wordanalysis import *
from class_SettingsWindow import *
from class_SelectStudentWindow import *


class wordFlash():

    def __init__(self, master, settings, stats, log):
        """
        Reads initial settings and creates the user interface.
        """
        
        # Capture objects for use in the class
        self.settings = settings
        self.stats = stats
        self.log = log

        # Set the Default settings
        self.getDefaultSettings()
        
        # Instantiates the lastKey variable for use within the class
        self.lastKey = ""
        
        # Creates the GUI
        self.master = master
        self.master.title("Word Flash Dev.2")
        self.master.geometry("900x450")
        self._centerWindow()
        #self.master.attributes('-fullscreen',
        #                   True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
        #self.master.bind("<Escape>", self.master.destroy)
        self.master.bind("<Key>", self._onKey) # Binds the window to capture all keyboard input

        self.frameScoreBoard = Frame(self.master)
        # Place the following widgets in frameScore
        # -----------------------------------------------------------------------------------------
        self.lblIncorrect = Label(self.frameScoreBoard, text="Incorrect")
        self.lblIncorrect.grid(row=0, column=0, padx=10)
        self.lblCountIncorrectVar = StringVar()
        self.lblCountIncorrectVar = "00"
        self.lblCountIncorrect = Label(self.frameScoreBoard, text=self.lblCountIncorrectVar, fg="red")
        self.lblCountIncorrect.config(font=("Courier", 32))
        self.lblCountIncorrect.grid(row=1, column=0)
        # Spacers
        self.lblScoreLabelSpacer = Label(self.frameScoreBoard)
        self.lblScoreLabelSpacer.grid(row=0, column=1, ipadx=360)
        self.lblScoreCountSpacer = Label(self.frameScoreBoard)
        self.lblScoreCountSpacer.grid(row=1, column=1)
        # -------
        self.lblCorrect = Label(self.frameScoreBoard, text="Correct")
        self.lblCorrect.grid(row=0, column=2, padx=10)
        self.lblCountCorrectVar = StringVar()
        self.lblCountCorrectVar = "00"
        self.lblCountCorrect = Label(self.frameScoreBoard, text=self.lblCountCorrectVar, fg="green")
        self.lblCountCorrect.config(font=("Courier", 32))
        self.lblCountCorrect.grid(row=1, column=2)
        # -----------------------------------------------------------------------------------------
        if self.showScore:
            self.frameScoreBoard.grid(row=0, sticky=N+S+E+W, padx=10)
            #self.frameScoreBoard.pack(fill=BOTH,expand=1)  # Prepare and display frameScore

        self.frameDisplay = Frame(self.master)
        # Place the following widgets in frameDisplay
        # -----------------------------------------------------------------------------------------
        self.lblDisplay = Label(self.frameDisplay, text="Word Flash")
        self.lblDisplay.config(font=("Times New Roman", 88))
        self.lblDisplay.pack()
        # -----------------------------------------------------------------------------------------
        #self.frameDisplay.pack(fill=BOTH,expand=1)  # Prepare and display frameDisplay
        self.frameDisplay.grid(row=1, sticky=N+S+E+W, pady=75)
        #Test(self.frameDisplay)
        

        self.frameMessage = Frame(self.master)
        # Place the following widgets in frameControls
        # -----------------------------------------------------------------------------------------
        self.lblMessage = Label(self.frameMessage, text="Click New Session to start.")
        self.lblMessage.config(font=("Helvetica", 26))
        self.lblMessage.pack()
        # -----------------------------------------------------------------------------------------
        #self.frameMessage.pack(fill=X, expand=1) #Prepare and display frameMessage
        self.frameMessage.grid(row=2, sticky=E+W, pady=8)


        self.frameControls = Frame(self.master)
        # Place the following widgets in frameControls
        # -----------------------------------------------------------------------------------------
        self.btnNewSession = Button(self.frameControls, text="New Session", command=self._btnNewSession)
        self.btnNewSession.pack(side=LEFT)
        self.btnReview = Button(self.frameControls, text="Review", command=self._btnReview)
        self.btnReview.config(state=DISABLED)
        self.btnReview.pack(side=LEFT)
        self.btnStudentStats = Button(self.frameControls, text="Student Stats", command=self._btnStudentStats)
        self.btnStudentStats.pack(side=LEFT)
        self.btnSettings = Button(self.frameControls, text = "Settings" , command = self._btnSettings)
        self.btnSettings.pack(side=LEFT)
        self.btnQuit = Button(self.frameControls, text="Quit", command=self.closeWindow)
        self.btnQuit.pack(side=LEFT)
        # -----------------------------------------------------------------------------------------
        #self.frameControls.pack(fill=X) #Prepare and display frameControls
        self.frameControls.grid(row=3, pady=8)


        self.frameStatusBar = Frame(self.master)
        # Place the following widgets in frameStatusBar
        # ------------------------------------------------------------------------------------------
        self.lblStatus = Label(self.frameStatusBar, fg="grey", bd=1, relief=SUNKEN)
        self.lblStatus.pack(side=BOTTOM, fill=X)
        # ------------------------------------------------------------------------------------------
        self.frameStatusBar.grid(row=4, sticky=S+E+W)
        #self.frameStatusBar.pack(fill=X,expand=1, side=BOTTOM)
        
        self._createWordList()
        self.getCurrentStudent()
    
    
    def _centerWindow(self):
        """Centers the tk() window on the screen."""
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
    
    def _onKey(self, evnt):
        """Sets a class variable to capture keyboard input"""
        self.lastKey = evnt.keysym


    def _formatStudentName(self, format_name):
        """Returns the name in 'FirstL' format"""
        first_upper = format_name[0].upper()  # Get the first character as uppercase
        last_upper = format_name[-1].upper()  # Get the last character as uppercase
        middle_string = format_name[1:-1]  # Get everything between the first and last character
        the_student = first_upper + middle_string + last_upper  # Concat the strings
        return the_student
    
    
    def _btnNewSession(self):
        """Checks for changes to settings and then starts a new session"""
        self.getDefaultSettings() #Check for changes to the settings
        self.lblMessage.config(text="")
        wordList = self._createWordList(True) #Pause and show 'Ready!'
        self.log.info("New Session started.")
        self._startSession(wordList)
    
    
    def _btnReview(self):
        self.lblMessage.config(text="")
        wordList = self.MissedWords
        self._createWordList(True)  # Pause and show 'Ready!'
        self.lblStatus.config(text="Reading words from: Review List; " + str(len(wordList)) + " words total.")
        self.log.info("Review Session started.")
        self.log.info(self.lblStatus['text'])
        self._startSession(wordList)


    def _btnStudentStats(self):
        top = 12
        high = 0
        word_list = self.topMissedWords(top)
        syllables = 0
        split_counts = []
        split_words = []

        # Prepare data lists
        for eachWord in word_list:
            count, word = eachWord.split(":")
            count = int(count)
            split_counts.append(count)
            split_words.append(word)
            syllables += count_syllables(word)
            if count > high:
                high = count

        syllables = syllables / top # Calculate average syllables per word
        high += 1

        # Create the graph
        x = numpy.arange(top)
        plot.bar(x, split_counts)
        plot.xticks(x, split_words)
        #plot.figure(figsize=(6*3.13,4*3.13))
        plot.gcf().canvas.set_window_title("Student Stats")
        plot.title(f"Top {top} Missed Words")
        plot.xlabel(f"Words (Average Syllables: {syllables})")
        plot.ylabel("# Times Missed")
        plot.show()
        

    def _btnSettings(self):
        self.SettingsWindow = Toplevel(self.master)
        self.app = SettingsWindow(self.SettingsWindow, self.settings)


    def _infoBox(self, message, title="Word Flash"):
        messagebox.showinfo(title, message)


    def _createWordList(self, readyWait=False):
        """
        Creates the WordList by reading files with their setting set
        to True. Returns the WordList as a list for use in a Session.
        """
        listCount = 0
        wordList = []
        plural = "lists;"
        shuffleWords = ""
        if self.shuffleWords == True:
            shuffleWords = " (Shuffled)"
        
        for eachKey in self.settings["WordList"].keys():
            if self.settings.getboolean("WordList",eachKey) == True:
                wordFile = self.settings.get("WordFiles",f"{eachKey}File")
                fileDirectory = os.path.dirname(os.path.realpath(__file__))
                wordFilePath = f"{fileDirectory}/word_lists/{wordFile}"

                with open(wordFilePath) as f:
                    for line in f.readlines():
                        newWord = line.strip()
                        wordList.append(newWord)
                        syllables = count_syllables(newWord)
                        if syllables == 0:
                            self.log.debug(f"'{newWord}' has {syllables} syllables")
                        newWord = ""
                if self.shuffleWords == True:
                    random.shuffle(wordList)
                listCount = listCount + 1
        
        if listCount <= 1:
            plural = "list;"
        msgStatus = f"Reading from {str(listCount)} {plural} {str(len(wordList))} words total.{shuffleWords}"
        self.lblStatus.config(text=msgStatus)

        if readyWait:
            self._displayWord("Ready!")

        return wordList


    def _displayWord(self,theWord):
        """
        Displays the word provided and waits for the user to press
        either the LEFT or RIGHT arrow key before continuing.
        """
        self.lblDisplay.config(text=theWord)

        theKey = ""

        while theKey != "Left" and theKey != "Right": #Only respond to the LEFT and RIGHT keys
            theKey = self.lastKey
            self.master.update()
            time.sleep(.1)

        self.lastKey = ""
        return theKey #Return the key pressed


    def _checkKey(self, theKey):
        """
        Checks to see which key was pressed, Left or Right, and then
        either adds one point to the Correct score or one point to the
        incorrect score. The variable 'score' is used as the accumulator,
        but the number is stored as a string in the label.
        """
        score = 0
        if theKey == "Left":
            score = self.lblCountIncorrect['text']
            score = int(score) + 1
            score = str(score)
            self.lblCountIncorrect.config(text=score)
            self.MissedWords.append(self.lblDisplay['text']) #Add missed word to a list for later review
        elif theKey == "Right":
            score = self.lblCountCorrect['text']
            score = int(score) + 1
            score = str(score)
            self.lblCountCorrect.config(text=score)
                

    def _startSession(self, wordList):
        """
        Plays a Flash Word game by displaying each word in the WordList
        array. After all words have been displayed an average is
        calculated and shown to the user.
        """
        self.lastKey = ""
        
        self.MissedWords = []
        
        self.lblCountCorrect.config(text="00")
        self.lblCountIncorrect.config(text="00")
        
        wordCount = len(wordList)
        missString = ""

        for eachWord in wordList:
            wordCount = wordCount - 1
            if eachWord in self.stats["MissedWords"].keys():
                #Get the number of misses for display
                count = self.stats.get("MissedWords", eachWord)
                missString = f" Missed {count} times."
            msgString = f"{str(wordCount)} words remaining.{missString}"
            missString = "" #Reset the variable so it does not display on the next word.
            self.lblStatus.config(text=msgString)
            keyPress = self._displayWord(eachWord)
            self._checkKey(keyPress)

        self.lblDisplay.config(text="All done!")
        average = int(100 * (int(self.lblCountCorrect['text']) / int(len(wordList))))
        msgString = f"Average: {str(average)}%"
        self.lblMessage.config(text=msgString)
        self.log.info(msgString)

        if not self.MissedWords: #if MissedWords list is empty
            self.btnReview.config(state=DISABLED)
            self.lblStatus.config(text="No words missed.")
            self.log.info(self.lblStatus['text'])
        else:
            self._saveStats() #Add the missed words the the student's .ini
            self.btnReview.config(state=NORMAL)
            self.lblStatus.config(text=f"Missed {str(len(self.MissedWords))} words.")
            self.log.info(self.lblStatus['text'])


    def _saveStats(self):
        wordList = self.MissedWords

        for eachWord in wordList:
            if eachWord in self.stats["MissedWords"].keys():
                #Add 1 to the current count
                count = self.stats.getint("MissedWords", eachWord)
                count = count + 1
                self.stats.set("MissedWords", eachWord, str(count))
            else:
                #Add a new words with a count of 1
                self.stats.set("MissedWords", eachWord, "1")

        fileDirectory = os.path.dirname(os.path.realpath(__file__))
        theFile = self.getCurrentStudent() + ".ini"
        studentFilePath = f"{fileDirectory}/students/{theFile}"

        with open(studentFilePath, "w") as configfile:
            self.stats.write(configfile)


    def topMissedWords(self, max_count=5):
        """Returns a list with items 'Frequency:Word' from the student .ini
        file MissedWords section"""
        list = ['0:none']
        missed_words = self.stats["MissedWords"].keys()  # Retrieve the missed words list

        for eachWord in missed_words:
            list = sorted(list)
            value = int(self.stats.get("MissedWords", eachWord))
            low = int(list[0].split(":")[0])
            if value >= low:
                if len(list) == max_count:
                    del list[0]
                list.append(f"{str(value)}:{eachWord}")

        return list


    def getCurrentStudent(self):
        """Checks which student key in settings is set to True and
        returns the value as a string"""
        currentStudent = ""

        # Checks for which student key is set to True  in the settings
        for eachKey in self.settings["Student"].keys():
            if self.settings.getboolean("Student", eachKey):
                currentStudent = eachKey
                break

        self.log.info(f"Current student: {self._formatStudentName(currentStudent)}")
        return currentStudent


    def getDefaultSettings(self):
        """Set the Default Settings based on the .ini"""
        self.showStatusBar = self.settings.getboolean("Default","showStatusBar")
        self.showScore = self.settings.getboolean("Default","showScore")
        self.shuffleWords = self.settings.getboolean("Default","shuffleWords")


    def closeWindow(self):
        self.master.destroy()