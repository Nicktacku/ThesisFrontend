from tkinter import *

root = Tk()
root.geometry("1280x720")
root.title("PCS")

title1 = Label(root, text="Phillipine court case summarizer")
title1.pack()

summarizer_button = Button(root, text="Summarizer")
summarizer_button.pack()

statistic_button = Button(root, text="Statistic")
statistic_button.pack()

root.mainloop()