import tkinter as tk

root = tk.Tk()
root.title("My App")
root.geometry("400x300")
root.minsize(width=400, height=300)

count = 0

label = tk.Label(root, text=f'Button was clicked {count} times')
label.config(font=("Aptos", 16, 'bold'),)
label.pack()
# Layout Managers

def foo():
    global count
    print("Button was clicked")
    count += 1
    label.config(text=f"Button was clicked {count} times")

btn = tk.Button(text='Click', bg="deep sky blue", fg="white", command=foo)
btn.pack()

root.mainloop()