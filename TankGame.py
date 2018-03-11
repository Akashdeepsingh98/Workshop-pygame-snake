import pygame
import random
pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 155, 0)
yellow = (200, 200, 0)
light_green = (0, 255, 0)
light_yellow = (255, 255, 0)
light_red = (255, 0, 0)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tanks')
clock = pygame.time.Clock()
FPS = 30
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)
tankWidth = 40
tankHeight = 20
turretWidth = 5
wheelWidth=5
ground_height=display_height*0.1-tankHeight-wheelWidth
#                                                                                   tank function
def tank(x, y,turpos):
    x = int(x)
    y = int(y)
    possTurrets=[(x-27,y-2),(x-26,y-5),(x-25,y-8),(x-23,y-12),(x-20,y-14),(x-18,y-15),(x-15,y-17),(x-13,y-19),(x-11,y-21)]
    pygame.draw.circle(gameDisplay, black, (x, y), int(tankHeight/2))
    pygame.draw.rect(gameDisplay, black, (x-tankWidth/2, y, tankWidth, tankHeight))
    pygame.draw.line(gameDisplay,black,(x,y),possTurrets[turpos],turretWidth)
    startX=15
    for i in range(7):
        pygame.draw.circle(gameDisplay,black,(x-startX,y+20),wheelWidth)
        startX-=5
    return possTurrets[turpos]
#                                                                                       Enemy tank function
def Enemy_tank(x, y,turpos):
    x = int(x)
    y = int(y)
    possTurrets=[(x+27,y-2),(x+26,y-5),(x+25,y-8),(x+23,y-12),(x+20,y-14),(x+18,y-15),(x+15,y-17),(x+13,y-19),(x+11,y-21)]
    pygame.draw.circle(gameDisplay, black, (x, y), int(tankHeight/2))
    pygame.draw.rect(gameDisplay, black, (x-tankWidth/2, y, tankWidth, tankHeight))
    pygame.draw.line(gameDisplay,black,(x,y),possTurrets[turpos],turretWidth)
    startX=15
    for i in range(7):
        pygame.draw.circle(gameDisplay,black,(x-startX,y+20),wheelWidth)
        startX-=5
    return possTurrets[turpos]
#                                                                                       game menu controls section function
def game_controls():
    controls = True
    while controls:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        message_to_screen("Controls", green, -100, "large")
        message_to_screen("Fire : Spacebar", black, -30)
        message_to_screen("Move Turret : Up and Down arrows", black, 10)
        message_to_screen("Move Tank : Left and Right arrows", black, 50)
        message_to_screen("Pause : P", black, 90)
        button("Play", 150, 500, 100, 50, green, light_green, "play")
        button("Main", 350, 500, 100, 50, yellow, light_yellow, "main")
        button("Quit", 550, 500, 100, 50, red, light_red, "quit")
        pygame.display.update()
#                                                                                               text_to_button function
def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight,
                   size="small"):
    textSurf, textRect = text_object(msg, color, size)
    textRect.center = (buttonx+buttonwidth/2, buttony+buttonheight/2)
    gameDisplay.blit(textSurf, textRect)
#                                                                                               text_object function
def text_object(msg, color, size):
    if size == "small":
        textSurface = smallfont.render(msg, True, color)
    elif size == "medium":
        textSurface = medfont.render(msg, True, color)
    elif size == "large":
        textSurface = largefont.render(msg, True, color)
    return textSurface, textSurface.get_rect()
#                                                                                       message to screen function
def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_object(msg, color, size)
    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)
#                                                                                           game intro function
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    intro = False
                    GameLoop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    intro = False
                    game_controls()
        gameDisplay.fill(white)
        message_to_screen("Welcome to Tanks", green, -100, "large")
        message_to_screen("The objective is shoot and destroy", black, -30)
        message_to_screen("the enemy tanks before they destroy you", black, 10)
        message_to_screen("The more enemies you destroy, the harder they get",black, 50)
        button("Play", 150, 500, 100, 50, green, light_green, "play")
        button("Controls", 350, 500, 100, 50, yellow, light_yellow, "controls")
        button("Quit", 550, 500, 100, 50, red, light_red, "quit")
        pygame.display.update()
#                                                                                                   Game over
def game_over():
    gameover = True
    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameover = False
                    GameLoop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    gameover = False
                    game_controls()
        gameDisplay.fill(white)
        message_to_screen("Game Over", green, -100, "large")
        message_to_screen("You Died!", black, -30)
        button("Play Again", 150, 500, 150, 50, green, light_green, "play")
        button("Controls", 350, 500, 100, 50, yellow, light_yellow, "controls")
        button("Quit", 550, 500, 100, 50, red, light_red, "quit")
        pygame.display.update()
