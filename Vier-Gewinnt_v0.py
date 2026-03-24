import pygame
pygame.init()

# Bei diesen Abschnitten (siehe Markiert mit Kommentare #<------ und #------>)
# wurden noch keine Commit- und Push-Befehle verwendet, da wir diese zu diesem
# Zeitpunkt noch nicht verstanden haben wie es funktioniert. Ab Sprint 2 wird es nun umgesetzt. 

#<------
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

screen = pygame.display.set_mode((390,390))
pygame.display.set_caption("VIERGEWINNT_2.py")

s6 = [  "0", "T", "T", "T", "0", "0", "0"]
s5 = [  "0" ]*7
s4 = [  "0" ]*7
s3 = [  "0" ]*7
s2 = [  "0" ]*7
s1 = [  "0" ]*7
s0 = [  "0" ]*7
 
feld = [s0,s1,s2,s3,s4,s5,s6]
#------>

breite_gewinnlinie = 6
B = 18
breite_kreuz = 2


def feld_ausgabe():
    y = 0
    while y < 7:
        x = 0
        while x < 7:
            if feld[y][x] == "T":
                pygame.draw.line(screen, RED, (45+50*x-B, 45+50*(6-y)+B),(45+50*x+B,45+50*(6-y)-B),breite_kreuz)
                pygame.draw.line(screen, RED, (45+50*x-B, 45+50*(6-y)-B),(45+50*x+B,45+50*(6-y)+B) ,breite_kreuz)
                pygame.display.flip()
            elif feld[y][x] == "X":
                pygame.draw.line(screen, GREEN, (45+50*x-B, 45+50*(6-y)+B),(45+50*x+B,45+50*(6-y)-B),breite_kreuz )
                pygame.draw.line(screen, GREEN, (45+50*x-B, 45+50*(6-y)-B),(45+50*x+B,45+50*(6-y)+B),breite_kreuz )
                pygame.display.flip()
            else:
                pass
            x = x + 1
        y = y + 1

#<------
aktiv = True

while aktiv:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            aktiv = False

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

    feld_ausgabe()

    pygame.display.flip()
#------> 