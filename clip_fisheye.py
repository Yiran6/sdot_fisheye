#requires python packages: schedule
#requires ffmpeg
import subprocess
import schedule
import time
from datetime import datetime, timedelta 

output_path = 'D:\\SDOT_fisheye_camera\\sdot15NE40'
video_source = 'https://61e0c5d388c2e.streamlock.net/live/15_NE_40_GS.stream/playlist.m3u8'
duration = 600 #collect time duration = 5min (300 sec)

def download_stream(m3u8_url, output_file, duration, fps=30):
    command = [
        'ffmpeg', '-i', m3u8_url,
        '-r', str(fps),  # Set FPS
        '-t', str(duration),  # Set duration in seconds
        '-c', 'copy',  # Copy the stream directly without re-encoding
        '-bsf:a', 'aac_adtstoasc',  # Bitstream filter for audio
        output_file
    ]
    subprocess.run(command)

def job():
    print("Starting download...")
    m3u8_url = video_source
    current_time = datetime.now()
    start_time = current_time.strftime("%Y%m%d_%H%M")
    end_time = current_time+timedelta(seconds=duration)
    end_time = end_time.strftime("%H%M")
    output_file = f'{output_path}_{start_time}_to_{end_time}.avi'  # Change to .avi if needed
    download_stream(m3u8_url, output_file, duration)
    print("Download completed.")

# Schedule your jobs here
schedule.every().friday.at("08:00").do(job)
schedule.every().friday.at("09:00").do(job)
schedule.every().friday.at("10:00").do(job)
schedule.every().friday.at("13:00").do(job)
schedule.every().friday.at("16:00").do(job)
schedule.every().friday.at("17:00").do(job)
schedule.every().friday.at("18:00").do(job)
schedule.every().friday.at("21:00").do(job)
schedule.every().friday.at("22:00").do(job)
#schedule.every().thursday.at("16:18").do(job)

# Infinite loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait one minute before checking again
