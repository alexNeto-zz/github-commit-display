from tkinter import *
from grid_display import GridDisplay


class createframe:

    def __init__(self, root):

        self.frame = Frame(root, width=768, height=576, bg="white", colormap="new")
        self.text = Label(self.frame, text="text", bg="white")
        self.entry = Entry(self.frame)
        self.go = Button(self.frame, text="generate", command=self.writedisplay)
        self.canvas = Canvas(self.frame, width=678, height=104, bg="white")

        self.frame.grid()
        self.text.grid(row=0, column=0, sticky=E)
        self.entry.grid(row=0, column=1, sticky=W)
        self.go.grid(row=0, column=3)
        self.canvas.grid(columnspan=4)

        self.grid = GridDisplay(self.canvas)

    def writedisplay(self):
        self.grid.createdisplay(self.entry.get())

root = Tk()
frame = createframe(root)
root.mainloop()
