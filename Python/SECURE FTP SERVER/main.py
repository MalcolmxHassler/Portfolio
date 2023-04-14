from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import TLS_FTPHandler ##for FTPS

import customtkinter as ctk
import tkinter
from tkinter import filedialog
import os
import logging

import threading as thr
from pathlib import Path

def ftp_server(username,password,location):
    authorizer = DummyAuthorizer()
    authorizer.add_user(username, password,location, perm="elradfmwMT")
    authorizer.add_anonymous(os.getcwd())
    handler = TLS_FTPHandler
    handler.certfile = 'keycert.pem'
    handler.authorizer = authorizer
    handler.log_prefix = 'XXX [%(username)s]@%(remote_ip)s'
    logging.basicConfig(filename='log/pyftpd.log', level=logging.DEBUG)
    server = FTPServer(("0.0.0.0", 21), handler)
    #server.max_cons = 1000
    #server.max_cons_per_ip = 10
    server.serve_forever()

def stop_server():
    server.close_when_done()

def openFile():
    my_dir=filedialog.askdirectory()
    folder.configure(text=my_dir)

def startbox():
    user = username.get()
    passw = password.get()
    #fol= folder.cget("text")
    fol=str(Path.home()/ "Downloads")
    print(user,passw,fol)
    if user=='' or passw=='':
        print('Fill the box..')
    else:
        ftp_server(user,passw,fol)
        

def threading():
    t1=thr.Thread(target=startbox)
    t1.start()
    
    

def page2():
    username.destroy()
    password.destroy()
    start_button.destroy()
    title_label.destroy()
    uptime = ctk.CTkLabel(frame, text="server is running... ", font=ctk.CTkFont(size=10,weight="bold"))
    uptime.pack(padx=10,pady=(30,20))
    stop_button=ctk.CTkButton(frame,text="STOP", width=500,border_width=0,corner_radius=8)
    stop_button.pack(pady=0,padx=150)
    label1 = ctk.CTkLabel(frame, text="Powered by", font=ctk.CTkFont(size=10,weight="bold"))
    label1.pack(pady=0)
    label2 = ctk.CTkLabel(frame, text="GNINGHAYE Malcolmx", font=ctk.CTkFont(size=10,weight="bold"))
    label2.pack()
    

#if __name__ == "__main__":


##for building the GUI
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app=ctk.CTk()
app.geometry("400x400")
app.title("X-FTP File Transfer")

frame=ctk.CTkFrame(master=app)
frame.pack(pady=20,padx=20,fill="both",expand=True)
##titre
title_label = ctk.CTkLabel(frame, text="X-FTP FILE TRANSFER", font=ctk.CTkFont(size=20,weight="bold"))
title_label.pack(padx=10,pady=(30,20))



##textbox
username=ctk.CTkEntry(master=frame,placeholder_text="Enter Username",width=300)
password=ctk.CTkEntry(frame,placeholder_text="Enter Password",width=300,show="*")
username.pack(pady=10,padx=10)
password.pack(pady=10,padx=10)

#folder=ctk.CTkButton(frame,text="Select Directory", width=200,font=("light_color",10),anchor=tkinter.RIGHT,command=openFile)
#folder.pack(pady=10,padx=100)
#folder.grid(row=0,column=0)
#my_dir=''
#folder = ctk.CTkLabel(frame, text=my_dir, font=ctk.CTkFont(size=10,weight="bold"),fg_color=("red", "red"),anchor=tkinter.W)
#folder.pack(pady=10,padx=100)
#folder.place(relx=0.5, rely=0.5, )

##button
start_button=ctk.CTkButton(frame,text="START", width=500,border_width=0,corner_radius=8,command=threading)
start_button.pack(pady=0,padx=150)


title_label1 = ctk.CTkLabel(frame, text="Powered by", font=ctk.CTkFont(size=10,weight="bold"))
title_label1.pack(pady=0)
title_label2 = ctk.CTkLabel(frame, text="GNINGHAYE Malcolmx", font=ctk.CTkFont(size=10,weight="bold"))
title_label2.pack()

app.mainloop()

