import yt_dlp

link = input("Enter YouTube link: ")
ydl_opts = {'outtmpl': '%(title)s.%(ext)s'}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
print("Video downloaded successfully!")
