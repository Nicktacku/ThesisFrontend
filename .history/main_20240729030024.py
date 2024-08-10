from tkinter import *

root = Tk()
root.geometry("1280x720")
root.title("PCS")

title1 = Label(root, text="Phillipine court case summarizer")
title1.grid(row=0, col=0)

summarizer_button = Button(root, text="Summarizer")
summarizer_button.grid(row=0, col=1)

statistic_button = Button(root, text="Statistic")
statistic_button.grid(row=0, col=2)

root.mainloop()