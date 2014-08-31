from tkinter import *
import Hello

m = PanedWindow(orient=VERTICAL)
m.pack(fill=BOTH, expand=1)

top = Label(m, text="top pane")
editor = Hello.Editor(m)
m.add(top)

bottom = Label(m, text="bottom pane")
m.add(bottom)

mainloop()