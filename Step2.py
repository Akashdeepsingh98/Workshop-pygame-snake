from pygame.locals import *
from random import randint
import pygame
import time
 
class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3
 
    def __init__(self, length):
       self.length = length
	   # get 200 parts of snake in list. not all used
       for i in range(0,200):
           self.x.append(-100)
           self.y.append(-100)
 
    def update(self):
 
        	#every piece of snake will take the position of previous piece
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
 
         # update position of head of snake
        if self.direction == 0:
            self.x[0] = self.x[0] + self.step
        if self.direction == 1:
            self.x[0] = self.x[0] - self.step
        if self.direction == 2:
            self.y[0] = self.y[0] - self.step
        if self.direction == 3:
            self.y[0] = self.y[0] + self.step
 
 
    def moveRight(self):
        self.direction = 0
 
    def moveLeft(self):
        self.direction = 1
 
    def moveUp(self):
        self.direction = 2
 
    def moveDown(self):
        self.direction = 3 
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 
 
 
class App:
 
    windowWidth = 800
    windowHeight = 600
    player = 0
 
    def __init__(self):
        self._running = True
        self._displaySurf = None
        self._image_surf = None
        self.player = Player(3) 
 
    def on_init(self):
        pygame.init()
        self._displaySurf = pygame.display.set_mode((self.windowWidth,self.windowHeight))
 
        pygame.display.set_caption('Pygame snake')
        self._running = True
        self._image_surf = pygame.image.load("wssnake.png")
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        self.player.update()
        pass
 
    def on_render(self):
        self._displaySurf.fill((0,0,0))
        self.player.draw(self._displaySurf, self._image_surf)
        pygame.display.flip()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
            if (keys[K_RIGHT]):
                self.player.moveRight()
 
            if (keys[K_LEFT]):
                self.player.moveLeft()
 
            if (keys[K_UP]):
                self.player.moveUp()
 
            if (keys[K_DOWN]):
                self.player.moveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False
            self.on_loop()
            self.on_render()
 
            time.sleep (100.0 / 1000.0);
        pygame.quit()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
