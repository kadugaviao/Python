import pygame

def musica():
    pygame.init()
    pygame.mixer.music.load('megadeth.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():  # Verifica se a música ainda está tocando
        pygame.time.Clock().tick(10)

musica()