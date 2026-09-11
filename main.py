import tkinter as tk
import ttkbootstrap as ttk
import assembler

#def assemble():
#    pass

window = ttk.Window(themename="darkly")
window.title("4004 Assembler")
window.geometry("600x500")

i4004_image = tk.PhotoImage(file="i4004.png")
window.iconphoto(False, i4004_image)

title_label = ttk.Label(master=window, text="4004 Machine Code: ", font=("Calibri", 18, "bold"))
title_label.pack()

text_label = ttk.Text(master=window, height=10, width=20, font=("Calibri", 14))
text_label.pack()
text_label.insert(tk.END, assembler.m_code_all)

real_time_string = tk.StringVar()
real_time_string.set(f"Real time: {(assembler.t2[0] - assembler.t1[0]) * 1000000} microseconds")
real_label = ttk.Label(
    master=window,
    text="real",
    font=("Calibri", 14),
    textvariable=real_time_string
)
real_label.pack()

cpu_time_string = tk.StringVar()
cpu_time_string.set(f"CPU time: {(assembler.t2[1] - assembler.t1[1]) * 1000000} microseconds")
cpu_label = ttk.Label(
    master=window,
    text="cpu",
    font=("Calibri", 14),
    textvariable=cpu_time_string
)
cpu_label.pack()

window.mainloop()
