import os
import picamera
import time
import RPi.GPIO as GPIO

# Function to capture an image
def capture_image(capture_images, filename):
    # Ensure the directory exists
    if not os.path.exists(capture_images):
        os.makedirs(capture_images)

    # Initialize the PiCamera
    with picamera.PiCamera() as camera:
        # Adjust camera settings if needed
        camera.resolution = (1920, 1080)  # Set resolution
        # camera.rotation = 180             # Set rotation

        # Capture an image
        camera.start_preview()
        # Add a delay to allow the camera to adjust to light levels
        time.sleep(2)
        camera.capture(os.path.join(capture_images, filename))
        camera.stop_preview()