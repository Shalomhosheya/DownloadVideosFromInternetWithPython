import time
import os
import shutil
import subprocess

def download_torrent_with_aria2(torrent_link, download_dir):
    if shutil.which("aria2c") is None:
        print("Error: aria2c is not installed or not found in PATH.")
        return
    try:
        # Make sure the download directory exists
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        
        print(f"Downloading torrent using aria2c to {download_dir}...\n")
        
        # Record the start time
        start_time = time.time()
        
        # Execute aria2c and capture the real-time output
        process = subprocess.Popen(
            ["aria2c", "--dir", download_dir, "--console-log-level=notice", torrent_link],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1
        )
        
        # Read and display aria2c output line by line
        for line in process.stdout:
            print(line.strip())
            
            # Look for download progress (e.g., "DL: 10MB/s" or similar)
            if "DL:" in line:
                print(line.strip())  # You can modify this line to extract specific data
                
        # Wait for the process to complete
        process.wait()

        # Record the end time
        end_time = time.time()

        if process.returncode == 0:
            # Calculate the elapsed time
            elapsed_time = end_time - start_time
            print(f"\nDownload complete! Time taken: {elapsed_time:.2f} seconds")
        else:
            print("\nAn error occurred during the download.")
    
    except Exception as e:
        print(f"An error occurred during aria2c download: {e}")

# Main program
print("Click EX for download")
choice = input("Enter the Permission: ")

torrent_link = input("Enter the torrent/magnet link: ")
download_dir = input("Enter the path where you want to save the video: ")

if choice == "EX":
    download_torrent_with_aria2(torrent_link, download_dir)
else:
    print("Invalid choice. Exiting.")
