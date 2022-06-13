import os
import pygame
from pygame import *
pygame.mixer.init()
pygame.font.init()


#all the variables ------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

WIDTH , HEIGHT = 900,500
WIN= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Legendary Game")



YELLOW = (255,255,0)
RED = (255,0,0)
WHITE = (255,255,255)

VEL = 5
BULLET_VEL = 8
MAX_BULLETS =  5

SPACESHIP_WIDTH , SPACESIP_HEIGHT = (55,40)
BORDER = pygame.Rect(WIDTH//2,0,10,HEIGHT)

Y_HIT = pygame.USEREVENT + 1
R_HIT = pygame.USEREVENT + 2

BULLET_HIT_SOUND =  pygame.mixer.Sound(os.path.join("Assets","Grenade+1.mp3")) 
BULLET_FIRE_SOUND =  pygame.mixer.Sound(os.path.join("Assets","Gun+Silencer.mp3")) 


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
YELLOW_SPACESHIP  = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,
( SPACESHIP_WIDTH,SPACESIP_HEIGHT)),90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_red.png"))
RED_SPACESHIP= pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,
( SPACESHIP_WIDTH,SPACESIP_HEIGHT)),270)

HEALTH_FONT = pygame.font.SysFont("Crispy Tofu",40)
WINNER_FONT = pygame.font.SysFont("Crispy Tofu",100)

SPACE =pygame.transform.scale(pygame.image.load(os.path.join("Assets","space.png")),(WIDTH,HEIGHT))
FPS = 60

#draws window and handles the appearance of images and graphics------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------



def draw_window(red,yellow,r_bullets,y_bullets,red_health,yellow_health):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,(0,0,0),BORDER)

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health),1 ,WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health),1,WHITE)

    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10,10))
    WIN.blit(yellow_health_text, (10,10))

    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))

    for bullet in y_bullets:
          pygame.draw.rect(WIN,YELLOW,bullet)
    for bullet in r_bullets:
          pygame.draw.rect(WIN,RED,bullet)
    

    pygame.display.update()

def handle_bullets(y_bullets,r_bullets,yellow,red):
      for bullet in y_bullets:
            bullet.x -= BULLET_VEL
            if red.colliderect(bullet):
                  pygame.event.post(pygame.event.Event(R_HIT))
                  y_bullets.remove(bullet)
            elif bullet.x > WIDTH:
                  y_bullets.remove(bullet)
     
     
      for bullet in r_bullets:
            bullet.x += BULLET_VEL
            if yellow.colliderect(bullet):
                  pygame.event.post(pygame.event.Event(Y_HIT))
                  r_bullets.remove(bullet)
            elif bullet.x < 0:
                  r_bullets.remove(bullet)

def draw_Winner(text):
      draw_text = WINNER_FONT.render(text,1,WHITE)
      WIN.blit(draw_text,(WIDTH/2-draw_text.get_width()/2,HEIGHT/2-draw_text.get_height()/2))
      
      pygame.display.update()
      
      pygame.time.delay(5000)

#Handle Movement of the characters--------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------
def yellow_handle_movement(key_pressed,yellow):
      
      if key_pressed[pygame.K_a] and yellow.x -VEL >0: #left
            yellow.x-= VEL
      if key_pressed[pygame.K_d] and yellow.x +VEL + yellow.width <  BORDER.x   : #right
            yellow.x+= VEL
      if key_pressed[pygame.K_w] and yellow.y - VEL >0: #up 
            yellow.y-= VEL
      if key_pressed[pygame.K_s] and yellow.y + VEL + yellow.height + 15< HEIGHT: #down
            yellow.y+= VEL
def red_handle_movement(key_pressed,red):
      
      if key_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #left
            red.x-= VEL
      if key_pressed[pygame.K_RIGHT] and red.x +VEL + red.width <  WIDTH: #right
            red.x+= VEL
      if key_pressed[pygame.K_UP] and red.y - VEL >0: #up
            red.y-= VEL
      if key_pressed[pygame.K_DOWN] and red.y + VEL + red.height + 15< HEIGHT: #down
            red.y+= VEL


def main():
    print("The Rules of the games are:\n")
    print("1. There are two players in the game.\n")
    print("2. Each player can 10 LIVES.\n")
    print("3. If you miss the opponent 5 times you will OUT OF BULLETS:\n")
    print("NOW ENJOY:))\n")
    red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESIP_HEIGHT)
    yellow= pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESIP_HEIGHT)
    clock = pygame.time.Clock()

    y_bullets = []
    r_bullets = []

    red_health = 10
    yellow_health = 10

    run= True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              run = False
              pygame.quit()         
            if event.type == pygame.KEYDOWN:
                  if event.key== pygame.K_LCTRL and len(y_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(yellow.x +yellow.width, yellow.y+yellow.height//2-2,10,5)
                        y_bullets.append(bullet) 
                        BULLET_FIRE_SOUND.play()       
                  
                  if event.key == pygame.K_RCTRL and len(r_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(red.x , red.y + red.height//2-2,10,5)
                        r_bullets.append(bullet)
                        BULLET_FIRE_SOUND.play() 

            if event.type == R_HIT:
                  yellow_health -= 1
                  BULLET_HIT_SOUND.play()
            if event.type == Y_HIT:
                  red_health -= 1
                  BULLET_HIT_SOUND.play()

        winner_text = ""
        if red_health<= 0 :
              winner_text = "Yellow Wins!"
        if yellow_health<= 0:
              winner_text = "Red Wins!"

        if winner_text!= "":
            draw_Winner(winner_text)
            break
        key_pressed = pygame.key.get_pressed()
        yellow_handle_movement(key_pressed,yellow)
        red_handle_movement(key_pressed,red)
        draw_window(red,yellow,r_bullets,y_bullets,red_health,yellow_health)
        
        handle_bullets(r_bullets,y_bullets,red ,yellow)
              
             
    main()



if __name__ == "__main__":
      main()


        
        
        
        







