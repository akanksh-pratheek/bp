import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 30
    camera.start_recording('ball_test.h264')
    camera.wait_recording(5)
    camera.stop_recording()
