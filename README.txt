Live-video payload Raspberry Pi README
Derek Haas and Cameron Sullivan June 2017

The Montana folks had their own script to record video: ~/bin/start-recording.sh
The script had to be manually executed for video recording to begin.
Also, their script named videos by date, and the Raspberry Pi does not have an internal clock.
Therefore, plugging the camera in twice would cause videos to be overwritten.

We wrote our own script in python to start video recording but name the files numerically.
Our script is ~/bin/start-recording.py

Also, we wanted video recording to start shortly after boot, so we created our own service.
Our service is /etc/systemd/system/picam-record.service
Our service depends on the operation of /etc/systemd/system/picam-rtsp-server.service
The rtsp service creates an rtsp server with a video stream that we convert to mp4 video.
The final video is located in ~/recordings
The most recently recorded video is the highest number video.
VLC seemed unable to view our videos, so we transfered recorded videos to another computer to view.

In order to update the Pi (6-7-17), we removed the static IP and set the Pi back to its Raspian defaults.
After we completed the updates we set the static IP back to what it was.
IP configuration was done in /etc/network/interfaces

We are very sorry about the keyboard.
We thought the updates would allow us to fix the keyboard, but they did not.
We tried changing locale & keyboard settings in raspi-config, but nothing fixes it.
May the pipe forever be a struggle for you.

When retrieving the payload during recovery, it was brought to our attention it was risky to unplug the Pi while still powered.
To avoid this, we developed a button pressing system, wired into the GPIO pin 18.
When the Pi boots, a service will execute a python script. If the button is pressed, the Pi will shutdown.
The python code can be found at ~/bin/button-poweroff.py
The service can be found at /etc/systemd/system/button-poweroff.service 

