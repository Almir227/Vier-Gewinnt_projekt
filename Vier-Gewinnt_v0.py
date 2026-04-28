import pygame 
pygame.init()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

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


breite_gewinnlinie = 6
B = 18
breite_kreuz = 2

def quer_gewinnen(B):
    b = 0
    while b < 7:
        a = 0
        while a < 4:
            if feld[b][a] == feld[b][a+1] == feld[b][a+2] == feld[b][a+3] and feld[b][a] != "0":
                
                if feld[b][a] == "T":
                    pygame.draw.line(screen, RED,(45-B+50*a,45+50*(6-b)), (45+B+50*(a+3), 45+50*(6-b)), breite_gewinnlinie)
                    pygame.display.flip()
                    break
                else:
                    pygame.draw.line(screen, GREEN,(45-B+50*a,45+50*(6-b)), (45+B+50*(a+3), 45+50*(6-b)), breite_gewinnlinie)
                    pygame.display.flip()
                    break

            else:
                a = a + 1

        b = b + 1

def hoch_gewinnen(B):
    
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


aktiv = True

n = 0 
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

feld_ausgabe()
pygame.display.flip()

for event in pygame.event.get():
        if event.type == pygame.QUIT:
            aktiv = False
        if n < 49:
            if event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    P = int(event.unicode)
                    if P is None or P < 1 or P > 7:
                        P = None
                    elif 8 > P > 0:
                        r = 0
                        while r < 7:
                            if feld[r][P-1] == "0":
                                
                                if n % 2 != 0:
                                    feld[r][P-1] = "T"
                                else:
                                    feld[r][P-1] = "X"

                                feld_ausgabe()
                                n = n + 1
                                r = 0
                                break
                    else:
                        r = r + 1



