# import pygame module in this program
import pygame

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# define the rgb value
# for white colour
white = (255, 255, 255)

# assigning values to x and y variable
x = 400
y = 400

# create the display surface object
# of specific dimension..e(x, y).
display_surface = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

# set the pygame window name
pygame.display.set_caption('image')

# create a surface object, image is drawn on it.
image = pygame.image.load("FOURBLOBS.png")
image = pygame.transform.scale(image, (1920, 1080))


# infinite loop
while True:

    # completely fill the surface object
    # with white colour
    display_surface.fill(white)

    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    display_surface.blit(image, (0, 0))

    # iterate over the list of event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is quit
        # then quitting the pygame
        # and program both.
        if event.type == pygame.quit:

            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

        # draws the surface object to the screen.
        pygame.display.update()
