import pygame
class up():
    def __init__(self,width,height,title='runergame',blit=0,fill=0):
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption(title)
        self.blit = blit
        self.fill = fill
        self.runing = True
        self.all_sprites = pygame.sprite.Group()
    def run(self):
        while self.runing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runing = False
            if self.blit == 0:
                self.screen.fill(self.fill)
            else:
                self.screen.blit(self.blit,(0,0))
            self.all_sprites.draw(self.screen)
            pygame.display.update()
    def running(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runing = False
        if self.blit == 0:
            self.screen.fill(self.fill)
        else:
            self.screen.blit(self.blit,(0,0))
        self.all_sprites.draw(self.screen)
    def testue(self,classe):
        self.all_sprites.add(classe)