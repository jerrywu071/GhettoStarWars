'''Name: Jerry Wu
Date: DUE MAY 29TH 2018
Description: CLASSES FOR GAME'''
import pygame, random #import libraries we need to use

#+++PLAYER SPRITES AND LABELS+++
class Player(pygame.sprite.Sprite):
    '''This class is for spawning the main player sprite'''
    def __init__(self, screen, xpos, ypos):
        '''This method initializes the sprite onto the screen'''
        pygame.sprite.Sprite.__init__(self) #call parent initializer
        self.__screen = screen #set screen
        self.__dx = 0 #initial speed in x direction is 0
        self.__dy = 0 #initial speed in y direction is 0
        self.__xpos = xpos
        self.__ypos = ypos
        self.__images = []
        for imagenum in range(82):
            self.__images.append(pygame.image.load("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\PLAYERSPRITES\\player" + str(imagenum) + ".png").convert_alpha())
        self.image = self.__images[0]
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.centerx = random.randint(0,self.__screen.get_width())
        self.rect.centery = 0
        self.__exploding = False
        self.rect = self.image.get_rect() #get rect of the image to detect colissions
        self.rect.centerx = screen.get_width()/2 #set initial x position
        self.rect.centery = screen.get_width()/2 #set initial y position
    def change_direction(self, xy_change):
        '''This method is called whenever the player wants to change direction'''
        self.__dx = xy_change[0] #index x change as element 0 in the xy tuple
        self.__dy = xy_change[1] #index y change as element 1 in the xy tuple
    def get_pos(self):
        '''This accessor method will be passed into the bullet object as an argument to find out where to fire from'''
        return (self.rect.centerx, self.rect.centery) #returns xy tuple
    def killed(self):
        '''This method sets the enemy's exploding mode to true'''
        self.__imagenum = 1
        self.__exploding = True
        self.__dx = 0
        self.__dy = 0
    def exploding(self):
        '''This method checks whether the enemy is in exploding mode or not'''
        return self.__exploding
    def reset(self):
        '''This method resets the meteors to the top of the screen'''
        self.rect.bottom = self.__screen.get_width()
        self.rect.centerx = random.randrange(0, self.__screen.get_width())
        self.__exploding = False
        self.image = self.__images[0]
        self.image = self.image.convert_alpha()
    def update(self):
        '''This method is used to detect colissions and make sure the player doesnt go off the screen'''
        if self.__exploding:
            if self.__imagenum < len(self.__images):
                self.image = self.__images[self.__imagenum]
                self.image = self.image.convert_alpha()
                self.__imagenum += 1
            else:
                self.reset()        
        if self.rect.centerx < 0: #if left of rect is less than 0 make dx 0 and set left position to 0
            self.__dx = 0
            self.rect.centerx = 0
        if self.rect.centerx > self.__screen.get_width(): #if left of rect is less than 0 make dx 0 and set right position to screen width
            self.__dx = 0
            self.rect.centerx = self.__screen.get_width()
        if self.rect.top < 0: #if top of rect is less than 0 make dy 0 and set top position to 0
            self.__dy = 0
            self.rect.top = 0
        if self.rect.bottom > self.__screen.get_height(): #if left of rect is less than 0 make dy 0 and set bottom position to screen height
            self.__dy = 0
            self.rect.bottom = self.__screen.get_height()
        self.rect.centerx += self.__dx*10
        self.rect.centery += self.__dy*10
        
class Scorekeeper(pygame.sprite.Sprite):
    '''This class will be used to create the scorekeeper at the top of the screen'''
    def __init__(self, score):
        '''This method will allow us to spawn the scorekeeper on the screen'''
        pygame.sprite.Sprite.__init__(self) #call parent initializer
        self.__font = pygame.font.Font("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\FONTS\\StarWars.ttf", 30) #load custom font
        self.__player_score = score #initial player score is 0
    def player_scored(self, pointvalue):
        '''This method will have an argument passed in for the point value of an enemy that was killed. Each enemy will have a "get_point_value() method.'''
        self.__player_score += pointvalue #pointvalue depends on what kind of enemy was killed.
    def update(self):
        '''This method will be used to display the score at the top of the window'''
        message = "Score: %d" %self.__player_score
        self.image = self.__font.render(message, 1, (255,255,255)) #set position on screen
        self.rect = self.image.get_rect()
        self.rect.center = (100, 15) #set position on screen
        
