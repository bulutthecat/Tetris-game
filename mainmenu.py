import pygame
import cv2
import json

# resolution information
# The resolution of the video is 720x480
# The resolution of the buttons can be anything

# load the main menu video
cap = cv2.VideoCapture('assets\mainmenu.mp4')
start_img = pygame.image.load(r'assets\buttons\menu\start.png')
quit_img = pygame.image.load(r'assets\buttons\menu\quit.png')

ready, frame = cap.read()
fps = cap.get(cv2.CAP_PROP_FPS)

window = pygame.display.set_mode(size=(720, 480))
clock = pygame.time.Clock()

pygame.display.set_caption('Tetris')

def start():
    print("start pressed")
    pass

def quit():
    print("quit pressed")
    pygame.quit()
    exit()
    pass

while ready:
    clock.tick(fps)
    # draw the start button

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # if the mouse is hovering over the button, change the image
        if event.type == pygame.MOUSEMOTION:
            if start_img_rect.collidepoint(event.pos):
                start_img = pygame.image.load(r'assets\buttons\menu\start_hover.png')
            else:
                start_img = pygame.image.load(r'assets\buttons\menu\start.png')
            if quit_img_rect.collidepoint(event.pos):
                quit_img = pygame.image.load(r'assets\buttons\menu\quit_hover.png')
            else:
                quit_img = pygame.image.load(r'assets\buttons\menu\quit.png')

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_img_rect.collidepoint(event.pos):
                start()
            if quit_img_rect.collidepoint(event.pos):
                quit() 
    
    ready, frame = cap.read()
    if ready:
        vidtex = pygame.image.frombuffer(
            frame.tobytes(), frame.shape[1::-1], 'BGR'
        )

    window.blit(vidtex, (0, 0)) # render the video frame first, as all UI elements should be on top of it

    play_position = (150, 200)
    quit_position = (150, 300)

    start_img_rect = start_img.get_rect(topleft=play_position)
    quit_img_rect = quit_img.get_rect(topleft=quit_position)

    window.blit(start_img, start_img_rect)
    window.blit(quit_img, quit_img_rect)

    pygame.display.flip()

pygame.quit()
exit()
    