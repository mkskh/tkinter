import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self) -> None:
        
        self.root = tk.Tk()
        self.root.geometry('500x300')
        self.root.title('Program')

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Close without question', command=exit)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Close', command=self.on_closing)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label='Show message', command=self.show_message)

        self.menubar.add_cascade(menu=self.filemenu, label='File')
        self.menubar.add_cascade(menu=self.actionmenu, label='Action')

        self.root.config(menu=self.menubar)


        self.label = tk.Label(self.root, text='This is some cool text. \nAnd you can write something cool as well:', font=('Times New Roman', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=3, font=('Times New Roman', 16))
        self.textbox.bind('<KeyPress>', self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.checkbox = tk.Checkbutton(self.root, text='Show the text', font=('Times New Roman', 12), variable=self.check_state)
        self.checkbox.pack(padx=10, pady=10)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=0)
        self.buttonframe.columnconfigure(1, weight=0)

        self.button = tk.Button(self.buttonframe, text='Show', font=('Times New Roman', 18), command=self.show_message)
        self.button.grid(row=0, column=0, padx=15, pady=10)

        self.clear_button = tk.Button(self.buttonframe, text='Clear', font=('Times New Roman', 18), command=self.clear)
        self.clear_button.grid(row=0, column=1, padx=15, pady=10)

        self.buttonframe.pack()

        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get():
            if len(self.textbox.get('1.0', tk.END)) != 1:
                messagebox.showinfo(title='Your text', message=self.textbox.get('1.0', tk.END))
            else:
                messagebox.showinfo(title='Error', message="Please write something")
        else:
            messagebox.showinfo(title='Error', message="Choose 'Show the text'")
    
    def shortcut(self, event):
        if event.state == 20 and event.keysym == 'Return':
            self.show_message()
    
    def on_closing(self):
        if messagebox.askyesno(title='Quit?', message='Do you really want to quit?'):
            self.root.destroy()

    def clear(self):
        self.textbox.delete('1.0', tk.END)

MyGUI()