# !/usr/bin/env python3
#class_settingWindow.py
#This module is part of the "Word Flash" program

from tkinter import *
from class_SelectStudentWindow import *

class SettingsWindow():
    """Provides GUI to change Word Flash settings."""

    def __init__(self , master, settings):
        """Constructor for the class. Implements the GUI."""
        #Capture the settings for use
        self.settings = settings
        
        self.master = master
        self.frame = Frame(master)
        self.master.title("Settings")

        #grid.columnconfigure(grid, x, weight=1)
        #grid.columnconfigure(grid, y, weight=1)

        frameActiveWordLists = LabelFrame(self.master, text="Sight Words")
        frameActiveWordLists.grid(row=0, column=0, sticky=N+S+E+W, padx=8, ipadx=8, pady=8, ipady=8)

        self.checkPrimer = IntVar()
        self.checkPrimer.set(int(self.settings.getboolean("WordList","primerWordList")))
        Checkbutton(frameActiveWordLists, text="Primer (Pre-K & Kindergarten)", variable=self.checkPrimer, onvalue=1, offvalue=0).pack(anchor="w")

        self.checkFirstGrade = IntVar()
        self.checkFirstGrade.set(int(self.settings.getboolean("WordList","firstGradeWordList")))
        Checkbutton(frameActiveWordLists, text="First Grade", variable=self.checkFirstGrade, onvalue=1, offvalue=0).pack(anchor="w")

        self.checkSecondGrade = IntVar()
        self.checkSecondGrade.set(int(self.settings.getboolean("WordList","secondGradeWordList")))
        Checkbutton(frameActiveWordLists, text="Second Grade", variable=self.checkSecondGrade, onvalue=1, offvalue=0).pack(anchor="w")

        self.checkThirdGrade = IntVar()
        self.checkThirdGrade.set(int(self.settings.getboolean("WordList","thirdGradeWordList")))
        Checkbutton(frameActiveWordLists, text="Third Grade", variable=self.checkThirdGrade, onvalue=1, offvalue=0).pack(anchor="w")

        self.checkFryInstant = IntVar()
        self.checkFryInstant.set(int(self.settings.getboolean("WordList","fryInstantWordList")))
        Checkbutton(frameActiveWordLists, text="Dr. Fry Instant Words", variable=self.checkFryInstant, onvalue=1,
                    offvalue=0).pack(anchor="w")

        frameDisplayOptions = LabelFrame(self.master, text="Display Options")
        frameDisplayOptions.grid(row=0, column=1, sticky=N+S+E+W, padx=8, ipadx=8, pady=8, ipady=8)

        self.checkShowScore = IntVar()
        self.checkShowScore.set(int(self.settings.getboolean("Default","showScore")))
        Checkbutton(frameDisplayOptions, text="Show Score", variable=self.checkShowScore, onvalue=1, offvalue=0).pack(anchor="w")

        self.checkShowStatusBar = IntVar()
        self.checkShowStatusBar.set(int(self.settings.getboolean("Default","showStatusBar")))
        Checkbutton(frameDisplayOptions, text="Show Status Bar", variable=self.checkShowStatusBar, onvalue=1,
                    offvalue=0).pack(anchor="w")

        self.checkShuffleWords = IntVar()
        self.checkShuffleWords.set(int(self.settings.getboolean("Default","shuffleWords")))
        Checkbutton(frameDisplayOptions, text="Shuffle Words", variable=self.checkShuffleWords, onvalue=1, offvalue=0).pack(anchor="w")
        
        self.checkInstantFeedback = IntVar()
        self.checkInstantFeedback.set(int(self.settings.getboolean("Default","instantFeedback")))
        Checkbutton(frameDisplayOptions, state=DISABLED, text="Instant Feedback", variable=self.checkInstantFeedback, onvalue=1,
                    offvalue=0).pack(anchor="w")


        frameActivePhonicsLists = LabelFrame(self.master, text="Phonics")
        frameActivePhonicsLists.grid(row=1, column=0, columnspan=2, sticky=N+S+E+W,padx=8, ipadx=8, pady=8, ipady=4)
        
        self.checkPhonicsAIWordList = IntVar()
        self.checkPhonicsAIWordList.set(int(self.settings.getboolean("WordList","phonicsaiwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'ai' (said)", variable=self.checkPhonicsAIWordList, onvalue=1,
                    offvalue=0).grid(row=0, column=0, sticky=W)
        
        self.checkPhonicsAtoEWordList = IntVar()
        self.checkPhonicsAtoEWordList.set(int(self.settings.getboolean("WordList","phonicsa-ewordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'a-e' (late)", variable=self.checkPhonicsAtoEWordList, onvalue=1,
                    offvalue=0).grid(row=0, column=1, sticky=W)
        
        self.checkPhonicsALWordList = IntVar()
        self.checkPhonicsALWordList.set(int(self.settings.getboolean("WordList","phonicsalwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'al' (ball)", variable=self.checkPhonicsALWordList, onvalue=1,
                    offvalue=0).grid(row=0, column=2, sticky=W)
        
        self.checkPhonicsARWordList = IntVar()
        self.checkPhonicsARWordList.set(int(self.settings.getboolean("WordList","phonicsarwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'ar' (yard)", variable=self.checkPhonicsARWordList, onvalue=1,
                    offvalue=0).grid(row=1, column=0, sticky=W)
        
        self.checkPhonicsAUWordList = IntVar()
        self.checkPhonicsAUWordList.set(int(self.settings.getboolean("WordList","phonicsauwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'au' (haul)", variable=self.checkPhonicsAUWordList, onvalue=1,
                    offvalue=0).grid(row=1, column=1, sticky=W)
        
        self.checkPhonicsAYWordList = IntVar()
        self.checkPhonicsAYWordList.set(int(self.settings.getboolean("WordList","phonicsaywordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'ay' (day)", variable=self.checkPhonicsAYWordList, onvalue=1,
                    offvalue=0).grid(row=1, column=2, sticky=W)
        
        self.checkPhonicsCHWordList = IntVar()
        self.checkPhonicsCHWordList.set(int(self.settings.getboolean("WordList","phonicschwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'ch' (chess)", variable=self.checkPhonicsCHWordList, onvalue=1,
                    offvalue=0).grid(row=2, column=0, sticky=W)
        
        self.checkPhonicsEAWordList = IntVar()
        self.checkPhonicsEAWordList.set(int(self.settings.getboolean("WordList","phonicseawordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'ea' (teach)", variable=self.checkPhonicsEAWordList, onvalue=1,
                    offvalue=0).grid(row=2, column=1, sticky=W)
        
        self.checkPhonicsEEWordList = IntVar()
        self.checkPhonicsEEWordList.set(int(self.settings.getboolean("WordList","phonicseewordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'ee' (sleep)", variable=self.checkPhonicsEEWordList, onvalue=1,
                    offvalue=0).grid(row=2, column=2, sticky=W)
        
        self.checkPhonicsERWordList = IntVar()
        self.checkPhonicsERWordList.set(int(self.settings.getboolean("WordList","phonicserwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'er' (her)", variable=self.checkPhonicsERWordList, onvalue=1,
                    offvalue=0).grid(row=3, column=0, sticky=W)
        
        self.checkPhonicsItoEWordList = IntVar()
        self.checkPhonicsItoEWordList.set(int(self.settings.getboolean("WordList","phonicsi-ewordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'i-e' (hide)", variable=self.checkPhonicsItoEWordList, onvalue=1,
                    offvalue=0).grid(row=3, column=1, sticky=W)
        
        self.checkPhonicsIEWordList = IntVar()
        self.checkPhonicsIEWordList.set(int(self.settings.getboolean("WordList","phonicsiewordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'ie' (pie)", variable=self.checkPhonicsIEWordList, onvalue=1,
                    offvalue=0).grid(row=3, column=2, sticky=W)
        
        self.checkPhonicsIRWordList = IntVar()
        self.checkPhonicsIRWordList.set(int(self.settings.getboolean("WordList","phonicsirwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'ir' (girl)", variable=self.checkPhonicsIRWordList, onvalue=1,
                    offvalue=0).grid(row=4, column=0, sticky=W)
        
        self.checkPhonicsNGWordList = IntVar()
        self.checkPhonicsNGWordList.set(int(self.settings.getboolean("WordList","phonicsngwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'ng' (song)", variable=self.checkPhonicsNGWordList, onvalue=1,
                    offvalue=0).grid(row=4, column=1, sticky=W)
        
        self.checkPhonicsIGHWordList = IntVar()
        self.checkPhonicsIGHWordList.set(int(self.settings.getboolean("WordList","phonicsighwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'igh' (might)", variable=self.checkPhonicsIGHWordList, onvalue=1,
                    offvalue=0).grid(row=4, column=2, sticky=W)
        
        self.checkPhonicsOtoEWordList = IntVar()
        self.checkPhonicsOtoEWordList.set(int(self.settings.getboolean("WordList","phonicso-ewordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'o-e' (vote)", variable=self.checkPhonicsOtoEWordList, onvalue=1,
                    offvalue=0).grid(row=5, column=0, sticky=W)
        
        self.checkPhonicsOAWordList = IntVar()
        self.checkPhonicsOAWordList.set(int(self.settings.getboolean("WordList","phonicsoawordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'oa' (coat)", variable=self.checkPhonicsOAWordList, onvalue=1,
                    offvalue=0).grid(row=5, column=1, sticky=W)
        
        self.checkPhonicsNKWordList = IntVar()
        self.checkPhonicsNKWordList.set(int(self.settings.getboolean("WordList","phonicsnkwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'nk' (bank)", variable=self.checkPhonicsNKWordList, onvalue=1,
                    offvalue=0).grid(row=5, column=2, sticky=W)
        
        self.checkPhonicsOIWordList = IntVar()
        self.checkPhonicsOIWordList.set(int(self.settings.getboolean("WordList","phonicsoiwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'oi' (soil)", variable=self.checkPhonicsOIWordList, onvalue=1,
                    offvalue=0).grid(row=6, column=0, sticky=W)
        
        self.checkPhonicsShortOOWordList = IntVar()
        self.checkPhonicsShortOOWordList.set(int(self.settings.getboolean("WordList","phonicsshortoowordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics Short 'oo' (foot)", variable=self.checkPhonicsShortOOWordList, onvalue=1,
                    offvalue=0).grid(row=6, column=1, sticky=W)
        
        self.checkPhonicsLongOOWordList = IntVar()
        self.checkPhonicsLongOOWordList.set(int(self.settings.getboolean("WordList","phonicslongoowordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics Long 'oo' (boot)", variable=self.checkPhonicsLongOOWordList, onvalue=1,
                    offvalue=0).grid(row=6, column=2, sticky=W)
        
        self.checkPhonicsORWordList = IntVar()
        self.checkPhonicsORWordList.set(int(self.settings.getboolean("WordList","phonicsorwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'or' (horn)", variable=self.checkPhonicsORWordList, onvalue=1,
                    offvalue=0).grid(row=7, column=0, sticky=W)
        
        self.checkPhonicsOUWordList = IntVar()
        self.checkPhonicsOUWordList.set(int(self.settings.getboolean("WordList","phonicsouwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'ou' (loud)", variable=self.checkPhonicsOUWordList, onvalue=1,
                    offvalue=0).grid(row=7, column=1, sticky=W)
        
        self.checkPhonicsOWWordList = IntVar()
        self.checkPhonicsOWWordList.set(int(self.settings.getboolean("WordList","phonicsowwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'ow' (town)", variable=self.checkPhonicsOWWordList, onvalue=1,
                    offvalue=0).grid(row=7, column=2, sticky=W)
        
        self.checkPhonicsSHWordList = IntVar()
        self.checkPhonicsSHWordList.set(int(self.settings.getboolean("WordList","phonicsshwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'sh' (cash)", variable=self.checkPhonicsSHWordList, onvalue=1,
                    offvalue=0).grid(row=8, column=0, sticky=W)
        
        self.checkPhonicsQUWordList = IntVar()
        self.checkPhonicsQUWordList.set(int(self.settings.getboolean("WordList","phonicsquwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'qu' (quick)", variable=self.checkPhonicsQUWordList, onvalue=1,
                    offvalue=0).grid(row=8, column=1, sticky=W)
        
        self.checkPhonicsOYWordList = IntVar()
        self.checkPhonicsOYWordList.set(int(self.settings.getboolean("WordList","phonicsoywordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'oy' (enjoy)", variable=self.checkPhonicsOYWordList, onvalue=1,
                    offvalue=0).grid(row=8, column=2, sticky=W)
        
        self.checkPhonicsTHWordList = IntVar()
        self.checkPhonicsTHWordList.set(int(self.settings.getboolean("WordList","phonicsthwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'th' (this)", variable=self.checkPhonicsTHWordList, onvalue=1,
                    offvalue=0).grid(row=9, column=0, sticky=W)
        
        self.checkPhonicsWHWordList = IntVar()
        self.checkPhonicsWHWordList.set(int(self.settings.getboolean("WordList","phonicswhwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'wh' (when)", variable=self.checkPhonicsWHWordList, onvalue=1,
                    offvalue=0).grid(row=9, column=1, sticky=W)
        
        self.checkPhonicsURWordList = IntVar()
        self.checkPhonicsURWordList.set(int(self.settings.getboolean("WordList","phonicsurwordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'ur' (turn)", variable=self.checkPhonicsURWordList, onvalue=1,
                    offvalue=0).grid(row=9, column=2, sticky=W)
        
        self.checkPhonicsYWordList = IntVar()
        self.checkPhonicsYWordList.set(int(self.settings.getboolean("WordList","phonicsywordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'y' (cry)", variable=self.checkPhonicsYWordList, onvalue=1,
                    offvalue=0).grid(row=10, column=0, sticky=W)
        
        self.checkPhonicsUEUtoEWordList = IntVar()
        self.checkPhonicsUEUtoEWordList.set(int(self.settings.getboolean("WordList","phonicsueu-ewordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'ue', 'u-e (clue/fuse)", variable=self.checkPhonicsUEUtoEWordList, onvalue=1,
                    offvalue=0).grid(row=10, column=1, sticky=W)
        
        self.checkPhonicsEWUtoEWordList = IntVar()
        self.checkPhonicsEWUtoEWordList.set(int(self.settings.getboolean("WordList","phonicsewu-ewordlist")))
        Checkbutton(frameActivePhonicsLists, text="Phonics 'ew', 'u-e' (few/rude)", variable=self.checkPhonicsEWUtoEWordList, onvalue=1,
                    offvalue=0).grid(row=10, column=2, sticky=W)
        
        '''
        #Attempt to dynamically create Checkbuttons for each entry in WordList
        theList = self.settings["WordList"].keys()
        for eachKey in theList:
            if "phonics" in eachKey:
                Checkbutton(frameActivePhonicsLists,text=eachKey, onvalue=1,
                    offvalue=0).pack(anchor="w")
        '''
        Button(self.master, text="Change Student",  command=self._btnChangeStudent).grid(row=2, column=0, padx=8, pady=4, sticky=W)
        Button(self.master, text="Insight Report", state=DISABLED).grid(row=2, column=0, padx=8, pady=4)
        Button(self.master, text="Okay", command=self._btnOkay).grid(row=2, column=1, padx=8, pady=4, sticky=E)
        self._centerWindow()


    def _centerWindow(self):
        """Centers the tk() window on the screen."""
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        
        
    def saveSettings(self):
        """Captures all changes to settings and saves to the .ini file."""
        if self.checkPrimer.get():
            self.settings.set("WordList", "primerWordList", "True")
        else:
            self.settings.set("WordList", "primerWordList", "False")

        if self.checkFirstGrade.get():
            self.settings.set("WordList", "firstGradeWordList", "True")
        else:
            self.settings.set("WordList", "firstGradeWordList", "False")

        if self.checkSecondGrade.get():
            self.settings.set("WordList", "secondGradeWordList", "True")
        else:
            self.settings.set("WordList", "secondGradeWordList", "False")

        if self.checkThirdGrade.get():
            self.settings.set("WordList", "thirdGradeWordList", "True")
        else:
            self.settings.set("WordList", "thirdGradeWordList", "False")

        if self.checkFryInstant.get():
            self.settings.set("WordList", "fryInstantWordList", "True")
        else:
            self.settings.set("WordList", "fryInstantWordList", "False")

        if self.checkShuffleWords.get():
            self.settings.set("Default", "shuffleWords", "True")
        else:
            self.settings.set("Default", "shuffleWords", "False")

        if self.checkShowStatusBar.get():
            self.settings.set("Default", "showStatusBar", "True")
        else:
            self.settings.set("Default", "showStatusBar", "False")

        if self.checkShowScore.get():
            self.settings.set("Default", "showScore", "True")
        else:
            self.settings.set("Default", "showScore", "False")

        if self.checkInstantFeedback.get():
            self.settings.set("Default", "instantFeedback", "True")
        else:
            self.settings.set("Default", "instantFeedback", "False")
            
        if self.checkPhonicsAIWordList.get():
            self.settings.set("WordList", "PhonicsAIWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsAIWordList", "False")
            
        if self.checkPhonicsAtoEWordList.get():
            self.settings.set("WordList", "PhonicsA-EWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsA-EWordList", "False")
        
        if self.checkPhonicsALWordList.get():
            self.settings.set("WordList", "PhonicsALWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsALWordList", "False")
            
        if self.checkPhonicsARWordList.get():
            self.settings.set("WordList", "PhonicsARWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsARWordList", "False")
            
        if self.checkPhonicsAUWordList.get():
            self.settings.set("WordList", "PhonicsAUWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsAUWordList", "False")
        
        if self.checkPhonicsAYWordList.get():
            self.settings.set("WordList", "PhonicsAYWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsAYWordList", "False")
            
        if self.checkPhonicsCHWordList.get():
            self.settings.set("WordList", "PhonicsCHWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsCHWordList", "False")
            
        if self.checkPhonicsEAWordList.get():
            self.settings.set("WordList", "PhonicsEAWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsEAWordList", "False")
            
        if self.checkPhonicsEEWordList.get():
            self.settings.set("WordList", "PhonicsEEWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsEEWordList", "False")
            
        if self.checkPhonicsERWordList.get():
            self.settings.set("WordList", "PhonicsERWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsERWordList", "False")
            
        if self.checkPhonicsItoEWordList.get():
            self.settings.set("WordList", "PhonicsI-EWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsI-EWordList", "False")
            
        if self.checkPhonicsIEWordList.get():
            self.settings.set("WordList", "PhonicsIEWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsIEWordList", "False")
            
        if self.checkPhonicsIRWordList.get():
            self.settings.set("WordList", "PhonicsIRWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsIRWordList", "False")
            
        if self.checkPhonicsNGWordList.get():
            self.settings.set("WordList", "PhonicsNGWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsNGWordList", "False")
            
        if self.checkPhonicsIGHWordList.get():
            self.settings.set("WordList", "PhonicsIGHWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsIGHWordList", "False")
        
        if self.checkPhonicsOtoEWordList.get():
            self.settings.set("WordList", "PhonicsO-EWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsO-EWordList", "False")
            
        if self.checkPhonicsOAWordList.get():
            self.settings.set("WordList", "PhonicsOAWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsOAWordList", "False")
            
        if self.checkPhonicsNKWordList.get():
            self.settings.set("WordList", "PhonicsNKWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsNKWordList", "False")
            
        if self.checkPhonicsOIWordList.get():
            self.settings.set("WordList", "PhonicsOIWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsOIWordList", "False")
            
        if self.checkPhonicsShortOOWordList.get():
            self.settings.set("WordList", "PhonicsShortOOWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsShortOOWordList", "False")
            
        if self.checkPhonicsLongOOWordList.get():
            self.settings.set("WordList", "PhonicsLongOOWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsLongOOWordList", "False")
            
        if self.checkPhonicsORWordList.get():
            self.settings.set("WordList", "PhonicsORWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsORWordList", "False")
            
        if self.checkPhonicsOUWordList.get():
            self.settings.set("WordList", "PhonicsOUWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsOUWordList", "False")
            
        if self.checkPhonicsOWWordList.get():
            self.settings.set("WordList", "PhonicsOWWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsOWWordList", "False")
        
        if self.checkPhonicsSHWordList.get():
            self.settings.set("WordList", "PhonicsSHWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsSHWordList", "False")
            
        if self.checkPhonicsQUWordList.get():
            self.settings.set("WordList", "PhonicsQUWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsQUWordList", "False")
            
        if self.checkPhonicsOYWordList.get():
            self.settings.set("WordList", "PhonicsOYWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsOYWordList", "False")
            
        if self.checkPhonicsTHWordList.get():
            self.settings.set("WordList", "PhonicsTHWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsTHWordList", "False")
            
        if self.checkPhonicsWHWordList.get():
            self.settings.set("WordList", "PhonicsWHWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsWHWordList", "False")
            
        if self.checkPhonicsURWordList.get():
            self.settings.set("WordList", "PhonicsURWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsURWordList", "False")
            
        if self.checkPhonicsYWordList.get():
            self.settings.set("WordList", "PhonicsYWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsYWordList", "False")
            
        if self.checkPhonicsUEUtoEWordList.get():
            self.settings.set("WordList", "PhonicsUEU-EWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsUEU-EWordList", "False")
            
        if self.checkPhonicsEWUtoEWordList.get():
            self.settings.set("WordList", "PhonicsEWU-EWordList", "True")
        else:
            self.settings.set("WordList", "PhonicsEWU-EWordList", "False")

        
        # Save settings to .ini
        with open('word_flash.ini', 'w') as configfile:
            self.settings.write(configfile)


    def _btnOkay(self):
        self.saveSettings()
        self.closeWindow()


    def _btnChangeStudent(self):
        self.SelectStudentWindow = Toplevel(self.master)
        self.app = SelectStudentWindow(self.SelectStudentWindow, self.settings)
        

    def closeWindow(self):
        self.master.destroy()