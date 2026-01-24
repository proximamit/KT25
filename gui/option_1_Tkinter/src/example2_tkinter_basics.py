import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter")

label = tk.Label(root, text="Hello World!")
label.pack()

button = tk.Button(root, text="Quit", command=root.destroy)
button.pack()

root.mainloop()
