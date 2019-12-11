# import pygame module in this program
import pygame
def fullscreen_fix(game_height):
    """ Sets full screen display mode and draws a square in the top left """
    # Set the display mode to the current screen resolution
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # create a square pygame surface
    game_surface = pygame.Surface((game_height, game_height))
    game_surface.fill((255, 255, 255))

    # draw a square in the top left
    pygame.draw.rect(game_surface, (0, 0, 0), pygame.draw.rect(10, 10, 200, 200))

    # make the largest square surface that will fit on the screen
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    smallest_side = min(screen_width, screen_height)
    screen_surface = pygame.Surface((smallest_side, smallest_side))

    # scale the game surface up to the larger surface
    pygame.transform.scale(
        game_surface,  # surface to be scaled
        (smallest_side, smallest_side),  # scale up to (width, height)
        screen_surface)  # surface that game_surface will be scaled onto

    # place the larger surface in the centre of the screen
    screen.blit(
        screen_surface,
        ((screen_width - smallest_side) // 2,  # x pos
        (screen_height - smallest_side) // 2))  # y pos

    pygame.display.flip()
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# define the rgb value
# for white colour
white = (255, 255, 255)

# assigning values to x and y variable

# create the display surface object
# of specific dimension..e(x, y).

image = pygame.image.load("FOURBLOBS.png")
image = pygame.transform.scale(image, (1280,720))
display_surface = pygame.display.set_mode((1280,720),pygame.FULLSCREEN)

window = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption('image')


while True:
    window.blit(image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pygame.quit()
            quit()

        pygame.display.update()
