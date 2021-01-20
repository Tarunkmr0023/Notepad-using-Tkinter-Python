#!/usr/bin/env python
# coding: utf-8

# In[18]:


from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox


# In[19]:


class Pynote:
    def __init__(self,root):
        self.root = root
        
        def x_out():
            if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
                 root.destroy()
        # create menu bar ..
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save)
        filemenu.add_command(label="Save as...", command=self.save_as)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=x_out)
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=menubar)
 
        self.textarea = ScrolledText(self.root,font=('arial', 14),undo=True,wrap = WORD)
        self.textarea.place(relwidth=1, relheight=1)
 
 
    # methods ......
 
    def new_file(self, *args):
        self.textarea.delete(1.0, END)
        self.filename = None
 
    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"),
                       ("Text Files", "*.txt"),
                       ("Python Scripts", "*.py"),
                       ("Markdown Documents", "*.md"),
                       ("JavaScript Files", "*.js"),
                       ("HTML Documents", "*.html"),
                       ("CSS Documents", "*.css")])
        if self.filename:
            self.textarea.delete(1.0, END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
 
 
    def save(self, *args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0,END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
            except Exception as e:
                print(e)
        else:
            self.save_as()
 
    def save_as(self, *args):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"),
                           ("Text Files", "*.txt"),
                           ("Python Scripts", "*.py"),
                           ("Markdown Documents", "*.md"),
                           ("JavaScript Files", "*.js"),
                           ("HTML Documents", "*.html"),
                           ("CSS Documents", "*.css")])
            textarea_content = self.textarea.get(1.0,END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
        except Exception as e:
            print(e)
 
 
if __name__ == "__main__":
    root = Tk()
    root.title("Pynote")
    root.geometry('500x500')
    root.configure(bg='white')
    Pynote(root)
    root.mainloop()


# In[ ]:




