from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil


def select_path():
    # function to select dowanload file location
    path = filedialog.askdirectory()
    path_label.config(text=path)

#download function
def file_down():
     data = link_field.get()
     user_path = path_label.cget("text")
     screen.title('Downloading....................') # video downloading message
     mp4_video = YouTube(data).streams.get_highest_resolution().download() # video and video quality functionn
     vid_clip = VideoFileClip(mp4_video)
     vid_clip.close()
     shutil.move(mp4_video, user_path)
     screen.title('Download Complete! Download Another File.??') # save file to selected directory




screen = Tk()
title = screen.title('Youtube Video Downloader')
canvas = Canvas(screen, width=500, height=500)
screen.resizable(height=False,width=False)
canvas.pack()



#link field
link_field = Entry(screen, width=40, font=('Arial', 15) )
link_label = Label(screen, text="Enter Video Link: ", font=('Arial', 15))

#Select Path for saving the file
path_label = Label(screen, text="Select Path For Download", font=('Arial', 15))
select_btn =  Button(screen, text="Select Path", bg='blue', padx='22', pady='5',font=('Arial', 15), fg='#fff',command=select_path)
#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#Add widgets to window 
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

#Download btns
download_btn = Button(screen, text="Download File",bg='red', padx='22', pady='5',font=('Arial', 15), fg='#fff',command=file_down)
#add to canvas
canvas.create_window(250, 390, window=download_btn)



screen.mainloop()