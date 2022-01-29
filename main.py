"""
HOW THIS CODE IS SUPPOSED  TO WORK

When IR_1 is high,camera 1 takes picture of the car and the ultrasonic sensors 1 and 2 calculate the time
When IR_2 is High,camera 1 takes picture of the car and the ultrasonic sensors 3 and 4 calculate the time

- Run 'sudo apt-get install v4l-utils' to allow you get the list of cameras plugged into the rasberry pi
- Run 'v4l2-ctl --list-devices' to see the list of cameras

"""

from timeit import default_timer as timer
import time
from datetime import timedelta
import RPi.GPIO as GPIO
import requests
import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

#  This allows us use the numbers printed on the board to refrence the pin to be used.
GPIO.setmode(GPIO.BORAD)

fixed_time = 0.99
fixed_distance = "value"  # This will be calculated to fit the length used for the body of the vehicle

#  Initializing ultrasonic trigger pins
trig_1, trig_2, trig_3, trig_4 = 10, 12, 16, 18

#  Initializing ultrasonic echo pins
echo_1, echo_2, echo_3, echo_4 = 11, 13, 15, 19

#  Initializing IR sensors one and two
IR_1, IR_2 = 3, 5

# initializing camera's one and two

# image pixel size
width, height = 320, 240

# camera
cam_1 = pygame.camera.Camera("/dev/video2", (width, height))
cam_2 = pygame.camera.Camera("/dev/video4", (width, height))

window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
window1 = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# start cameras
cam_1.start()
cam_2.start()


# GPIO pin setup
GPIO.setup(trig_1, GPIO.OUT)
GPIO.setup(echo_1, GPIO.IN)

GPIO.setup(trig_2, GPIO.OUT)
GPIO.setup(echo_2, GPIO.IN)

GPIO.setup(trig_3, GPIO.OUT)
GPIO.setup(echo_3, GPIO.IN)

GPIO.setup(trig_4, GPIO.OUT)
GPIO.setup(echo_4, GPIO.IN)

GPIO.setup(IR_1, GPIO.IN)
GPIO.setup(IR_2, GPIO.IN)


def incoming_traffic():
    snap_picture = cam_1.get_image()
    snap_picture.stop()
    window.blit(image, (0, 0))
    sensors_1 = GPIO.input(echo_1)
    sensors_2 = GPIO.input(echo_2)

    if sensors_1 == 0:
        start = timer()

    if sensors_2 == 0:
        end = timer()

    time = timedelta(seconds=end - start)

    if time > fixed_time:
        # delete_snap_picture =  this will delete_snap_picture
        is_speeding = False

        pass

    if time < fixed_time:
        image = pygame.image.save(window, "left/PyGame_image.jpg")
        url = "https://road-traffic-offender.herokuapp.com/file/upload/"
        payload = {"speed": "120 still needs to be converted", "is_speeding": True}
        files = [
            (
                "image",
                ("image.png", open("left/image.png", "rb"), "image/png"),
            )
        ]  # needs editing
        headers = {}

        response = requests.request(
            "POST", url, headers=headers, data=payload, files=files
        )
        if response:
            True


def outgoing_traffic():
    # snap_picture =   This is where the command for taking pictures will seat . The name of the picture will be the speed
    sensors_1 = GPIO.input(echo_3)
    sensors_2 = GPIO.input(echo_4)

    if sensors_1 == 0:
        start = timer()
    if sensors_2 == 0:
        end = timer()
    time = timedelta(seconds=end - start)

    if time > fixed_time:
        # delete_snap_picture =  this will delete_snap_picture
        is_speeding = False

        pass

    if time < fixed_time:
        url = "https://road-traffic-offender.herokuapp.com/file/upload/"
        payload = {"speed": "120", "is_speeding": "False"}
        files = [
            (
                "image",
                ("image.png", open("/home/blac/Pictures/image.png", "rb"), "image/png"),
            )
        ]  # needs editing
        headers = {}

        response = requests.request(
            "POST", url, headers=headers, data=payload, files=files
        )
        if response:
            True


# try:
#     while True:
#        GPIO.output(trig_1, True)
#        GPIO.output(trig_2, True)
#        GPIO.output(trig_3, True)
#        GPIO.output(trig_4, True)
#        time.sleep(0.00001)
#        GPIO.output(trig_1, False)
#        GPIO.output(trig_2, False)
#        GPIO.output(trig_3, False)
#        GPIO.output(trig_4, False)

# Setting echo pin high with 0


# start = timer()
# print("start")
# time.sleep(60)
# print("stop")
# end = timer()
# print(timedelta(seconds=end - start))
