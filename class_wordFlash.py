# !/usr/bin/env python3
#class_wordFlash.py
#This module is part of the "Word Flash" program

from tkinter import *
from tkinter import messagebox
import os, random, time

from class_settingsWindow import *

class wordFlash():

    def __init__(self, master, settings):
        '''
        Reads initial settings and creates the user interface.
        '''
        
        #Capture the settings object for use in the class
        self.settings = settings
        self.getDefaultSettings()
        
        #Instantiates the lastKey variable for use within the class
        self.lastKey = ""
        
        #Creates the GUI
        self.master = master
        self.master.title("Word Flash Dev.2")
        self.master.geometry("900x450")
        self._centerWindow()
        self.master.bind("<Key>", self._onKey) #Binds the window to capture keyboard input

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
        #Spacers
        self.lblScoreLabelSpacer = Label(self.frameScoreBoard)
        self.lblScoreLabelSpacer.grid(row=0, column=1, ipadx=350)
        self.lblScoreCountSpacer = Label(self.frameScoreBoard)
        self.lblScoreCountSpacer.grid(row=1, column=1)
        #-------
        self.lblCorrect = Label(self.frameScoreBoard, text="Correct")
        self.lblCorrect.grid(row=0, column=2, padx=10)
        self.lblCountCorrectVar = StringVar()
        self.lblCountCorrectVar = "00"
        self.lblCountCorrect = Label(self.frameScoreBoard, text=self.lblCountCorrectVar, fg="green")
        self.lblCountCorrect.config(font=("Courier", 32))
        self.lblCountCorrect.grid(row=1, column=2)
        # -----------------------------------------------------------------------------------------
        #self.frameScoreBoard.pack(expand=TRUE, fill=X)  # Prepare and display frameScore
        if self.showScore:
            self.frameScoreBoard.grid(row=0, padx=10)


        self.frameDisplay = Frame(self.master, width=900)
        # Place the following widgets in frameDisplay
        # -----------------------------------------------------------------------------------------
        self.lblDisplay = Label(self.frameDisplay, text="Word Flash")
        self.lblDisplay.config(font=("Times New Roman", 88))
        self.lblDisplay.pack()
        # -----------------------------------------------------------------------------------------
        #self.frameDisplay.pack(expand=TRUE, fill=BOTH)  # Prepare and display frameDisplay
        self.frameDisplay.grid(row=1, pady=75)
        

        self.frameMessage = Frame(self.master, width=900)
        # Place the following widgets in frameControls
        # -----------------------------------------------------------------------------------------
        self.lblMessage = Label(self.frameMessage, text="Click New Session to start.")
        self.lblMessage.config(font=("Helvetica", 26))
        self.lblMessage.pack()
        # -----------------------------------------------------------------------------------------
        #self.frameMessage.pack(expand=TRUE, fill=X) #Prepare and display frameMessage
        self.frameMessage.grid(row=2)
        

        self.frameControls = Frame(self.master, width=900)
        #Place the following widgets in frameControls
        #-----------------------------------------------------------------------------------------
        self.btnNewSession = Button(self.frameControls, text="New Session", command=self._btnNewSession)
        self.btnNewSession.pack(side=LEFT)
        self.btnReview = Button(self.frameControls, text="Review", command=self._btnReview)
        self.btnReview.config(state=DISABLED)
        self.btnReview.pack(side=LEFT)
        self.btnSettings = Button(self.frameControls, text = "Settings" , command = self._btnSettings)
        self.btnSettings.pack(side=LEFT)
        self.btnQuit = Button(self.frameControls, text="Quit", command=self.closeWindow)
        self.btnQuit.pack(side=LEFT)
        # -----------------------------------------------------------------------------------------
        #self.frameControls.pack(expand=TRUE, side=BOTTOM) #Prepare and display frameControls
        self.frameControls.grid(row=3)
        
        
        self.frameStatusBar = Frame(self.master, width=900)
        #Place the following widgets in frameStatusBar
        #------------------------------------------------------------------------------------------
        self.lblStatus = Label(self.frameStatusBar, fg="grey", bd=1, relief=SUNKEN, anchor=W)
        self.lblStatus.pack(fill=X)
        #------------------------------------------------------------------------------------------
        self.frameStatusBar.grid(row=4, sticky=S)
        
        self._createWordList()
    
    
    def _centerWindow(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
    
    def _onKey(self, evnt):
        self.lastKey = evnt.keysym
    
    
    def _btnNewSession(self):
        self.getDefaultSettings()
        self.lblMessage.config(text="")
        wordList = self._createWordList()
        self._startSession(wordList)
    
    
    def _btnReview(self):
        self.lblMessage.config(text="")
        wordList = self.MissedWords
        self.lblStatus.config(text="Reading words from: Review List; " + str(len(wordList)) + " words total.")
        self._startSession(wordList)
        

    def _btnSettings(self):
        self.settingsWindow = Toplevel(self.master)
        self.app = settingsWindow(self.settingsWindow, self.settings)
                

    def _infoBox(self, message, title="Word Flash"):
        messagebox.showinfo(title, message)


    def _createWordList(self):
        '''
        Creates the WordList by reading files with their setting set
        to True. Returns the WordList as a list for use in a Session.
        '''
        listCount = 0
        wordList = []
        plural = " lists; "
        shuffleWords = ""
        if self.shuffleWords == True:
            shuffleWords = "(Shuffled)"
        
        for eachKey in self.settings["WordList"].keys():
            if self.settings.getboolean("WordList",eachKey) == True:
                wordFile = self.settings.get("WordFiles",eachKey + "File")
                fileDirectory = os.path.dirname(os.path.realpath(__file__))
                wordFilePath = fileDirectory + "/word_lists/" + wordFile

                with open(wordFilePath) as f:
                    for line in f.readlines():
                        newWord = line.strip()
                        wordList.append(newWord)
                        newWord = ""
                if self.shuffleWords == True:
                    random.shuffle(wordList)
                listCount = listCount + 1
        
        if listCount <= 1:
            plural = " list; "
        self.lblStatus.config(text="Reading from " + str(listCount) + plural + str(len(wordList)) + " words total. " + shuffleWords)
                
        return wordList


    def _displayWord(self,theWord):
        '''
        Displays the word provided and waits for the user to press
        either the LEFT or RIGHT arrow key before continuing.
        '''
        self.lblDisplay.config(text=theWord)

        theKey = ""

        while theKey != "Left" and theKey != "Right": #Only respond to the LEFT and RIGHT keys
            theKey = self.lastKey
            self.master.update()
            time.sleep(.1)

        self.lastKey = ""
        return theKey #Return the key pressed


    def _checkKey(self, theKey):
        '''
        Checks to see which key was pressed, Left or Right, and then
        either adds one point to the Correct score or one point to the
        incorrect score. The variable 'score' is used as the accumulator,
        but the number is stored as a string in the label.
        '''
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
        '''
        Plays a Flash Word game by displaying each word in the WordList
        array. After all words have been displayed an average is
        calculated and shown to the user.
        '''
        self.lastKey = ""
        
        self.MissedWords = []
        
        self.lblCountCorrect.config(text="00")
        self.lblCountIncorrect.config(text="00")
        
        wordCount = len(wordList)

        for eachWord in wordList:
            keyPress = self._displayWord(eachWord)
            self._checkKey(keyPress)
            wordCount = wordCount - 1
            msgString = str(wordCount) + " words remaining."
            self.lblStatus.config(text=msgString)

        self.lblDisplay.config(text="All done!")
        average = int(100 * (int(self.lblCountCorrect['text']) / int(len(wordList))))
        msgString = "Average: " + str(average) + "%"
        self.lblMessage.config(text=msgString)
        
        if not self.MissedWords: #if MissedWords list is empty
            self.btnReview.config(state=DISABLED)
        else:
            self.btnReview.config(state=NORMAL)


    def getDefaultSettings(self):
        #Get Default Settings
        self.showStatusBar = self.settings.getboolean("Default","showStatusBar")
        self.showScore = self.settings.getboolean("Default","showScore")
        self.shuffleWords = self.settings.getboolean("Default","shuffleWords")

    def closeWindow(self):
        self.master.destroy()