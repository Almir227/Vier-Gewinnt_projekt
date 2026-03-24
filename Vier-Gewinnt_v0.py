import pygame
pygame.init()

# Dieser Code-Teil wurde im Sprint 1 erstellt. In diesem Abschnitt (ca. Zeile 4-48)
# wurden noch keine Commit- und Push-Befehle verwendet, da wir diese zu diesem
# Zeitpunkt noch nicht verstanden haben bzw. ab Sprint 2 nun umsetzen werden. 

WHITE = (255,255,255)

screen = pygame.display.set_mode((390,390))
pygame.display.set_caption("VIERGEWINNT_2.py")

s6 = [  "0" ]*7
s5 = [  "0" ]*7
s4 = [  "0" ]*7
s3 = [  "0" ]*7
s2 = [  "0" ]*7
s1 = [  "0" ]*7
s0 = [  "0" ]*7
 
feld = [s0,s1,s2,s3,s4,s5,s6]

aktiv = True

while aktiv:
    pygame.draw.line(screen, WHITE, (20,20), (370,20) )
    pygame.draw.line(screen, WHITE, (20,70), (370,70) )
    pygame.draw.line(screen, WHITE, (20,120), (370,120) )
    pygame.draw.line(screen, WHITE, (20,170), (370,170) )
    pygame.draw.line(screen, WHITE, (20,220), (370,220) )
    pygame.draw.line(screen, WHITE, (20,270), (370,270) )
    pygame.draw.line(screen, WHITE, (20,320), (370,320) )
    pygame.draw.line(screen, WHITE, (20,370), (370,370) )
   
    pygame.draw.line(screen, WHITE, (20,20), (20, 370) )
    pygame.draw.line(screen, WHITE, (70,20), (70,370) )
    pygame.draw.line(screen, WHITE, (120,20), (120,370) )
    pygame.draw.line(screen, WHITE, (170,20), (170,370) )
    pygame.draw.line(screen, WHITE, (220,20), (220,370) )
    pygame.draw.line(screen, WHITE, (270,20), (270,370) )
    pygame.draw.line(screen, WHITE, (320,20), (320,370) )
    pygame.draw.line(screen, WHITE, (370,20), (370,370) )
    pygame.display.flip()

    for event in pygame.event.get():
        pygame.event.get()
        if event.type == pygame.QUIT:
            aktiv = False