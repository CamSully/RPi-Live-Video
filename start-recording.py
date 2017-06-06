# An alternate script to start video recording from the Pi camera.
# Derek Haas and Cameron Sullivan - 6-6-17 

# Module to check file existence.
import os.path
# Module to execute terminal commands.
from subprocess import call

print "Starting recording python script..."
fileNum = 0

# Check to see if next file exists and create next file.
# We use a numerical system (1.mp4, 2.mp4, etc).
while os.path.exists("/home/pi/recordings/%d.mp4" % fileNum):
	fileNum += 1

# Use ffmpeg to stream the video from raspivid (terminal command) and save video to file created.
print "Starting ffmpeg..."
call(["/opt/stream/bin/ffmpeg", "-i", "rtsp://@127.0.0.1:8554/", "-vcodec", "copy", "-acodec", "none", "-f", "mp4", "/home/pi/recordings/%d.mp4" % fileNum])
