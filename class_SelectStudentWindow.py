# !/usr/bin/env python3
#class_selectStudentWindow.py
#This module is part of the "Word Flash" program

from tkinter import *
from configparser import ConfigParser
import os


class SelectStudentWindow():
    """Provides GUI to select a student of create a new student file."""

    def __init__(self, master, settings):
        """Constructor for the class. Implements the GUI."""

        # Capture the settings for use in the class
        self.settings = settings

        self.master = master
        self.frame = Frame(master)
        self.master.title("Select Student")

        listbox = Listbox(self.master, selectmode=SINGLE)
        listbox.grid(row=0, columnspan=2, padx=4, pady=4)
        self.listbox = listbox

        entrybox = Entry(self.master)
        entrybox.grid(row=1, columnspan=2, padx=4, pady=4)
        self.entrybox = entrybox

        # Fill the Listbox with student names
        for eachStudent in self.settings['Student']:
            the_student = self._formatStudentName(eachStudent)
            self.listbox.insert(END, the_student)              # Add the new string to the Listbox

        # Highlight the current student
        current_student = self._getCurrentStudent()
        current_student = self._formatStudentName(current_student)
        index = self.listbox.get(0, END).index(current_student)
        self.listbox.activate(index)
        self.listbox.see(index) # Makes the highlighted item visible in a long list

        Button(self.master, text="New Student", command=self._btnNewStudent).grid(row=2, column=0, padx=8, pady=4)
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


    def _formatStudentName(self, format_name):
        """Returns the name in 'FirstL' format"""
        first_upper = format_name[0].upper()  # Get the first character as uppercase
        last_upper = format_name[-1].upper()  # Get the last character as uppercase
        middle_string = format_name[1:-1]  # Get everything between the first and last character
        the_student = first_upper + middle_string + last_upper  # Concat the strings
        return the_student


    def _getCurrentStudent(self):
        """
        Checks which student key in settings is set to True and returns
        the value as a string
        """
        currentStudent = ""

        # Checks for which student key is set to True  in the settings
        for eachKey in self.settings["Student"].keys():
            if self.settings.getboolean("Student", eachKey):
                currentStudent = eachKey
                break

        return currentStudent


    def _changeStudent(self):
        """
        Sets the current student to False and returns the new student as a string
        """
        # Set the current student to False
        current_student = self._getCurrentStudent()
        self.settings.set("Student", current_student, "False")

        new_student = self.listbox.get(ACTIVE).lower()  # Get the lowercase version of the Listbox selection text
        return new_student


    def _btnNewStudent(self):
        """
        Creates an .ini file for the new student, adds the name to the listbox,
        and sets them as active.
        """
        # Gets the text from the Entry widget
        new_student = self.entrybox.get()
        new_student = new_student.lower()

        # Determines the path for the new student .ini file
        fileDirectory = os.path.dirname(os.path.realpath(__file__))
        theFile = new_student + ".ini"
        studentFilePath = f"{fileDirectory}/students/{theFile}"

        # Creates the ConfigParser() object
        new_file = ConfigParser()
        new_file.add_section("MissedWords")

        # Writes the new .ini to the disk
        with open(studentFilePath, "w") as configfile:
            new_file.write(configfile)

        # Adds the new student to the listbox
        new_student = self._formatStudentName(new_student)
        self.listbox.insert(END, new_student)

        # Get the index for the new student and activate it for use in settings
        index = self.listbox.get(0, END).index(new_student)
        self.listbox.activate(index)
        self.listbox.see(index)


    def _btnOkay(self):
        the_student = self._changeStudent()
        self.settings.set("Student", the_student, "True")
        self.closeWindow()


    def closeWindow(self):
        self.master.destroy()