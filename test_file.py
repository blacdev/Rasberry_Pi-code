import pygame
import pygame.camera

# Captured image dimensions. It should be less than or equal to the maximum dimensions acceptable by the camera.
width = 320
height = 240

# Initializing PyGame and the camera.
pygame.init()
pygame.camera.init()

# Specifying the camera to be used for capturing images. If there is a single camera, then it have the index 0.
cam = pygame.camera.Camera("/dev/video2", (width, height))
cam1 = pygame.camera.Camera("/dev/video4", (width, height))

# Preparing a resizable window of the specified size for displaying the captured images.
window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
window1 = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# Starting the camera for capturing images.
cam.start()
cam1.start()

# Capturing an image.
image = cam.get_image()
image1 = cam1.get_image()

# Stopping the camera.
cam.stop()
cam1.stop()

# Displaying the image on the window starting from the top-left corner.
window.blit(image, (0, 0))

# Refreshing the window.
# pygame.display.update()

# Saving the captured image.
pygame.image.save(window, "left/PyGame_image.jpg")
pygame.image.save(window1, "PyGame1_image.jpg")
