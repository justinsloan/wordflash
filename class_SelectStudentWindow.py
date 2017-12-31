# !/usr/bin/env python3
#class_selectStudentWindow.py
#This module is part of the "Word Flash" program

from tkinter import *


class SelectStudentWindow():
    """Provides GUI to select a student of create a new student file."""

    def __init__(self, master, settings):
        """Constructor for the class. Implements the GUI."""

        # Capture the settings for use in the class
        self.settings = settings

        self.master = master
        self.frame = Frame(master)
        self.master.title("Select Student")

        listbox = Listbox(self.master)
        listbox.grid(row=0, columnspan=2, padx=4, pady=4)

        listbox.insert(END, "a list entry")

        for item in ["one", "two", "three", "four"]:
            listbox.insert(END, item)

        Button(self.master, text="New Student", state=DISABLED).grid(row=1, column=0, padx=8, pady=4)
        Button(self.master, text="Okay", command=self._btnOkay).grid(row=1, column=1, padx=8, pady=4, sticky=E)
        self._centerWindow()


    def _centerWindow(self):
        """Centers the tk() window on the screen."""
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))


    def _btnOkay(self):
        self.closeWindow()


    def closeWindow(self):
        self.master.destroy()