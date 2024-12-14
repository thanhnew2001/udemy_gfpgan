import yt_dlp
import subprocess
import os

def download_video(url, start_time, end_time, output_filename):
    # Define download options for yt-dlp
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download the best quality video and audio
        'outtmpl': 'temp_video.%(ext)s',  # Temporary file name
    }

    # Download the full video using yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # After downloading, use ffmpeg to trim the video
    input_file = 'temp_video.mp4'
    output_file = output_filename
    
    # Command to trim the video using ffmpeg
    ffmpeg_cmd = [
        'ffmpeg', 
        '-i', input_file,         # Input file
        '-ss', str(start_time),    # Start time in seconds
        '-to', str(end_time),      # End time in seconds
        '-c:v', 'libx264',         # Video codec
        '-c:a', 'aac',             # Audio codec
        '-strict', 'experimental', # To avoid issues with audio codec
        '-preset', 'fast',         # Compression speed (adjust if needed)
        output_file                # Output file
    ]
    
    # Run the ffmpeg command to trim the video
    subprocess.run(ffmpeg_cmd)

    # Clean up the temporary downloaded file
    os.remove(input_file)

    print(f"Video has been downloaded and trimmed. Saved as {output_file}")

# Example usage:
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your video URL
start_time = 30  # Start at 30 seconds
end_time = 60    # End at 60 seconds
output_filename = 'trimmed_video.mp4'  # Output filename for the trimmed video

download_video(url, start_time, end_time, output_filename)