def you_win():
    win = True
    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        message_to_screen("You won!", green, -100, "large")
        message_to_screen("Congratulations", black, -30)
        button("Play Again", 150, 500, 150, 50, green, light_green, "play")
        button("Controls", 350, 500, 100, 50, yellow, light_yellow, "controls")
        button("Quit", 550, 500, 100, 50, red, light_red, "quit")
        pygame.display.update()
#                                                                                                           score function
def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0, 0])
#                                                                                                           pause function
def pause():
    message_to_screen("Paused", black, -100, "large")
    message_to_screen("Press C to continue, P to pause or Q to quit",black, 25)
    pygame.display.update()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
#                                                                                                                   barrier fucntion
def barrier(xloc,randomHeight,barrierWidth):
    pygame.draw.rect(gameDisplay,black,[xloc,display_height-randomHeight,barrierWidth,randomHeight])
#                                                                                                           explosion function
def explosion(x,y,size=50):
    explode=True
    colorchoices=[red,light_red,yellow,light_yellow]
    startpoint=x,y
    while explode:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        magnitude=1
        while magnitude<size:
            explodingBitX=x+random.randrange(-1*magnitude,magnitude)
            explodingBitY=y+random.randrange(-1*magnitude,magnitude)
            pygame.draw.circle(gameDisplay,colorchoices[random.randrange(0,4)],(explodingBitX,explodingBitY),random.randrange(1,5))
            magnitude+=1
            pygame.display.update()
            clock.tick(100)
        explode=False
#                                                                                                       fireshell function
def fireShell(xy,tankx,tanky,turpos,gunpower,barrierX,barrierWidth,wallHeight,enemy_tankx,enemy_tanky):
    fire=True
    startingShell=[xy[0],xy[1]]
    damage=0
    while fire:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(gameDisplay,red,(startingShell[0],startingShell[1]),5)
        startingShell[0]-=(12-turpos)**2
        startingShell[1]+=int(((startingShell[0]-xy[0])*0.015/(gunpower/50))**2 - (turpos+turpos/(12-turpos)))
#       has shell hit the ground?
        if startingShell[1]>display_height-ground_height:
            fire=False
            hit_x=int((startingShell[0]*display_height-ground_height)/startingShell[1])
            hit_y=int(display_height-ground_height)
            if enemy_tankx+15>hit_x>enemy_tankx-15:
                damage=25
            explosion(hit_x,hit_y)
#       barrier check
        checkX1=startingShell[0]<=barrierX+barrierWidth
        checkX2=startingShell[0]>=barrierX
        checkY1=startingShell[1]<=display_height
        checkY2=startingShell[1]>=display_height-wallHeight
        if checkX1 and checkX2 and checkY1 and checkY2:
            fire=False
            hit_x=int(startingShell[0])
            hit_y=int(startingShell[1])
            explosion(hit_x,hit_y)
        pygame.display.update()
        clock.tick(50)
    return damage
#                                                                                                       Enemy fireshell
def Enemy_fireShell(xy,tankx,tanky,turpos,gunpower,barrierX,barrierWidth,wallHeight,p_tankx,p_tanky):
    damage=0
    current_power=1
    power_found=False
    hit_x=0
    hit_y=0
    while not power_found:
        current_power+=1
        if current_power>300:
           power_found=True
        fire=True
        startingShell=[xy[0],xy[1]]
        while fire:
            startingShell[0]+=(12-turpos)**2
            startingShell[1]+=int(((startingShell[0]-xy[0])*0.015/(current_power/50))**2 - (turpos+turpos/(12-turpos)))
            hit_x=int((startingShell[0]*(display_height-ground_height))/startingShell[1])
            hit_y=int(display_height-ground_height)
            if p_tankx+15>hit_x>p_tankx-15:
                power_found=True
                fire=False
            if startingShell[1]>display_height-ground_height:
                fire=False
            checkX1=startingShell[0]<=barrierX+barrierWidth
            checkX2=startingShell[0]>=barrierX
            checkY1=startingShell[1]<=display_height
            checkY2=startingShell[1]>=display_height-wallHeight
            if checkX1 and checkX2 and checkY1 and checkY2:
                fire=False
    startingShell=[xy[0],xy[1]]
    fire=True
    while fire:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(gameDisplay,red,(startingShell[0],startingShell[1]),5)
        startingShell[0]+=(12-turpos)**2
        startingShell[1]+=int(((startingShell[0]-xy[0])*0.015/(current_power/50))**2 - (turpos+turpos/(12-turpos)))
        if startingShell[1]>display_height-ground_height:
            hit_x=int((startingShell[0]*(display_height-ground_height))/startingShell[1])
            if p_tankx+15>hit_x>p_tankx-15:
                print(hit_x)
                damage=25
            fire=False
            explosion(hit_x,hit_y)
        checkX1=startingShell[0]<=barrierX+barrierWidth
        checkX2=startingShell[0]>=barrierX
        checkY1=startingShell[1]<=display_height
        checkY2=startingShell[1]>=display_height-wallHeight
        if checkX1 and checkX2 and checkY1 and checkY2:
            fire=False
            hit_x=int(startingShell[0])
            hit_y=int(startingShell[1])
            explosion(hit_x,hit_y)
        pygame.display.update()
        clock.tick(50)
    print(hit_x)
    print(damage)
    return damage
