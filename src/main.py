"""Name: Jerry Wu
DUE: MAY 29TH 2018
Description: ICS SUMMATIVE GAME PROJECT, 
This game is a shoot em up game based mostly on RNG. The goal of this game is to survive for as long as possible, while killing aliens that shoot at you, and dodging meteors that go in random directions, collect powerups that are randomly dropped. There are a variety of powerups to pick up over the course of the game. There are 2 powerups avalible; healthpacks and 1ups. There will be more powerups added in the future, but not for this assignment.
Controls: Left mouse button to shoot, mouse to move, space to shoot, arrow keys to move around"""
import pygame, classes, random #Import pygame library and initialize modules within library
pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 1, 512) #make sure there is no delay in sound playing by pre initializing the sound module
def menu():
    '''This function creates the main menu'''
    screen = pygame.display.set_mode((640, 480)) #Display
    pygame.display.set_caption("MAIN MENU") #window title
    menuicon = pygame.image.load("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\MISC\\menuicon.png")
    pygame.display.set_icon(menuicon) #main menu ico
    pygame.mixer.music.load("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\SFX\\menumusic2.ogg")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1) #set music to play on infinite loop
    background = pygame.image.load("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\MISC\\menu.png")
    font = pygame.font.Font("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\FONTS\\font2.ttf", 25)
    message1 = "MAIN MENU" #main menu text render
    message2 = "Welcome to the dank version of Star Wars"
    message3 = "Press space or left mouse button to start"
    message4 = "Press esc to exit"
    message5 = "Btw press p to pause if you need a break"
    difficulty1 = "1: Easy"
    difficulty2 = "2: Normal"
    difficulty3 = "3: Hard"
    difficulty4 = "4: HELL"
    menuTextln1 = font.render(message1, 1, (0,255,0)) #render array of text onto screen
    menuTextln2 = font.render(message2, 1, (255,0,0))
    menuTextln3 = font.render(message3, 1, (0,0,255))
    menuTextln4 = font.render(message4, 1, (255,0,255))
    menuTextln5 = font.render(message5, 1, (255,255,255))
    clock = pygame.time.Clock()
    inMenu = True

    while inMenu: #loop
        pygame.mouse.set_visible(False) #set mouse to be invisible
        clock.tick(60)
        for event in pygame.event.get(): #event handling
            if event.type is pygame.QUIT:
                pygame.mixer.music.fadeout(1000)
                pygame.quit()
            if event.type is pygame.KEYDOWN:
                if event.key is pygame.K_SPACE:
                    pygame.mixer.music.fadeout(1000)
                    inMenu = False
                if event.key is pygame.K_ESCAPE:
                    pygame.mixer.music.fadeout(1000)
                    pygame.quit()
            if event.type is pygame.MOUSEBUTTONDOWN:
                if event.button is 1:
                    pygame.mixer.music.fadeout(1000)
                    inMenu = False
        screen.blit(background, (0,0)) #refresh screen
        screen.blit(menuTextln1, (screen.get_width()/2-80, 20))
        screen.blit(menuTextln2, (screen.get_width()/2-300, 120))
        screen.blit(menuTextln3, (screen.get_width()/2-300, 220))
        screen.blit(menuTextln4, (screen.get_width()/2-130, 320))
        screen.blit(menuTextln5, (screen.get_width()/2-300, 420))
        pygame.display.flip()

def pauseScreen():
    '''This method is callled when the user wants to pause'''
    pygame.mixer.music.pause()
    screen = pygame.display.set_mode((640, 720)) #set screen size
    clock = pygame.time.Clock() #make clock
    pygame.display.set_caption("PAUSED, Press 'p' to un pause") #caption
    background = pygame.image.load("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\MISC\\pauseimage.png") #load image
    pausefont = pygame.font.Font("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\FONTS\\font2.ttf", 50) #set font for the pause screen
    message1 = "PAUSED"
    message2 =  "Press 'p' to un pause"
    pausemessageln1 = pausefont.render(message1, 1, (255,255,0))
    pausemessageln2 = pausefont.render(message2, 1, (255,0,0))
    paused = True #loop
    while paused:
        for event in pygame.event.get(): #event handling
            if event.type is pygame.QUIT:
                pygame.quit()
            if event.type is pygame.KEYDOWN:
                if event.key is pygame.K_p:
                    pygame.display.set_caption("Ghetto star wars.exe")
                    paused = False
                elif event.key is pygame.K_ESCAPE:
                    pygame.quit()
        screen.blit(background, (0,0)) #show everything on the screen
        screen.blit(pausemessageln1, (screen.get_width()/2-110, screen.get_height()/2-80))
        screen.blit(pausemessageln2, (screen.get_width()/2-300, screen.get_height()/2+40))
        pygame.display.update()
        pygame.display.flip()
    pygame.mixer.music.unpause()

