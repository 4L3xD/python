import mixer as music

# Inicializando o mixer PyGame
music.pygame.mixer.init()

music.pygame.mixer.music.load('Derviche.m4a')
music.pygame.mixer.music.play()
music.pygame.event.wait()
input()