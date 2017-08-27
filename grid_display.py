from tkinter import *
from fonthub import Fonthub
import random

class GridDisplay:

    displaytext = []
    color = ['#ebedf0', '#c6e48b', '#7bc96f', '#239a3b', '#196127']
    frame = ''
    font = Fonthub()

    def __init__(self, frame):
        #frame.geometry("676x104")
        self.frame = frame
        self.createdisplay(self.displaytext)
        for i in range(53):
            for j in range(7):
                bg_color = self.color[0]
                l = Label(self.frame,
                          text=' ',
                          bg=bg_color)
                l.place(x=20 + i * 12, y=20 + j * 12, width=10, height=10)

    def createdisplay(self, stringtext=""):

        self.displaytext = self.font.string2fonthub(stringtext)
        week = 0
        j = 0
        for i, ni in enumerate(self.displaytext):
            if i % 7 == 0:
                week += 1
                j = 0
            if ni == 1:
                bg_color = self.color[random.randrange(1, 5)]
            else:
                bg_color = self.color[0]
            l = Label(self.frame,
                          text=' ',
                          bg=bg_color)
            l.place(x=20 + week * 12, y=20 + j * 12, width=10, height=10)
            j += 1


        '''
        for i in range(53):
            for j in range(7):
                bg_colour = self.color[0]
                l = Label(self.frame,
                          text=' ',
                          bg=bg_colour)
                l.place(x=20 + i * 12, y=20 + j * 12, width=10, height=10)
    '''

