import pygame, sys

pygame.init()
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
white = [255, 255, 255]
black = [0, 0, 0]
screen = pygame.display.set_mode((500, 300))
running = True
my_font = pygame.font.Font(None, 33)
text = ''
entered = ''
number = ''
letter = ''
num = 0
recty = pygame.Rect(180, 200, 140, 33)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray19')
color = color_passive
active = False
pygame.display.set_caption('Abcd')
a = pygame.image.load('a.jpg') # you need to use a full path to the file of a.jpg
pygame.display.set_icon(a)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if recty.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    text = text[0:-1]
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_RETURN:
                    entered = text
                else:
                    text += event.unicode
            elif event.key == pygame.K_ESCAPE:
                sys.exit()

    screen.fill(black)

    if active:
        color = color_active
    else:
        color = color_passive

    if len(entered) > 0:
        ent = entered.lower()
        if ent in characters:
            num = characters.index(ent)
            number = str(num + 1)
            surface2 = my_font.render(number, True, white)
            screen.blit(surface2, (250, 110))
        elif entered.isdigit and len(entered) < 3:
            try:
                num = int(entered)
                if num <= len(characters) + 1:
                    if characters[int(num) - 1] in characters:
                        letter = characters[int(num) - 1]
                        surface3 = my_font.render(letter, True, white)
                        screen.blit(surface3, (250, 110))
            except:
                pass

    pygame.draw.rect(screen, color, recty, 2)
    surface = my_font.render(text, True, white)
    screen.blit(surface, (recty.x + 5, recty.y + 5))
    recty.w = max(130, surface.get_width() + 10)

    pygame.display.update()
