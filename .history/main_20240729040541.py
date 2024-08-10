from tkinter import *

root = Tk()
root.geometry("1280x720")
root.title("PCS")

title1 = Label(root, text="Phillipine court case summarizer")
title1.grid(row=0, column=0)

summarizer_button = Button(root, text="Summarizer")
summarizer_button.grid(row=0, column=2)

statistic_button = Button(root, text="Statistic")
statistic_button.grid(row=0, column=4)

title2 = Label(root, text="Phillipine court case summarizer")
title2.grid(row=1, column=0)
court_case_list = Listbox(root)
court_case_list.insert(1, "case 1")
court_case_list.insert(2, "case 2")
court_case_list.insert(3, "case 3")
court_case_list.grid(row=2, column=0)

title3 = Label(root, text="Phillipine court case summarizer")
title3.grid(row=1, column=1)
summarized = Message(root, text="This is a case")
summarized.config(bg="red")
title3.grid(row=2, column=1)


root.mainloop()