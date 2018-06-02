from tkinter import *
from tkinter import filedialog


def askdirectory():
    dirname = filedialog.askdirectory()
    if dirname:
        var.set(dirname)

def askdirectory2():
    dirname = filedialog.askdirectory()
    if dirname:
        var2.set(dirname)


def UserFileInput(status, name):
    text = status
    var = StringVar(root)
    var.set(text)
    w = Entry(root, textvariable=var).grid(row=2, column=1, sticky=W)

    return w, var


def UserFileInput2(status, name):
    text = status
    var2 = StringVar(root)
    var2.set(text)
    w2 = Entry(root, textvariable=var2).grid(row=4, column=1, sticky=W)

    return w2, var2


def get_results():
    return (var.get(),var2.get(), c1.get(), c2.get(), c3.get())


root = Tk()

# Give your app a title
root.title("Medify")
Label(root, text="Musics directory").grid(row=1,column=1)
dirBut = Button(root, text="...", command=askdirectory)
dirBut.grid(row=2, column=2, sticky=W)
getBut = Button(root, text="start", command=get_results)
getBut.grid(row=8, column=1, sticky=E)
w, var = UserFileInput("", "Directory")
Label(root, text="Destination directory").grid(row=3,column=1)
dirBut2 = Button(root, text="...", command=askdirectory2)
dirBut2.grid(row=4, column=2, sticky=W)
w2, var2 = UserFileInput2("", "Directory")
c1, c2, c3 = BooleanVar(), BooleanVar(), BooleanVar()
Checkbutton(root, text="categorize", variable=c1).grid(row=5, column=1, sticky=W)
Checkbutton(root, text="correct metadata", variable=c2).grid(row=6, column=1, sticky=W)
Checkbutton(root, text="suggest", variable=c3).grid(row=7, column=1, sticky=W)

root.mainloop()
