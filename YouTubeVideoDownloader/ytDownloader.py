import yt_dlp

# Output folder
output_folder = r"C:\Users\natha\OneDrive\Documents\YouTubeVideoDownloader"

# Prompt for link
link = input("Enter the YouTube video link: ")

# yt-dlp options
ydl_opts = {
    'format': 'best',  # Download the best quality
    'outtmpl': f"{output_folder}/%(title)s.%(ext)s",  # Save with video title
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print(f"Download completed successfully in {output_folder}")
except Exception as e:
    print(f"An error occurred: {e}")