class Healthkeeper(pygame.sprite.Sprite):
    '''This class will be used to display the player's current health'''
    def __init__(self, health_number):
        '''This constructor initializes the healthkeeper on the screen'''
        pygame.sprite.Sprite.__init__(self) #call parent initializer method
        self.__font = pygame.font.Font("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\FONTS\\StarWars.ttf", 30)
        self.__health = health_number
    def take_damage(self, damage):
        '''This method subtracts health from the player'''
        self.__health -= damage
    def respawn(self, health_number):
        '''This method resets the health number after all hp is lost'''
        self.__health = health_number
    def set_health(self, hpnum):
        '''This method will be used to reset health of the player if they overheal with healthpacks'''
        self.__health = hpnum
    def get_health(self):
        '''This method returns the number of health points the player has left'''
        return self.__health
    def healthup(self, health):
        '''This method is called whenever the player collides with a healthpack powerup'''
        self.__health += health
    def update(self):
        '''This method displays number of HP points remaining'''
        message = "HP: %d" %self.__health #display message
        self.image = self.__font.render(message, 1, (0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (300, 15) #set position on screen
        
class Lifekeeper(pygame.sprite.Sprite):
    '''This class will be used to display the number of lives remaining'''
    def __init__(self, life_number):
        '''This constructor spawns the lifekeeper on the screen'''
        pygame.sprite.Sprite.__init__(self) #call parent initializer
        self.__font = pygame.font.Font("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\FONTS\\StarWars.ttf", 30)
        self.__lives = life_number
    def life_lost(self, lives_lost):
        '''This method subtracts a life from the lifekeeper'''
        self.__lives -= lives_lost
    def life_gain(self, life):
        '''This method is called when the user collects a 1up powerup'''
        self.__lives += life
    def set_lives(self, life):
        '''This method is used to make sure lives dont go above a certain value'''
        self.__lives = life
    def get_lives(self):
        '''This method returns number of lives left'''
        return self.__lives
    def update(self):
        '''This method displays number of lives remaining'''
        message = "Lives left: %d" %self.__lives #display message
        self.image = self.__font.render(message, 1, (255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (500, 15) #set position on screen

class Bullet(pygame.sprite.Sprite):
    '''This class will allow us to create bullets when the player shoots'''
    def __init__(self, position):
        '''This constructor initializes the bullets onto the screen'''
        pygame.sprite.Sprite.__init__(self) #call parent initializer
        self.image = pygame.image.load("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\PLAYERSPRITES\\bullet.png") #load image
        self.rect = self.image.get_rect()
        self.__dy = 0 #y position only
        self.rect.center = position
    def fire(self, dy):
        '''This method will fire the bullet'''
        self.__dy = dy #set dy to a dy passed into the method
    def update(self):
        '''This method allows us to kill the bullets so that they dont keep going forever'''
        self.rect.centery -= self.__dy
        if self.rect.bottom < 0:
            self.kill()

class GameoverScreen(pygame.sprite.Sprite):
    '''This class creates the game over screen'''
    def __init__(self, screen):
        '''This constructor contains all the instance variables'''
        pygame.sprite.Sprite.__init__(self)
        self.__font = pygame.font.Font("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\FONTS\\font2.ttf", 50)
        self.__screen = screen
    def update(self):
        '''This method prints the message to the screen'''
        message = "GAME OVER!"
        self.image = self.__font.render(message, 1, (255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.__screen.get_width()/2, self.__screen.get_height()/2)
#+++ENEMY CLASSES+++
class Alien(pygame.sprite.Sprite): #INCOMPLETE
    '''This class allows us to create aliens that try to kill the player'''
    def __init__(self, screen, dx, dy, xpos, ypos, maxypos):
        '''This constructor initializes the sprite onto the screen'''
        pygame.sprite.Sprite.__init__(self) #call parent initializer
        self.__images = [] #make list of images
        for imagenum in range(82): #load all images
            self.__images.append(pygame.image.load("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\ENEMYSPRITES\\alien" + str(imagenum) + ".png").convert_alpha()) #string formatting
        self.image = self.__images[0] #set image to index 0
        self.rect = self.image.get_rect() #get the rect of the image
        self.rect.left = xpos
        self.rect.top = ypos
        self.__dx = dx
        self.__dy = dy
        self.__maxypos = maxypos
        self.__screen = screen
        self.__isatmaxypos = False
        self.__exploding = False
        self.__health = 5
    def get_pos(self):
        '''returns xy tuple of the enemy's position'''
        return(self.__xpos, self.__ypos)
    def killed(self):
        '''This method sets the enemy's exploding mode to true'''
        self.__imagenum = 1
        self.__exploding = True #set to exploding state
        self.__dx = 0 #stop moving
        self.__dy = 0
    def exploding(self):
        '''This method checks whether the enemy is in exploding mode or not'''
        return self.__exploding
    def take_damage(self):
        '''This method is called when the player bullet hits the alien'''
        self.__health -= 1
    def get_health(self):
        '''This method returns the alien's current health state'''
        return self.__health
    def reset(self, dx, dy, xpos, ypos, maxypos):
        '''This method resets the meteors to the top of the screen'''
        self.image = self.__images[0] #reset all instance variables to the same ones in __init__()
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.left = xpos
        self.rect.top = ypos
        self.__dx = dx
        self.__dy = dy
        self.__maxypos = maxypos
        self.__isatmaxypos = False
        self.__exploding = False
        self.__health = 5
    def update(self):
        '''This method allows the aliens to die after they reach any edge of the screen'''
        self.rect.centery += self.__dy
        self.rect.centerx += self.__dx
        if self.rect.centery > self.__maxypos and not self.__isatmaxypos:
            self.__isatmaxypos = True
            self.__dy = 0
            self.__dx = random.randint(-5,5)
            while self.__dx is 0: #make sure the selected value is not 0
                self.__dx = random.randint(-5,5)
            self.rect.centerx += self.__dx
        if self.__exploding: #check if meteor is exploding
            if self.__imagenum < len(self.__images):
                self.image = self.__images[self.__imagenum]
                self.image = self.image.convert_alpha()
                self.__imagenum += 1
            else:
                self.reset(random.randint(-4,4), random.randint(1,8), random.randint(50, self.__screen.get_width()-50), random.randint(-5000,0), random.randint(50, self.__screen.get_height()/2)) #reset        
        if (self.rect.left < 0) or (self.rect.right > self.__screen.get_width()):
            self.__dx = -self.__dx

class Meteor(pygame.sprite.Sprite):
    '''This class spawns meteors'''
    def __init__(self, screen, xpos, ypos):
        '''This method will initialize all the instance variables of the meteors'''
        pygame.sprite.Sprite.__init__(self) #call parent initializer
        self.__screen = screen
        self.__dx = random.randint(-5, 5) #random x directions
        self.__dy = random.randint(5,10) #random y directions only down
        self.__images = []
        for imagenum in range(82): #load all images
            self.__images.append(pygame.image.load("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\ENEMYSPRITES\\meteor" + str(imagenum) + ".png").convert_alpha())
        self.image = self.__images[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = xpos
        self.rect.bottom = ypos
        self.__exploding = False
    def killed(self):
        '''This method sets the enemy's exploding mode to true'''
        self.__imagenum = 1
        self.__exploding = True
        self.__dx = 0
        self.__dy = 0
    def exploding(self):
        '''This method checks whether the enemy is in exploding mode or not'''
        return self.__exploding
    def reset(self, xpos, ypos):
        '''This method resets the meteors to the top of the screen'''
        self.rect.bottom = ypos
        self.rect.centerx = xpos
        self.__dx = random.randint(-5, 5) #random x directions
        self.__dy = random.randint(10, 15) #random y directions only down
        self.__exploding = False
        self.image = self.__images[0]
        self.image = self.image.convert_alpha()
        self.rect.centerx = xpos
        self.rect.bottom = ypos
    def get_pos(self):
        '''This method returns the position of the meteor'''
        return self.rect.center
    def update(self):
        '''This method will check if the meteor is off the screen so we can call the reset method'''
        self.rect.centerx += self.__dx
        self.rect.centery += self.__dy
        if self.__exploding: #check if meteor is exploding
            if self.__imagenum < len(self.__images):
                self.image = self.__images[self.__imagenum]
                self.image = self.image.convert_alpha()
                self.__imagenum += 1
            else:
                self.reset(random.randint(0, self.__screen.get_width()), -1000) #reset
        if self.rect.top > self.__screen.get_height() or self.rect.right < 0 or self.rect.left > self.__screen.get_width():
            self.reset(random.randint(0,self.__screen.get_width()), -1000) #reset

class EnemyBullet(pygame.sprite.Sprite):
    '''This class allows the enemy to shoot'''
    def __init__(self, screen, xpos, ypos, dy):
        '''This method initializes all instance variables'''
        pygame.sprite.Sprite.__init__(self) #call parent initializer
        self.image = pygame.image.load("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\ENEMYSPRITES\\enemybullet.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = xpos
        self.rect.centery = ypos
        self.__dy = dy
        self.__screen = screen
    def update(self):
        '''This method will kill the bullet if it goes off the screen'''
        self.rect.centery += self.__dy
        if self.rect.top > self.__screen.get_width():
            self.kill()
#+++POWERUPS
class Healthpack(pygame.sprite.Sprite):
    '''This class will be used to create health packs for which the player can regain health'''
    def __init__(self, screen, xpos, ypos, dy):
        '''This method initializes all instance variables for the object'''
        pygame.sprite.Sprite.__init__(self) #call parent initializer
        self.image = pygame.image.load("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\MISC\\healthpack.png")
        self.rect = self.image.get_rect()
        self.__screen = screen
        self.__dy = dy #set dy and position
        self.rect.centerx = xpos
        self.rect.centery = ypos
    def update(self):
        '''Make sure the sprite is killed when it goes off screen'''
        self.rect.centery += self.__dy
        if self.rect.top > self.__screen.get_height(): #kill if it goes off screen
            self.kill()

class Extralife(pygame.sprite.Sprite):
    '''This method is used to spawn 1up powerups for which the player can regain a life'''
    def __init__(self, screen, xpos, ypos, dy):
        '''This method initializes instance variables upon instanciation'''
        pygame.sprite.Sprite.__init__(self) #call parent initializer
        self.image = pygame.image.load("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\MISC\\1up.png")
        self.rect = self.image.get_rect()
        self.__screen = screen
        self.__dy = dy
        self.rect.centerx = xpos
        self.rect.centery = ypos
    def update(self):
        self.rect.centery += self.__dy
        if self.rect.top > self.__screen.get_height():
            self.kill()
#++MISC CLASSES+++
class Background(pygame.sprite.Sprite):
    '''This class creates the background'''
    def __init__(self, screen, dy):
        '''This method sets all the instance variables'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:\\Users\\Jerry\\Desktop\\ICS SUMMATIVE GAME\\MISC\\background.png")
        self.rect = self.image.get_rect()
        self.__screen = screen
        self.__dy = dy
        self.rect.bottom = self.__screen.get_height()
    def stop(self):
        '''This method stops the background from moving when game ends'''
        self.__dy = 0
    def start(self, dy):
        self.__dy = dy
    def update(self):
        '''This method will cause the background to reset'''
        self.rect.bottom += self.__dy
        if self.rect.top + 720 > self.__screen.get_height():
            self.reset()
    def reset(self):
        '''This method resets the background'''
        self.rect.bottom = self.__screen.get_height()

class Flame(pygame.sprite.Sprite):
    '''***CREDITS TO JASON SUN***, this class will leave a trail behind a meteor and the spaceship'''
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self) #call parent init method
        size = random.randrange(5,20) #Particles
        self.image = pygame.Surface((size,size))
        self.rect = self.image.get_rect()
        self.color = [(random.randint(0,255), random.randint(0,255), random.randint(0,255)), (random.randint(0,255), random.randint(0,255), random.randint(0,255)),(random.randint(0,255), random.randint(0,255), random.randint(0,255))]
        self.color = random.choice(self.color) #random colour cycle
        self.pos = pos
        self.image.fill(self.color)
    def update(self):
        '''update method for meteor and spaceship trail'''
        self.pos = (self.pos[0], self.pos[1]+2)
        self.image = pygame.Surface((self.rect.width-1,self.rect.width-1))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.image.fill(self.color)
        if self.rect.width is 1:
            #make sure flame goes away after set amount of time
            self.kill()