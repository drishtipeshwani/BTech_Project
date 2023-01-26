from picamera import PiCamera
import time
import sys

filename = "video_" + str(time.time()) + ".h264"
framerate = 30
resolution_w = 1280
resolution_h = 720
videoTime = 10

for index in range(len(sys.argv)):
    if sys.argv[index]=="-fps":
        framerate = int(sys.argv[index+1])
    if sys.argv[index]=="-t":
        videoTime = int(sys.argv[index+1])
    if sys.argv[index]=="-r":
        resolution_w = int(sys.argv[index+1])
        resolution_h = int(sys.argv[index+2])
    if sys.argv[index]=="-o":
        filename = sys.argv[index+1]

camera = PiCamera()
time.sleep(2)
camera.framerate = framerate
camera.resolution = (resolution_w,resolution_h)
camera.vflip = True
camera.contrast = 10

print("Framerate - " + str(framerate))
print("Video Time - " + str(videoTime))
print("Resolution - " + str(resolution_w) + " " + str(resolution_h))
print("Filename - " + filename)
print("Start recording...")
camera.start_recording(filename)
camera.wait_recording(videoTime)
camera.stop_recording()
print("Done.")

