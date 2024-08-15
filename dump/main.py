import os
import time
import picamera
import RPi.GPIO as GPIO

import dump.capture_image as capture_image
import read_text_file
import dump.log_to_csv as log_to_csv
import dump.get_next_filename as get_next_filename

# Main function
def main():
    save_directory = "/home/pi/Desktop/GarbageDetection/PhotoOutput"  # Directory to save captured images
    csv_file = os.path.join(save_directory, "image_tags.csv")  # Path to the CSV file

    # Capture an image
    filename = get_next_filename(save_directory, "capture", "jpeg")  # Generate next filename
    print("Capturing image...")
    capture_image(save_directory, filename)  # Capture image
    print(f"Image captured and saved to {os.path.join(save_directory, filename)}")

    # Read the content from the prediction output text file
    directory = '/home/pi/Desktop/GarbageDetection/TextInput'  # Directory containing the prediction output text file
    text_filename = 'prediction_output.txt'  # Name of the prediction output text file
    file_content = read_text_file(directory, text_filename)  # Read content from the text file

    if file_content is not None:
        print(file_content)  # Print the content of the text file

        # Log the image filename and its associated tag to the CSV file
        log_to_csv(csv_file, filename, file_content)

        # Define GPIO pins for different materials based on the file content
        if file_content == "BIODEGRADABLE":
            control_pins = [11, 13, 15, 19]
        elif file_content in ["CARDBOARD", "GLASS", "METAL", "PAPER", "PLASTIC"]:
            control_pins = [29, 31, 33, 35]
        else:
            control_pins = []

        if control_pins:
            # Initialize GPIO pins
            for pin in control_pins:
                GPIO.setup(pin, GPIO.OUT)  # Set control pins as output
                GPIO.output(pin, 0)  # Set initial state to LOW

            # Define the sequence for the stepper motor
            seq = [
                [1, 0, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 1],
                [1, 0, 0, 1],
            ]

            # Rotate the stepper motor
            for i in range(512):  # Number of steps
                for halfstep in range(8):  # Half-step sequence
                    for pin in range(4):  # Iterate over control pins
                        GPIO.output(control_pins[pin], seq[halfstep][pin])  # Set pin state
                    time.sleep(0.001)  # Small delay for motor step timing

            GPIO.cleanup()  # Clean up GPIO settings

if __name__ == "__main__":
    main()  # Run the main function