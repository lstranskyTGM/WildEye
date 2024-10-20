from gpiozero import MotionSensor
from signal import pause


# Use GPIO pin 18 for the PIR sensor
pir_sensor = MotionSensor(18)

def motion_detected():
    print("Motion detected!")

def no_motion():
    print("No motion detected.")


if __name__ == '__main__':
    # Set up event handlers
    pir_sensor.when_motion = motion_detected
    pir_sensor.when_no_motion = no_motion

    # Keep the script running to listen for motion events
    pause()
