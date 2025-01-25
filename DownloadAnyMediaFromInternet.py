import yt_dlp

def list_formats(link):
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(link, download=False)
        print("\nAvailable formats:")
        for fmt in info['formats']:
            print(f"Format ID: {fmt['format_id']} | Resolution: {fmt.get('resolution', 'N/A')} | "
                  f"Extension: {fmt['ext']} | Video Codec: {fmt.get('vcodec', 'N/A')}")

link = input("Enter the link: ")

list_formats(link)

format_id = input("\nEnter the Format ID of the desired resolution: ")

ydl_opts = {
    'format': format_id, 
    'outtmpl': '%(title)s.%(ext)s',  
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print("Video downloaded successfully!")
