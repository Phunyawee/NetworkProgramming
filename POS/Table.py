from tkinter import *

tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('PythonExamples.org - Tkinter Example')

def toggleText(button):
    if(button['text']=='Submit'):
        button['text']='Submitted'
    else:
        button['text']='Submit'

button1 = Button(tkWindow,
                text = 'Submit',
                command = toggleText())
button1.pack()

tkWindow.mainloop()