import pygame, sys

pygame.init()
slova = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
white = [255, 255, 255]
black = [0, 0, 0]
screen = pygame.display.set_mode((500, 300))
running = True
moj_font = pygame.font.Font(None, 33)
tekstic = ''
entered = ''
broj = ''
slovo = ''
brj = 0
rektic = pygame.Rect(180, 200, 140, 33)
bojanka_aktivna = pygame.Color('lightskyblue3')
bojanka_pasivna = pygame.Color('gray19')
bojanka = bojanka_pasivna
aktivno = False
pygame.display.set_caption('Abcd')
a = pygame.image.load('C:/Users/ogica/Codes/NaKomJeMestu/a.jpg')
pygame.display.set_icon(a)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rektic.collidepoint(event.pos):
                aktivno = True
            else:
                aktivno = False
        if event.type == pygame.KEYDOWN:
            if aktivno == True:
                if event.key == pygame.K_BACKSPACE:
                    tekstic = tekstic[0:-1]
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_RETURN:
                    entered = tekstic
                else:
                    tekstic += event.unicode
            elif event.key == pygame.K_ESCAPE:
                sys.exit()

    screen.fill(black)

    if aktivno:
        bojanka = bojanka_aktivna
    else:
        bojanka = bojanka_pasivna

    if len(entered) > 0:
        ent = entered.lower()
        if ent in slova:
            br = slova.index(ent)
            broj = str(br + 1)
            surfejs2 = moj_font.render(broj, True, white)
            screen.blit(surfejs2, (250, 110))
        elif entered.isdigit and len(entered) < 3:
            try:
                brj = int(entered)
                if brj <= len(slova) + 1:
                    if slova[int(brj) - 1] in slova:
                        slovce = slova[int(brj) - 1]
                        surfejs3 = moj_font.render(slovce, True, white)
                        screen.blit(surfejs3, (250, 110))
            except:
                pass

    pygame.draw.rect(screen, bojanka, rektic, 2)
    surfejs = moj_font.render(tekstic, True, white)
    screen.blit(surfejs, (rektic.x + 5, rektic.y + 5))
    rektic.w = max(130, surfejs.get_width() + 10)

    pygame.display.update()