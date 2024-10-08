import pygame
from platform import system

if system() == "Windows":
    normalfontsize = 22
    normalfontstyle = 'Arial'
    bigfontsize = 42
    bigfontstyle = 'Arial'
else:
    smallfontsize = 22
    smallfontstyle = 'Liberation Sans'
    normalfontsize = 22
    normalfontstyle = 'Liberation Sans'
    bigfontsize = 42
    bigfontstyle = 'dgjahkjgldakljg'

class TextBox:

    def __init__(self, x, y, w, h, text=''):
        # Main
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (0, 0, 0)
        self.text = text
        self.manuallyWritten = False
        self.fontstyle=pygame.font.SysFont(normalfontstyle,normalfontsize)
        self.txt_surface = self.fontstyle.render(text, True, self.color)
        self.active = True

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = (0, 0, 0) if self.active else (150, 150, 150)

        if event.type == pygame.KEYDOWN or self.manuallyWritten == True:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) != 72:
                        self.text += event.unicode

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

        self.txt_surface = self.fontstyle.render(self.text, True, self.color)

    def writeinto(self, text):
        if len(text) != 0:
            self.text += text

    def replacewith(self, text):
        self.text = text

    def backspace(self):
        self.text = self.text[:-1]

    def clearbox(self):
        self.text = ''