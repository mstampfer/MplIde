from tkinter import *
import code
import sys


class Interpreter(code.InteractiveInterpreter):
    def __init__(self, locals):
        code.InteractiveInterpreter.__init__(self, locals)

    def Runit(self, cmd):
        code.InteractiveInterpreter.runsource(self, cmd)


class Editor(Text):
    def __init__(self, parent):
        super().__init__(parent)
        # self.config(state=NORMAL)
        self.pack(fill=Y, expand=1)
        sys.stdout = self
        sys.stderr = self
        self.bind('<Key>', self.OnKeyPressed)
        self.cmd = ''

    def SetInterpreter(self, interpreter):
        self.interpreter = interpreter

    def write(self, ln):
        self.insert(END, '%s'%str(ln))

    def OnKeyPressed(self, event):
        self.changed = True
        char = event.keysym
        if char == 'Return':
            lnno = self.index('insert').split('.')[0]
            ln = self.get(float(lnno), END)
            self.cmd = self.cmd + ln
            self.write('\n')
            self.interpreter.Runit(self.cmd)
            self.cmd = ''
            pass

class Window(Frame):
    def __init__(self, master=None):
        super().__init__(master) # Creates self.master
        self.ed = Editor(self)


if __name__ == '__main__':
    Ecpint = Tk()
    I = Interpreter(None)
    win = Window()
    win.ed.SetInterpreter(I)
    win.master.title("Hello")
    win.pack()
    win.master.mainloop()

