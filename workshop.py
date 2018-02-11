from pygame.locals import *
from random import randint
import pygame
import time

class Apple:
    x = 0
    y = 0
	#'step' is just the step size in pixels
	#prefer to keep it 44 as the images are 44X44
    step = 44
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 
  
class Player:
    # lists of x and y coordinates of each snake square
    x = [0]
    y = [0]
    step = 44
	#0 for right,1 for left,2 for up, 3 for down
    direction = 0
    length = 3

    def __init__(self, length):
       self.length = length
	   # get 200 parts of snake in list. not all used
       for i in range(0,200):
           self.x.append(-100)
           self.y.append(-100)
 
       # initial positions, no collision.
       for i in range(1,self.length-1):
           self.x[i] = i*self.step
 
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
 
class Collision:
    def isCollision(self,x1,y1,x2,y2,size):
        if x1 == x2 and y1 == y2:
            #if y1 + size >= y2 and y1 <= y2 + size:
            return True
        return False
		
    def WallCollision(self,x,y,windowWidth,windowHeight,size):
        if x > windowWidth or x < 0 or y > windowHeight or y < 0:
            return True
        return False
 
class App:
# this is the entire game app. The main thing.
    windowWidth = 800
    windowHeight = 600
    player = 0
    apple = 0
 
    def __init__(self):
		# is game running?
        self._running = True
		#game display object
        self._display = None
		#snake image
        self._snakeimg = None
		# apple image
        self._appleimg = None
		#object to keep collision in check
        self.game = Collision()
		#passing the initial length of snake and initial positions steps of apple
        self.player = Player(3)
        self.apple = Apple(5,5)

    def on_init(self):
	#on initialization of game
        pygame.init()
        self._display = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('Pygame Snake')
        self._running = True
        self._snakeimg = pygame.image.load("wssnake.png")
        self._appleimg = pygame.image.load("wsapple.png")

    def on_loop(self):
        self.player.update()
 
        # does apple spawn on snake's body?
        for i in range(0,self.player.length):
            if self.game.isCollision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],self.player.step):
                self.apple.x = randint(2,9) * self.apple.step
                self.apple.y = randint(2,9) * self.apple.step
                self.player.length = self.player.length + 1
		
		# does snake eat apple?
        if self.game.isCollision(self.apple.x,self.apple.y,self.player.x[0], self.player.y[0],self.player.step):
                self.apple.x = randint(2,9) * self.apple.step
                self.apple.y = randint(2,9) * self.apple.step
                self.player.length = self.player.length + 1
 
		# does snake collide with itself?
        for i in range(2,self.player.length):
            if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],self.player.step-10):
                print("You lose! Collided with self! ")
                exit(0)
				
		# does snake collide with wall?
        if self.game.WallCollision(self.player.x[0],self.player.y[0],self.windowWidth,self.windowHeight,self.player.step):
            print("Collided with wall!")
            exit(0)

    def on_render(self):
        self._display.fill((0,0,0))
        self.player.draw(self._display, self._snakeimg)
        self.apple.draw(self._display, self._appleimg)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
	## this line will call the on_init and start pygame
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
            # control the speed
            time.sleep (100.0 / 1000.0);
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()