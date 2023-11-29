import pygame
from pygame import mixer

pygame.init()

loop = True
screen = pygame.display.set_mode((500,500))

class Josh:
    def __init__(self,screen, x=0, y=100, move_x=2, move_y=2, size = 100) -> None:
        self.screen = screen
        self.size = size
        self.X = x
        self.Y = y
        self.move_x = move_x
        self.move_y = move_y
    
    def double_josh(self):
        self.move_x = -1.3*self.move_x
        self.move_y = -1.3*self.move_y
        if self.X >= (500-self.size) or self.X <= 0:
            josh_list.append(Josh(self.screen, self.X, self.Y, self.move_x, -self.move_y))
        elif self.Y > (500-self.size) or self.Y <= 0:
            josh_list.append(Josh(self.screen, self.X, self.Y, -self.move_x, self.move_y))
        mixer.init()
        mixer.music.load('whistle.mp3')
        mixer.music.set_volume(1)
        mixer.music.play()

    def check_double(self):
        if self.X > (500-self.size) or self.X < 0 or self.Y > (500-self.size) or self.Y < 0:
            self.double_josh()

    def update(self):
        pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(self.X, self.Y, self.size, self.size))
        self.X = self.X + self.move_x
        self.Y = self.Y + self.move_y
        josh = pygame.transform.scale(pygame.image.load('josh.jpg'), (self.size,self.size))
        self.screen.blit(josh, (self.X, self.Y))


josh_list = [Josh(screen)]

make_more = False

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    for j in josh_list:
        j.update()
        if make_more:
            j.check_double()
            #make_more = False
    make_more = True
    pygame.display.update()
    
    