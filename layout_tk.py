import tkinter as tk

root = tk.Tk()

root.geometry('500x300')
root.title('My first tkinter program')

label = tk.Label(root, text='Here is a place for your text:', font=('Arial', 18))
label.pack(padx=19, pady=10)

textbox = tk.Text(root, height=3, font=('Arial', 18))
textbox.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text='Button 1', font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn2 = tk.Button(buttonframe, text='Button 2', font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonframe, text='Button 3', font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

# anotherbtn = tk.Button(root, text='Another btn', font=('Arial', 18))
# anotherbtn.place(x=100, y=100, height=100, width=150)


root.mainloop()