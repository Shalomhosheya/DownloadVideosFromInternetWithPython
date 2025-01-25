import time
import os
import shutil
import subprocess

def download_torrent_with_aria2(torrent_link):
    if shutil.which("aria2c") is None:
        print("Error: aria2c is not installed or not found in PATH.")
        return
    
    try:
        print("Downloading torrent using aria2c...\n")
        
        # Execute aria2c and capture the real-time output
        process = subprocess.Popen(
            ["aria2c", torrent_link],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1
        )
        
        # Read and display aria2c output line by line
        for line in process.stdout:
            print(line.strip())

        # Wait for the process to complete
        process.wait()

        if process.returncode == 0:
            
            print("\nDownload complete!")
        else:
            print("\nAn error occurred during the download.")
    
    except Exception as e:
        print(f"An error occurred during aria2c download: {e}")

# Main program
print(" click EX for download")
choice = input("Enter Response: ): ")

torrent_link = input("Enter the torrent/magnet link: ")

if choice == "EX":
    download_torrent_with_aria2(torrent_link)
else:
    print("Invalid choice. Exiting.")
