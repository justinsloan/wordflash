import re

class PhonicsLexer(object):
    """Lexical Analyzer for parsing phonics and blend word combinations."""

    def __init__(self, source_words):
        """Takes a list as source_words"""
        self.source_words = source_words

    def tokenize(self):
        """Returns a dict with the phonics token and count."""

        source_index = 0
        tokens = {}
        source_words = self.source_words
        phonics = self._phonics_tokens()

        while source_index < len(source_words):
            word = source_words[source_index]

            for sound in phonics:
                # Check to see if the index (sound) is a regex
                if sound[0] == "[":
                    if re.search(r"" + sound, f"{word}."):
                        #print(f"{sound} MATCHED {word}")
                        if sound in tokens:
                            tokens[sound] += 1
                        else:
                            tokens[sound] = 1
                elif sound in word:
                    if sound in tokens:
                        tokens[sound] += 1
                    else:
                        tokens[sound] = 1
            source_index += 1

        return tokens

    def _phonics_tokens(self):
        """Returns a list of phonics sounds and regular expressions"""
        # '[aeiou][^vr]e(?=[^r])' matches 'Sneaky E' words
        tokens = ["are",
                  "au",
                  "ea",
                  "ee",
                  "igh",
                  "ny",
                  "ou",
                  "oo",
                  "ore",
                  "ure",
                  "[aeiou][^vr]e(?=[^r])"
                  ]
        return tokens