#                                                                                           power of shell function
def power(level):
    text=smallfont.render("Power: "+str(level)+"%",True,black)
    gameDisplay.blit(text,[display_width/2,0])
#                                                                                           healthbar
def health_bars(player_health,enemy_health):
    if player_health>75:
        player_health_color=green
    elif player_health>50:
        player_health_color=yellow
    elif player_health>0:
        player_health_color=red
    else:
        player_health=0
        player_health_color=white
    if enemy_health>75:
        enemy_health_color=green
    elif enemy_health>50:
        enemy_health_color=yellow
    elif enemy_health>0:
        enemy_health_color=red
    else:
        enemy_health=0
        enemy_health_color=white
    pygame.draw.rect(gameDisplay,player_health_color,(680,25,player_health,25))
    pygame.draw.rect(gameDisplay,enemy_health_color,(20,25,enemy_health,25))
#                                                                                                   the main gameloop fucntion
def GameLoop():
    gameExit = False
    gameOver = False
    mainTankX = display_width*0.9
    mainTankY = display_height*0.9
# Starting position of main Tank
    player_health=100
    enemy_health=100
    currentTurPos=0
    changeTur=0
    tankMove=0
    xloc=display_width/2+random.randint(-0.1*display_width,0.1*display_width)
    randomHeight=random.randrange(display_height*0.1,display_height*0.6)
    barrierWidth=50
    firepower=50
    powerchange=0
    enemyTankX = display_width*0.1
    enemyTankY = display_height*0.9
    while not gameExit:
        if gameOver is True:
            message_to_screen("Game over.", black, -50, "large")
            message_to_screen("Press C to play again or Q to quit", red, 50,
                              "medium")
            pygame.display.update()
        while gameOver == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        GameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove=-5
                elif event.key == pygame.K_RIGHT:
                    tankMove=5
                elif event.key == pygame.K_UP:
                    changeTur=1
                elif event.key == pygame.K_DOWN:
                    changeTur=-1
                elif event.key == pygame.K_p:
                    pause()
                elif event.key==pygame.K_SPACE:
                    damage=fireShell(gun,mainTankX,mainTankY,currentTurPos,firepower,xloc,barrierWidth,randomHeight,enemyTankX,enemyTankY)
                    enemy_health-=damage
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                tankMove=-5
                            elif event.key == pygame.K_RIGHT:
                                tankMove=5
                            elif event.key == pygame.K_UP:
                                changeTur=1
                            elif event.key == pygame.K_DOWN:
                                changeTur=-1
                    damage=Enemy_fireShell(enemy_gun,enemyTankX,enemyTankY,8,firepower,xloc,barrierWidth,randomHeight,mainTankX,mainTankY)
                    player_health-=damage
                elif event.key == pygame.K_a:
                    powerchange=-1
                elif event.key==pygame.K_d:
                    powerchange=1
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT):
                    tankMove=0
                if event.key == pygame.K_UP or event.key==pygame.K_DOWN:
                    changeTur=0
                if event.key == pygame.K_a or event.key==pygame.K_d:
                    powerchange=0
        mainTankX+=tankMove
        currentTurPos+=changeTur
        if currentTurPos>8:
            currentTurPos=8
        elif currentTurPos<0:
            currentTurPos=0
        if mainTankX-tankWidth/2<xloc+barrierWidth:
            mainTankX+=5
        gameDisplay.fill(white)
        health_bars(player_health,enemy_health)
        gun=tank(mainTankX, mainTankY,currentTurPos)
        enemy_gun=Enemy_tank(enemyTankX,enemyTankY,8)
        firepower+=powerchange
        power(firepower)
        barrier(xloc,randomHeight,barrierWidth)
        gameDisplay.fill(green,rect=[0,display_height-ground_height,display_width,ground_height])
        pygame.display.update()
        if player_health<1:
            game_over()
        elif enemy_health<1:
            you_win()
        clock.tick(FPS)
    pygame.quit()
    quit()
#                                                                                               button function
def button(text, x, y, width, height, in_color, color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > cur[0] > x and y+height > cur[1] > y:
        pygame.draw.rect(gameDisplay, color, (x, y, width, height))
        if click[0] is 1 and action is not None:
            if action is "quit":
                pygame.quit()
            if action is "controls":
                game_controls()
            if action is "play":
                GameLoop()
            if action is "main":
                game_intro()
    else:
        pygame.draw.rect(gameDisplay, in_color, (x, y, width, height))
    text_to_button(text, black, x, y, width, height)
game_intro()