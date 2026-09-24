import tkinter as tk
from tkinter import filedialog, messagebox


def new_file():
    txt.delete("1.0", tk.END)
    root.title("Untitled - PieNote")


def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
        

        txt.delete("1.0", tk.END)
        txt.insert("1.0", content)
        

        root.title(f"{file_path} - PieNote")


def save_file_as():

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )


    if file_path:

        file_content = txt.get("1.0", tk.END)
        

        with open(file_path, "w") as file:
            file.write(file_content)
            

        root.title(f"{file_path} - PieNote")
        messagebox.showinfo("Saved", "File saved successfully!")


def open_about():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    window_width = 250
    window_height = 150
    

    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    

    center_x = int(root_x + (root_width / 2) - (window_width / 2))
    center_y = int(root_y + (root_height / 2) - (window_height / 2))
    

    about_window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    
    

    about_window.transient(root)
    about_window.grab_set()
    
    label = tk.Label(about_window, text="PieNote\nVersion 1.0\nBuilt By kotten.", pady=20)
    label.pack()


root = tk.Tk()
root.title("PieNote")

menu = tk.Menu(root)
root.config(menu=menu)


filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open...", command=open_file)

filemenu.add_command(label="Save As...", command=save_file_as) 
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)


helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=open_about)


txt = tk.Text(root, height=15, width=50)
txt.pack(padx=10, pady=10, expand=True, fill='both')

app_icon = tk.PhotoImage(file="PieNote.png")
root.iconphoto(True, app_icon)

root.mainloop()