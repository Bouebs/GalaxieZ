import pygame

"""
<Sound>.play(loop = 0, time = ms 0 signifie maxtime, fadein = ms)
        .stop()
        .fadeout(ms)
        .set_volume(entre 0.0 et 1.0)
        .get_volume()
        .get_lenght(en secondes)

"""


pygame.init()

def gerer_la_musique(commande):
    ambiant_song = pygame.mixer.Sound("musicloop.wav")
    if commande == "play":
        ambiant_song.play(2,0,5000)
    elif commande == "stop":
        ambiant_song.stop()
