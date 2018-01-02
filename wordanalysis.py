#!/usr/bin/env python3
# wordanalysis.py
# This module is part of the "Word Flash" program
"""
This module provides functions to analyze student progress and help determine
areas where the student in struggling.
"""

def countSyllables(word):
    """Returns the number of syllables in the word provided."""
    vowels = "aeiouy"
    count = 0
    last_was_vowel = False
    for letter in word:
        found_vowel = False
        for v in vowels:
            if v == letter:
                if not last_was_vowel: count += 1  # don't count diphthongs
                found_vowel = last_was_vowel = True
                break
        if not found_vowel:  # If full cycle and no vowel found, set last_was_vowel to false
            last_was_vowel = False


    if len(word) > 2 and word[-2:] == "es" and count > 1:  # Remove es - it's "usually" silent (?)
        count -= 1

    if len(word) > 4 and word[-1:] == "e":  # remove silent e
        count -= 1

    if len(word) > 1 and word[-2:] == "ee":  # adds 1 for na
        count += 1

    if len(word) > 1 and word[-2:] == "na":  # adds 1 for na
        count += 1

    # Check for special case words
    special_case = ['eloise','i']
    if word in special_case:
        count += 1

    return count