def respawnScreen():
    '''This method is callled when the user wants to pause'''
    screen = pygame.display.set_mode((640, 720)) #set screen size
    pygame.display.set_caption("YOU DIED! Press any key to respawn") #caption
    background = pygame.image.load("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\MISC\\background.png") #load image
    pausefont = pygame.font.Font("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\FONTS\\font2.ttf", 30) #set font for the pause screen
    message1 = "YOU DIED!"
    message2 =  "Press any key to respawn"
    pausemessageln1 = pausefont.render(message1, 1, (255,255,0))
    pausemessageln2 = pausefont.render(message2, 1, (255,0,0))
    dead = True #loop
    while dead:
        for event in pygame.event.get(): #event handling
            if event.type is pygame.QUIT:
                pygame.quit()
            if event.type is pygame.KEYDOWN:
                pygame.display.set_caption("Ghetto star wars.exe")
                dead = False
            if event.type is pygame.MOUSEBUTTONDOWN:
                pygame.display.set_caption("Ghetto star wars.exe")
                dead = False            
        screen.blit(background, (0,0)) #show everything on the screen
        screen.blit(pausemessageln1, (screen.get_width()/2-80, screen.get_height()/2-80))
        screen.blit(pausemessageln2, (screen.get_width()/2-200, screen.get_height()/2+40))
        pygame.display.update()
        pygame.display.flip()

