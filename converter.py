import tkinter as tk
import tkinter.ttk as ttk
from pytube import YouTube
from moviepy.editor import *

window = tk.Tk()
window.title("YT to mp3 converter")
save_path = "D:/Music/converter_music/"

mp3_flag = 1
mp4_flag = 0

def convert_command():
    if mp3_flag == 1:
        url = url_entry.get()
        # Use pytube to download the video
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        
        # Download the video to a file
        out_file = video.download(output_path=save_path)
        
        # Set up new filename for the MP3
        new_file = out_file.replace(".mp4", ".mp3")
        # Use moviepy to convert video audio to mp3
        video_clip = AudioFileClip(out_file)
        video_clip.write_audiofile(new_file)
        
        # Remove the original video file
        os.remove(out_file)
        
        return new_file  # Return the path to the new file
"""
    elif mp4_flag == 1:
        url = url_entry.get()
        video_info = youtube_dl.YoutubeDL().extract_info(
            url = url,download=False
        )
        filename = f"{video_info['title']}.mp4"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        print("Download complete... {}".format(filename))
"""
def mp3_command():
    mp3_flag = 1
    mp4_flag = 0
    mp3_btn["relief"] = tk.SUNKEN
    mp4_btn["relief"] = tk.RAISED
    mp4_btn["borderwidth"] = 2
    mp3_btn["borderwidth"] = 5


def mp4_command():
    mp4_flag = 1
    mp3_flag = 0
    mp4_btn["relief"] = tk.SUNKEN
    mp3_btn["relief"] = tk.RAISED
    mp4_btn["borderwidth"] = 5
    mp3_btn["borderwidth"] = 2

url_entry_frame = tk.Frame()
convert_btn_frame = tk.Frame()
mp3_4_btn_frame = tk.Frame()

url_entry = tk.Entry(master=url_entry_frame,
                     width=50
                     )
url_entry.pack(side=tk.RIGHT)



mp3_btn = tk.Button(master=mp3_4_btn_frame,
                    text=".mp3",
                    width=10,
                    height=1,
                    command=mp3_command,
                    borderwidth=5,
                    relief=tk.SUNKEN
                    )
mp3_btn.pack(side=tk.LEFT)

mp4_btn = tk.Button(master=mp3_4_btn_frame,
                    text=".mp4",
                    width=10,
                    height=1,
                    command=mp4_command
                    )
mp4_btn.pack(side=tk.LEFT)

convert_btn = tk.Button(master=convert_btn_frame,
                        text="Convert",
                        width=10,
                        height=1,
                        command=convert_command
                        )
convert_btn.pack(side=tk.TOP)


url_entry_frame.pack(side=tk.TOP)
convert_btn_frame.pack(side=tk.RIGHT)
mp3_4_btn_frame.pack()

# Start the event loop.
window.mainloop()