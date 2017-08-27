from tkinter import *
from fonthub import Fonthub
import random

class GridDisplay:

    color = ['#ebedf0', '#c6e48b', '#7bc96f', '#239a3b', '#196127']
    frame = ''
    font = Fonthub()

    def __init__(self, frame):
        self.frame = frame
        self.cleandisplay()

    def cleandisplay(self):
        for i in range(53):
            for j in range(7):
                bg_color = self.color[0]
                l = Label(self.frame,
                          text=' ',
                          bg=bg_color)
                l.place(x=20 + i * 12, y=20 + j * 12, width=10, height=10)

    def createdisplay(self, stringtext=""):
        self.cleandisplay()
        displaytext = self.font.string2fonthub(stringtext)
        week = 0
        j = 0
        for i, ni in enumerate(displaytext):
            if week >= 53:
                break
            if i % 7 == 0:
                week += 1
                j = 0
            if ni == 1:
                bg_color = self.color[random.randrange(1, 5)]
            else:
                bg_color = self.color[0]
            l = Label(self.frame, text=' ', bg=bg_color)
            l.place(x=20 + week * 12, y=20 + j * 12, width=10, height=10)
            j += 1


