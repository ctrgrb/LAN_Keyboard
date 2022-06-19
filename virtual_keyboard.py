from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as mbox
import tkinter as tk
import socket

import os
import time
import webbrowser

IP = ''

class Keypad(tk.Frame):
    def changeOnHover(button, colorOnHover, colorOnLeave,self):
      
        # adjusting backgroung of the widget
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(bg='white'))
      
        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(bg='yellow'))

    cells_small_init = [
        ["esc", "1", "2", "3", "4", "5", "6", "7","8", "9", "0", "-", "="],
        ["↹", "q", "w", "e", "r", "t", "y", 'u','i', 'o', 'p', '[', ']'],
        ["CtTa", 'a', 's', 'd', 'f', 'g', 'h', 'j','k', 'l', ';', "'", '\\'],
        ["Shift", 'z', 'x', 'c', 'v', 'b', 'n', 'm',',', '.', '/'],
    ]
    cells_big = [
        "esc", "!", "@", "#", "$", "%", "^", "&","*", "(", ")", "_", "+",
        "↹", "Q", "W", "E", "R", "T", "Y", 'U','I', 'O', 'P', '{', '}',
        "CtTa", 'A', 'S', 'D', 'F', 'G', 'H', 'J','K', 'L', ':', '"', '|',
        "Shift", 'Z', 'X', 'C', 'V', 'B', 'N', 'M','<', '>', '?'
    ]
    cells_small = [
        "esc", "1", "2", "3", "4", "5", "6", "7","8", "9", "0", "-", "=",
        "↹", "q", "w", "e", "r", "t", "y", 'u','i', 'o', 'p', '[', ']',
        "CtTa", 'a', 's', 'd', 'f', 'g', 'h', 'j','k', 'l', ';', "'", '\\',
        "Shift", 'z', 'x', 'c', 'v', 'b', 'n', 'm',',', '.', '/'
    ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        self.place(relx=0.5, rely=0.5, anchor='c')

        self.cap = False
        self.buttons = []
        for y, row in enumerate(self.cells_small_init):
            for x, item in enumerate(row):
                b = tk.Button(self, text=item, command=lambda text=item:self.append(text),font=("TkFixedFont", 30), bg = "black", fg = "white", borderwidth=3, relief="raised", width=3, height=1)
                b.grid(row=y, column=x, sticky='ew')
                #self.changeOnHover(b,'yellow','white')
                self.buttons.append(b)


        x = tk.Button(self, text="⌫", command=lambda text=item:self.append('backspace'),font=("Helvetica", 30), bg = "black", fg = "white", borderwidth=3, relief="raised", height=1,repeatdelay=50, repeatinterval=75)
        x.grid(row=0, column=13, sticky='news')
        x = tk.Button(self, text=' ↵ ', command=lambda text=item:self.append('enter'),font=("TkFixedFont", 30), bg = "black", fg = "white", borderwidth=3, relief="raised", height=1)
        x.grid(row=1, column=13, rowspan='2', sticky='news')


        x = tk.Button(self, text='Alt F4', command=lambda text=item:self.append('cls'),font=("Helvetica", 20), bg = "black", fg = "white", borderwidth=3, relief="raised", height=1)
        x.grid(row=4, column=0, sticky='news')
        x = tk.Button(self, text='⊞', command=lambda text=item:self.append('win'),font=("TkFixedFont", 30), bg = "black", fg = "white", borderwidth=3, relief="raised", height=1)
        x.grid(row=4, column=1, sticky='news')
        x = tk.Button(self, text='', command=lambda text=item:self.append('space'),font=("TkFixedFont", 30), bg = "black", fg = "white", borderwidth=3, relief="raised", height=1)
        x.grid(row=4, column=2,columnspan='6', sticky='news')
        x = tk.Button(self, text='⟲', command=lambda text=item:self.append('f5'),font=("Helvetica", 30), bg = "black", fg = "white", borderwidth=3, relief="raised", height=1)
        x.grid(row=4, column=8, sticky='news')
        x = tk.Button(self, text='⨁', command=lambda text=item:self.append('nt'),font=("Helvetica", 30), bg = "black", fg = "white", borderwidth=3, relief="raised", height=1)
        x.grid(row=4, column=9, sticky='news')
        x = tk.Button(self, text='⮽', command=lambda text=item:self.append('ct'),font=("Helvetica", 30), bg = "black", fg = "white", borderwidth=3, relief="raised", height=1)
        x.grid(row=4, column=10, sticky='news')
        x = tk.Button(self, text=' ↑ ', command=lambda text=item:self.append('up'),font=("TkFixedFont", 30), bg = "black", fg = "white", borderwidth=3, relief="raised", height=1,repeatdelay=100, repeatinterval=100)
        x.grid(row=3, column=12, sticky='ewns')
        x = tk.Button(self, text='←', command=lambda text=item:self.append('left'),font=("TkFixedFont", 30), bg = "black", fg = "white", borderwidth=3, relief="raised", height=1,repeatdelay=100, repeatinterval=100)
        x.grid(row=4, column=11, sticky='nesw')
        x = tk.Button(self, text=' ↓ ', command=lambda text=item:self.append('down'),font=("TkFixedFont", 30), bg = "black", fg = "white", borderwidth=3, relief="raised", height=1,repeatdelay=100, repeatinterval=100)
        x.grid(row=4, column=12, sticky='ewns')
        x = tk.Button(self, text='→', command=lambda text=item:self.append('right'),font=("TkFixedFont", 30), bg = "black", fg = "white", borderwidth=3, relief="raised", height=1,repeatdelay=100, repeatinterval=100)
        x.grid(row=4, column=13, sticky='ewns')
        x = tk.Button(self, text='🔊', command=lambda text=item:self.append('volumeup'),font=("TkFixedFont", 30), bg = "black", fg = "white", borderwidth=3, relief="raised", height=1,repeatdelay=500, repeatinterval=100)
        x.grid(row=3, column=13, sticky='news')
        x = tk.Button(self, text='🔉', command=lambda text=item:self.append('volumedown'),font=("TkFixedFont", 30), bg = "black", fg = "white", borderwidth=3, relief="raised", height=1,repeatdelay=500, repeatinterval=100)
        x.grid(row=3, column=11, sticky='news')

        # mouse
        '''
        x = tk.Button(self, text=' ↟ ', command=lambda text=item:self.append('mup'),font=("TkFixedFont", 30), bg = "black", fg = "white", borderwidth=3, relief="raised",repeatdelay=50, repeatinterval=75,width=3)
        x.grid(row=0, column=16, sticky='ewns')
        x = tk.Button(self, text='↞', command=lambda text=item:self.append('mleft'),font=("TkFixedFont", 30), bg = "black", fg = "white", borderwidth=3, relief="raised",repeatdelay=50, repeatinterval=75,width=3)
        x.grid(row=1, column=15, sticky='nesw')
        x = tk.Button(self, text=' ↡ ', command=lambda text=item:self.append('mdown'),font=("TkFixedFont", 30), bg = "black", fg = "white", borderwidth=3, relief="raised",repeatdelay=50, repeatinterval=75,width=3)
        x.grid(row=2, column=16, sticky='ewns')
        x = tk.Button(self, text='↠', command=lambda text=item:self.append('mright'),font=("TkFixedFont", 30), bg = "black", fg = "white", borderwidth=3, relief="raised",repeatdelay=50, repeatinterval=75,width=3)
        x.grid(row=1, column=17, sticky='ewns')
        x = tk.Button(self, text='❖', command=lambda text=item:self.append('click'),font=("Helvetica", 30), bg = "black", fg = "white", borderwidth=3, relief="raised")
        x.grid(row=1, column=16, sticky='news')
        x = tk.Button(self, text='⇕', command=lambda text=item:self.append('mclick'),font=("Helvetica", 30), bg = "black", fg = "white", borderwidth=3, relief="raised")
        x.grid(row=0, column=15, sticky='news')
        x = tk.Button(self, text='☴', command=lambda text=item:self.append('rclick'),font=("Helvetica", 30), bg = "black", fg = "white", borderwidth=3, relief="raised")
        x.grid(row=2, column=15, sticky='news')
        x = tk.Button(self, text='⇈', command=lambda text=item:self.append('scrlup'),font=("TkFixedFont", 30), bg = "black", fg = "white", borderwidth=3, relief="raised",repeatdelay=500, repeatinterval=100)
        x.grid(row=0, column=17, sticky='ew')
        x = tk.Button(self, text='⇊', command=lambda text=item:self.append('scrldwn'),font=("TkFixedFont", 30), bg = "black", fg = "white", borderwidth=3, relief="raised",repeatdelay=500, repeatinterval=100)
        x.grid(row=2, column=17, sticky='ew')
        '''

        #x.grid(row=3, column=15,columnspan=3, sticky='news')
        #x.grid(row=4, column=15,columnspan=3, sticky='news')



    def append(self, text):
        #print(text)
        if text == '↹': text = 'tab'
        if text == 'Shift':
            if self.cap:
                self.uncapitalize()
            else:
                self.capitalize()
            return
        s.sendto(text.encode(),server)

    def capitalize(self):
        self.cap = True
        for i in range(len(self.buttons)):
            item = self.cells_big[i]
            self.buttons[i].config(text=item, command=lambda text=item:self.append(text))

    def uncapitalize(self):
        self.cap = False
        for i in range(len(self.buttons)):
            item = self.cells_small[i]
            self.buttons[i].config(text=item, command=lambda text=item:self.append(text))


#-------------------------------------------------------#
def exit_win():
    #if messagebox.askokcancel("Exit", "Do you want to exit?"):
    root.destroy()

root = Tk()
#root.attributes('-fullscreen', True)
root.configure(bg='black')
root.geometry("1520x400+0+0")
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server = (IP,4444)
keypad = Keypad(root)

def exit_win():
    #if messagebox.askokcancel("Exit", "Do you want to exit?"):
    root.destroy()


root.protocol("WM_DELETE_WINDOW", exit_win)
#os.system('"C:\Program Files\TeamViewer\TeamViewer.exe"')
root.mainloop()