def main():
    '''Main function, this is where all the good stuff happens'''
    screen = pygame.display.set_mode((640, 720)) #Display
    pygame.display.set_caption("Ghetto star wars.exe") #window title
    mainicon = pygame.image.load("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\MISC\\icon.png")
    pygame.display.set_icon(mainicon)
    pygame.mixer.music.load("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\SFX\\music.ogg") #star wars space battle theme, i think thats what its called
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1) #play music in infinite loop
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,0)) #make blank surface to put scrolling background on
    space = classes.Background(screen, 8) #make background scroll at 8 p/s
    player = classes.Player(screen, screen.get_height()/2, screen.get_width()/2) #ENTITIES
    score = 0 #set initial score to 0
    health = 100 #set initial HP to 100
    lives = 5 #set initial life number to 5
    scorekeeper = classes.Scorekeeper(score) #create scorekeeper
    lifekeeper = classes.Lifekeeper(lives) #create lifekeeper
    healthkeeper = classes.Healthkeeper(health) #create healthkeeper
    fire = pygame.mixer.Sound("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\SFX\\fire.ogg") #load sounds
    explosion = pygame.mixer.Sound("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\SFX\\explosion.ogg")
    death = pygame.mixer.Sound("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\SFX/death.ogg")
    gameOverSound = pygame.mixer.Sound("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\SFX\\gameover.ogg")
    healthPackSound = pygame.mixer.Sound("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\SFX\\healthpack.ogg")
    extraLifeSound = pygame.mixer.Sound("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\SFX\\1up.ogg")
    fire.set_volume(0.2) #set volume of sounds
    explosion.set_volume(0.8)
    death.set_volume(1)
    healthPackSound.set_volume(1)
    extraLifeSound.set_volume(0.5)
    meteors = pygame.sprite.Group() #make a group of meteors
    aliens = pygame.sprite.Group()
    bullets = pygame.sprite.Group() #make an empty group of bullets
    healthpacks = pygame.sprite.Group()
    extraLives = pygame.sprite.Group()
    enemybullets = pygame.sprite.Group()
    for meteor in range(25): #create 25 meteors
        meteor = classes.Meteor(screen, random.randint(0,screen.get_width()), random.randint(-5000, -1000))
        meteors.add(meteor)
    for alien in range(10): #create 10 aliens
        alien = classes.Alien(screen, random.randint(-4,4), random.randint(1,8), random.randint(50, screen.get_width()-50), random.randint(-5000,-1000), random.randint(100, screen.get_height()/2 +100))
        aliens.add(alien)
    allSprites = pygame.sprite.OrderedUpdates(space, player, meteors, aliens, scorekeeper, lifekeeper, healthkeeper, bullets, healthpacks, extraLives) #make sprite order group
    clock = pygame.time.Clock()
    running = True
    #ACTION
    while running: #loop
        pygame.mouse.set_visible(False) #set mouse to be invisible
        clock.tick(60) #60FPS, time
        playerflame1 = classes.Flame((player.rect.centerx-25, player.rect.centery+player.rect.height/2)) #add spaceship trails
        playerflame2 = classes.Flame((player.rect.centerx+25, player.rect.centery+player.rect.height/2))
        playerflame3 = classes.Flame((player.rect.centerx, player.rect.centery+player.rect.height/2 +10))
        allSprites.add(playerflame1)
        allSprites.add(playerflame2)
        allSprites.add(playerflame3)
        RNG = random.randrange(1000) #RANDOM NUMBER GENERATOR
        ENEMY_RNG_CASES = (666,555,324,647,416,53,17,39,199,85) #make 10 cases where the enemy will shoot
        for meteor in meteors: #add meteor trails
            meteorflame = classes.Flame((meteor.rect.centerx,meteor.rect.centery-20))
            allSprites.add(meteorflame)
        for event in pygame.event.get(): #events
            if event.type is pygame.QUIT:
                scorekeeper.kill() #if lives is 0 then game ends
                healthkeeper.kill() #kill all sprites when game ends
                lifekeeper.kill()
                player.kill()
                for meteor in meteors:
                    meteor.kill()
                pygame.mixer.music.fadeout(1000)
                running = False #break out of loop
            if event.type is pygame.MOUSEMOTION: #mouse controls
                if pygame.mouse.get_pos()[0] < screen.get_width() or pygame.mouse.get_pos()[0] > 0:
                    player.rect.centerx = pygame.mouse.get_pos()[0]
                if pygame.mouse.get_pos()[1] < screen.get_height() or pygame.mouse.get_pos()[1] > 0:
                    player.rect.centery = pygame.mouse.get_pos()[1]
            if event.type is pygame.MOUSEBUTTONDOWN:
                if event.button is 1: #if left mouse button is pressed then fire
                    bullet = classes.Bullet(player.get_pos())
                    bullets.add(bullet)
                    for bullet in bullets:
                        bullet.fire(15) #set bullet speed to 15
                        fire.play(0) #play fire sound
                        allSprites.add(bullet) #put bullet on screen
            if event.type is pygame.KEYDOWN: 
                if event.key is pygame.K_p:
                    pauseScreen()
                if event.key is pygame.K_SPACE:
                    bullet = classes.Bullet(player.get_pos())
                    bullets.add(bullet)
                    for bullet in bullets:
                        bullet.fire(15) #set bullet speed to 15
                        fire.play(0) #play fire sound
                        allSprites.add(bullet) #put bullet on screen                   
        keyspressed = pygame.key.get_pressed()
        player.change_direction((0,0))
        if keyspressed[pygame.K_UP]:
            player.change_direction((0,-1))
        if keyspressed[pygame.K_LEFT]:
            player.change_direction((-1,0))
        if keyspressed[pygame.K_DOWN]:
            player.change_direction((0,1))
        if keyspressed[pygame.K_RIGHT]:
            player.change_direction((1,0))              
        if RNG is 43 and healthkeeper.get_health() < 100: #random spawning of healthpack powerup, check if player has less than 100 hp
            healthpack = classes.Healthpack(screen, random.randint(50,screen.get_width()-50), 0, random.randint(5,10)) #make healthpack object
            healthpacks.add(healthpack)
            allSprites.add(healthpack)
        if RNG is 68 and lifekeeper.get_lives() < 5: #random spawning of 1up powerup #check if player has less than 5 lives
            extraLife = classes.Extralife(screen, random.randint(50,screen.get_width()-50), 0, random.randint(5,10))
            extraLives.add(extraLife)
            allSprites.add(extraLife)
        for healthpack in healthpacks: #check if player hits powerup
            if player.rect.colliderect(healthpack.rect) and healthkeeper.get_health() < 100:
                allSprites.remove(healthpack)
                healthkeeper.healthup(10)
                healthpack.kill()
                healthpacks.remove(healthpack) #remove healthpack from collision group
                healthPackSound.play(0)
                scorekeeper.player_scored(200) #give player 200 points
            if player.rect.colliderect(healthpack.rect) and healthkeeper.get_health() >= 100:
                allSprites.remove(healthpack)
                healthkeeper.healthup(0)
                healthpack.kill() #remove healthpack from collision group
                healthpacks.remove(healthpack)
                healthPackSound.play(0)
                healthkeeper.set_health(100) #make sure health stays at 100 and doesnt go over
                scorekeeper.player_scored(200) #give player 200 points
        for extraLife in extraLives:
            if player.rect.colliderect(extraLife.rect) and lifekeeper.get_lives() < 5:
                allSprites.remove(extraLife)
                lifekeeper.life_gain(1)
                extraLife.kill()
                extraLives.remove(extraLife)
                extraLifeSound.play(0)
                scorekeeper.player_scored(200) #give player 200 points
            if player.rect.colliderect(extraLife.rect) and lifekeeper.get_lives() >= 5:
                allSprites.remove(extraLife)
                lifekeeper.life_gain(0)
                extraLife.kill()
                extraLives.remove(extraLife)
                extraLifeSound.play(0)
                lifekeeper.set_lives(5)
                scorekeeper.player_scored(200) #give player 200 points
        if healthkeeper.get_health() > 100:
            healthkeeper.set_health(100) #make sure health stays at 100 and doesnt go over
        if lifekeeper.get_lives() > 5:
            lifekeeper.set_lives(5) #make sure lives stay at 5 and doesnt go over
        for meteor in meteors:
            if player.rect.inflate(-60,-60).colliderect(meteor.rect) and not meteor.exploding() and not player.exploding(): #check if player is exploding
                explosion.play(0) #play explosion once
                scorekeeper.player_scored(random.randint(1,20)) #add random number of points to scorekeeper
                healthkeeper.take_damage(random.randint(1,10)) #take off 10 health points
                meteor.killed()
                meteor.exploding()
            for bullet in bullets:
                if bullet.rect.colliderect(meteor.rect) and not meteor.exploding(): #check if meteor is exploding
                    explosion.play(0) #blow it up
                    bullet.kill() #kill bullet when it hits
                    scorekeeper.player_scored(random.randint(1,20)) #increase the score by 10
                    bullets.remove(bullet)
                    meteor.killed()
                    meteor.exploding()
        for alien in aliens: #collission detection for aliens
            if player.rect.inflate(-60,-60).colliderect(alien.rect) and not alien.exploding() and not player.exploding():
                explosion.play(0)
                scorekeeper.player_scored(random.randint(25,50))
                healthkeeper.take_damage(random.randint(10,15))
                alien.killed()
                alien.exploding()
            for bullet in bullets: #check if bullet hits alien in group
                if bullet.rect.colliderect(alien.rect) and not alien.exploding(): #check if alien is exploding
                    alien.take_damage()
                    bullet.kill()
                    bullets.remove(bullet)                    
                    if alien.get_health() is 0:
                        explosion.play(0)
                        scorekeeper.player_scored(random.randint(100,150))
                        alien.killed()
                        alien.exploding()
            if (RNG in ENEMY_RNG_CASES) and (alien.rect.bottom > 0) and not alien.exploding(): #check if RNG chooses these numbers to make enemies shoot
                enemybullet = classes.EnemyBullet(screen, alien.rect.centerx, alien.rect.centery, random.randint(10,15))
                fire.play(0)
                enemybullets.add(enemybullet)
                allSprites.add(enemybullet)
        for enemybullet in enemybullets:
            if player.rect.inflate(-60,-60).colliderect(enemybullet.rect) and not player.exploding():#check if player is exploding
                healthkeeper.take_damage(random.randint(2,10)) #take random value of damage between 1 and 5
                enemybullet.kill()
        if healthkeeper.get_health() <= 0: #check if health is less than or equal to 0
            respawnScreen()
            death.play(0) #play death sound once
            player.killed()
            player.exploding()
            lifekeeper.life_lost(1) #if hp is 0 then take one life point off
            for enemybullet in enemybullets:
                enemybullet.kill() #kill all enemy bullet instances
                enemybullets.remove(enemybullet)
                allSprites.remove(enemybullet)
            for meteor in meteors: #reset all enemies off the screen
                meteor.reset(random.randint(0, screen.get_width()), random.randint(-5000, -1000))
            for alien in aliens:
                alien.reset(random.randint(-4,4), random.randint(1,8), random.randint(50, screen.get_width()-50), random.randint(-5000,0), random.randint(50, screen.get_height()/2))
            healthkeeper.respawn(health) #reset hp to 100
        if lifekeeper.get_lives() is 0:
            lifekeeper.life_gain(5) #make sure game over sound does not play more than once
            pygame.mouse.set_visible(True)
            scorekeeper.kill() #if lives is 0 then game ends
            healthkeeper.kill() #kill all sprites when game ends
            lifekeeper.kill()
            player.kill() #kill all sprites when game ends
            space.stop() #stop the background from moving
            for meteor in meteors:
                meteor.kill() #destroy all meteor instances
                meteors.remove(meteor)
            for bullet in bullets:
                bullet.kill()
                allSprites.remove(bullet)
            for alien in aliens:
                alien.kill()
                aliens.remove(alien)
            for healthpack in healthpacks:
                healthpack.kill()
                healthpacks.remove(healthpack)
            for extraLife in extraLives:
                extraLife.kill()
                extraLives.remove(extraLife)
            fire.set_volume(0)
            pygame.mixer.music.fadeout(1000)
            allSprites.remove(player) #remove all flame instances from screen
            allSprites.remove(playerflame1)
            allSprites.remove(playerflame2)
            allSprites.remove(playerflame3)
            allSprites.add(classes.GameoverScreen(screen)) #add gameover screen to sprite group and blit it
            gameOverSound.play()
            for event in pygame.event.get():
                if event.type is pygame.KEYDOWN:
                    running = False
        screen.blit(background, (0,0)) #refresh screen
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()
    pygame.quit() #exit

def game():
    menu() #call menu function
    main() #call main function

game()