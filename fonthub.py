

class Fonthub:

    font = {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
        'E': [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 0, 1, 1],
            [1, 1, 0, 1, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 1]
        ],
        'F': [],
        'G': [],
        'H': [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1]

        ],
        'I': [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ],
        'J': [],
        'K': [],
        'L': [],
        'M': [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ],
        'N': [],
        'O': [],
        'P': [],
        'Q': [],
        'R': [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 0, 1, 1, 1]
        ],
        'S': [],
        'T': [],
        'U': [],
        'V': [],
        'W': [],
        'X': [],
        'Y': [],
        'Z': []
    }

    def __init__(self):
        self

    def returnfont(self, letter):
        return self.font[letter]

    def string2fonthub(self, string=""):
        displaytext = []
        for l in list(string):
            print(l.upper())
            if l.upper() in self.font:
                displaytext.append(self.font[l.upper()])
        return displaytext


