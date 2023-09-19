#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pygame
import random
import time

file=open("C:\\Users\\user\\Music\\snake_game\\highscore.txt","r")
highscore=file.readline().strip()
file.close()

black = (0,0,0)
green=(0,255,0)
red=(255, 0, 0)
yellow=(255,255,0)
pygame.init()
width, height = 640, 640
screen = pygame.display.set_mode((width, height))
pos1,pos2=320,320     #initial location of snake
snake=[[320,320]]         
run=True
size=16
r1=range(16,640,size)
food=[random.choice(r1),random.choice(r1)]
bonus_loc=[None,None]
directions={"vertical":{pygame.K_UP:-size,pygame.K_DOWN:size},"horizontal":{pygame.K_RIGHT:size,pygame.K_LEFT:-size}}
pos="pos1"
inc=size
pause=False
speed=0.1
# loc='C:\\Users\\user\\Downloads\\snake1.png'
# snake=pygame.image.load(loc)
# snake_size=20
# snake=pygame.transform.scale(snake,(snake_size,snake_size-1))
# snake_loc=snake.get_rect()
# snake_loc.center = (320,320)

score_value=0
font=pygame.font.SysFont("freesansbold.ttf",32)
textx=460
texty=0

def generate_food():
    x,y=random.choice(r1),random.choice(r1)
    if([x,y] not in snake):
        food[0]=x
        food[1]=y
    else:
        generate_food()
def generate_bonus():
    x,y=random.choice(r1),random.choice(r1)
    if([x,y] not in snake):
        bonus_loc[0]=x
        bonus_loc[1]=y
    else:
        generate_bonus()
    
def show_score(x,y):
    score=font.render("SCORE : {}".format(score_value),True,"green","blue")
    screen.blit(score,(x,y))

def end(x,y):
    msg1=font.render("YOUR SCORE : {}".format(score_value),True,"green","blue")
    msg2=font.render("HIGH SCORE : {}".format(highscore),True,"green","blue")
    screen.blit(msg1,(x,y))
    screen.blit(msg2,(x,y+20))
    
gameover=False
bonus=False
bonus_timer=0

try:
    while run:
        show_score(textx,texty)
        for p1,p2 in snake:
            pygame.draw.rect(screen, red, (p1, p2, size, size))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN:               
                if(event.key==pygame.K_UP or event.key==pygame.K_DOWN):
                    direct="vertical"
                    if(pos!="pos2"):
                        pos="pos2"
                        inc=directions[direct][event.key]
                        pause=False
                elif(event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
                    direct="horizontal"
                    if(pos!="pos1"):
                        pos="pos1"
                        inc=directions[direct][event.key]
                        pause=False
                elif event.key == pygame.K_SPACE:
                    pause=True

        if(not(pause) and not(gameover)):        
            time.sleep(speed)
            
            if(pos=="pos1"):
                pos1+=inc
            else:
                pos2+=inc
            if(pos1>=640):
                pos1=size
            elif(pos1<size):
                pos1=640
            if(pos2>=640):
                pos2=size
            elif(pos2<size):
                pos2=640
            pygame.draw.rect(screen, green, (food[0],food[1], size, size))
            
            if([pos1,pos2]==food):
                generate_food()
                snake.insert(1,snake[0])
                score_value+=1
                if(score_value%5==0 and score_value!=0):
                    generate_bonus()
                    bonus=True
                   
            if(bonus):
                bonus_timer+=speed
                if(bonus_timer<5):
                    pygame.draw.rect(screen, yellow, (bonus_loc[0],bonus_loc[1], size, size))
                    if([pos1,pos2]==bonus_loc):
                        score_value+=5
                        bonus=False
                        bonus_timer=0
                else:
                    bonus=False
                    bonus_timer=0
                    pygame.draw.rect(screen, black, (bonus_loc[0],bonus_loc[1], size, size))
            if([pos1,pos2] in snake):
                if(int(highscore)<score_value):
                    file=open("C:\\Users\\user\\Music\\snake_game\\highscore.txt","w")
                    file.write(str(score_value))
                    file.close()
                    highscore=score_value
                gameover=True
                
            snake.append([pos1,pos2])
            
        pygame.display.update()
        pygame.draw.rect(screen, black, (snake[0][0], snake[0][1], size, size))
        if(gameover):
            end(220,270)
        if(not(pause) and not(gameover)):
            snake.pop(0)
except Exception as e:
    print(e)
pygame.quit()


# In[ ]:




