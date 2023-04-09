#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Import the library pygame
import pygame
from pygame.locals import *

# Take colors input
white = (255, 253, 208)
black = (150, 75, 0)

# Construct the GUI game
pygame.init()

# Set dimensions of game GUI
width, height = 640, 640
screen = pygame.display.set_mode((width, height))


board_size=8
square_size=80

#pieces
loc='C:\\Users\\user\\Music\\chess\\'
d={"wk":loc+"white_king.png","wq":loc+"white_queen.png","wkn1":loc+"white_knight.png", "wkn2":loc+"white_knight.png","wb1":loc+"white_bishop.png","wb2":loc+"white_bishop.png", "wr1":loc+"white_rook.png","wr2":loc+"white_rook.png","wp1":loc+"white_pawn.png", "wp2":loc+"white_pawn.png","wp3":loc+"white_pawn.png","wp4":loc+"white_pawn.png", "wp5":loc+"white_pawn.png","wp6":loc+"white_pawn.png","wp7":loc+"white_pawn.png", "wp8":loc+"white_pawn.png","bk":loc+"black_king.png","bq":loc+"black_queen.png", "bkn1":loc+"black_knight.png","bkn2":loc+"black_knight.png","bb1":loc+"black_bishop.png","bb2":loc+"black_bishop.png","br1":loc+"black_rook.png","br2":loc+"black_rook.png","bp1":loc+"black_pawn.png","bp2":loc+"black_pawn.png","bp3":loc+"black_pawn.png","bp4":loc+"black_pawn.png","bp5":loc+"black_pawn.png","bp6":loc+"black_pawn.png","bp7":loc+"black_pawn.png","bp8":loc+"black_pawn.png"}

img = pygame.image.load('C:\\Users\\user\\Music\\chess\\wb.jpg')
img.convert()
img=pygame.transform.scale(img,(80,80))

# Draw rectangle around the image
rect = img.get_rect()


# Take image as input
wr1=pygame.image.load(d["wr1"])
wr1=pygame.transform.scale(wr1,(80,80))
wr1_loc=wr1.get_rect()
wr1_loc.center = (40, 600)

wkn1=pygame.image.load(d["wkn1"])
wkn1=pygame.transform.scale(wkn1,(80,80))
wkn1_loc=wkn1.get_rect()
wkn1_loc.center=(120,600)

wb1=pygame.image.load(d["wb1"])
wb1=pygame.transform.scale(wb1,(80,80))
wb1_loc=wb1.get_rect()
wb1_loc.center=(200,600)

wq=pygame.image.load(d["wq"])
wq=pygame.transform.scale(wq,(80,80))
wq_loc=wb1.get_rect()
wq_loc.center=(280,600)

wk=pygame.image.load(d["wk"])
wk=pygame.transform.scale(wk,(80,80))
wk_loc=wk.get_rect()
wk_loc.center = (360,600)

wb2=pygame.image.load(d["wb2"])
wb2=pygame.transform.scale(wb2,(80,80))
wb2_loc=wk.get_rect()
wb2_loc.center =(440,600)

wkn2=pygame.image.load(d["wkn2"])
wkn2=pygame.transform.scale(wkn2,(80,80))
wkn2_loc=wk.get_rect()
wkn2_loc.center =(520,600)

wr2=pygame.image.load(d["wr2"])
wr2=pygame.transform.scale(wr2,(80,80))
wr2_loc=wk.get_rect()
wr2_loc.center =(600,600)

wp1=pygame.image.load(d["wp1"])
wp1=pygame.transform.scale(wp1,(80,80))
wp1_loc=wp1.get_rect()
wp1_loc.center =(40,520)

wp2=pygame.image.load(d["wp2"])
wp2=pygame.transform.scale(wp2,(80,80))
wp2_loc=wp2.get_rect()
wp2_loc.center =(120,520)

wp3=pygame.image.load(d["wp3"])
wp3=pygame.transform.scale(wp3,(80,80))
wp3_loc=wp3.get_rect()
wp3_loc.center =(200,520)

wp4=pygame.image.load(d["wp4"])
wp4=pygame.transform.scale(wp4,(80,80))
wp4_loc=wp4.get_rect()
wp4_loc.center =(280,520)

wp5=pygame.image.load(d["wp5"])
wp5=pygame.transform.scale(wp5,(80,80))
wp5_loc=wp5.get_rect()
wp5_loc.center =(360,520)

wp6=pygame.image.load(d["wp6"])
wp6=pygame.transform.scale(wp6,(80,80))
wp6_loc=wp6.get_rect()
wp6_loc.center =(440,520)

wp7=pygame.image.load(d["wp7"])
wp7=pygame.transform.scale(wp7,(80,80))
wp7_loc=wp7.get_rect()
wp7_loc.center =(520,520)

wp8=pygame.image.load(d["wp8"])
wp8=pygame.transform.scale(wp8,(80,80))
wp8_loc=wp8.get_rect()
wp8_loc.center =(600,520)

br1=pygame.image.load(d["br1"])
br1=pygame.transform.scale(br1,(80,80))
br1_loc=br1.get_rect()
br1_loc.center =(40,40)

bkn1=pygame.image.load(d["bkn1"])
bkn1=pygame.transform.scale(bkn1,(80,80))
bkn1_loc=bkn1.get_rect()
bkn1_loc.center =(120,40)

bb1=pygame.image.load(d["bb1"])
bb1=pygame.transform.scale(bb1,(80,80))
bb1_loc=bb1.get_rect()
bb1_loc.center =(200,40)

bq=pygame.image.load(d["bq"])
bq=pygame.transform.scale(bq,(80,80))
bq_loc=bq.get_rect()
bq_loc.center =(280,40)

bk=pygame.image.load(d["bk"])
bk=pygame.transform.scale(bk,(80,80))
bk_loc=bk.get_rect()
bk_loc.center =(360,40)

bb2=pygame.image.load(d["bb2"])
bb2=pygame.transform.scale(bb2,(80,80))
bb2_loc=bb2.get_rect()
bb2_loc.center =(440,40)

bkn2=pygame.image.load(d["bkn2"])
bkn2=pygame.transform.scale(bkn2,(80,80))
bkn2_loc=bkn2.get_rect()
bkn2_loc.center =(520,40)

br2=pygame.image.load(d["br2"])
br2=pygame.transform.scale(br2,(80,80))
br2_loc=br2.get_rect()
br2_loc.center =(600,40)

bp1=pygame.image.load(d["bp1"])
bp1=pygame.transform.scale(bp1,(80,80))
bp1_loc=bp1.get_rect()
bp1_loc.center =(40,120)

bp2=pygame.image.load(d["bp2"])
bp2=pygame.transform.scale(bp2,(80,80))
bp2_loc=bp2.get_rect()
bp2_loc.center =(120,120)

bp3=pygame.image.load(d["bp3"])
bp3=pygame.transform.scale(bp3,(80,80))
bp3_loc=bp3.get_rect()
bp3_loc.center =(200,120)

bp4=pygame.image.load(d["bp4"])
bp4=pygame.transform.scale(bp4,(80,80))
bp4_loc=bp4.get_rect()
bp4_loc.center =(280,120)

bp5=pygame.image.load(d["bp5"])
bp5=pygame.transform.scale(bp5,(80,80))
bp5_loc=bp5.get_rect()
bp5_loc.center =(360,120)

bp6=pygame.image.load(d["bp6"])
bp6=pygame.transform.scale(bp6,(80,80))
bp6_loc=bp6.get_rect()
bp6_loc.center =(440,120)

bp7=pygame.image.load(d["bp7"])
bp7=pygame.transform.scale(bp7,(80,80))
bp7_loc=bp7.get_rect()
bp7_loc.center =(520,120)

bp8=pygame.image.load(d["bp8"])
bp8=pygame.transform.scale(bp8,(80,80))
bp8_loc=bp8.get_rect()
bp8_loc.center =(600,120)

list1=[wr1,wkn1,wb1,wq,wq,wb2,wkn2,wr2,br1,bkn1,bb1,bq,bq,bb2,bkn2,br2,wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8, bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8]
list2=[wr1_loc, wkn1_loc, wb1_loc, wq_loc, wk_loc, wb2_loc, wkn2_loc, wr2_loc, br1_loc, bkn1_loc, bb1_loc, bq_loc, bk_loc, bb2_loc, bkn2_loc, br2_loc, wp1_loc, wp2_loc, wp3_loc, wp4_loc, wp5_loc, wp6_loc, wp7_loc, wp8_loc, bp1_loc, bp2_loc, bp3_loc, bp4_loc, bp5_loc, bp6_loc, bp7_loc, bp8_loc]


# Setting what happens when game
# is in running state
i=0
fx,fy=0,0
mx,my=0,0

def find_center(x1,y1):
    for key,value in boxes.items():
        v1=value[0]
        v2=value[1]
        v3=value[2]
        v4=value[3]
        if(x1>=v1 and x1<=v2 and y1>=v3 and y1<=v4):
            box=key
            return ((v1+v2)//2,(v3+v4)//2)


def correct_pos(x1,y1):
    (box_x,box_y)=find_center(x1,y1)
    find_piece_loc(box_x,box_y)
    if(x1<=box_x+40 and x1>box_x-40):
        if(y1>=box_y-40 and y1<box_y+40):
            return (box_x,box_y)
        elif(y1>=box_y-40):
            return (box_x,box_y+80)
        else:
            return (box_x,box_y-80)
    elif(x1>box_x-40):
        if(y1>=box_y-40 and y1<box_y+40):
            return (box_x+80,box_y)
        elif(y1>=box_y-40):
            return (box_x+80,box_y+80)
        else:
            return (box_x+80,box_y-80)
    else:
        if(y1>=box_y-40 and y1<box_y+40):
            return (box_x-80,box_y)
        elif(y1>=box_y-40):
            return (box_x-80,box_y+80)
        else:
            return (box_x-80,box_y-80)

whites_blacks={"whites":["wr1_loc", "wkn1_loc", "wb1_loc", "wq_loc", "wk_loc", "wb2_loc", "wkn2_loc", "wr2_loc", "wp1_loc", "wp2_loc", "wp3_loc", "wp4_loc", "wp5_loc", "wp6_loc", "wp7_loc", "wp8_loc"],"blacks":["br1_loc", "bkn1_loc", "bb1_loc", "bq_loc", "bk_loc", "bb2_loc", "bkn2_loc", "br2_loc", "bp1_loc", "bp2_loc", "bp3_loc", "bp4_loc", "bp5_loc", "bp6_loc", "bp7_loc", "bp8_loc"]}

piece_locs={"wr1_loc":"A1", "wkn1_loc":"B1", "wb1_loc":"C1", "wq_loc":"D1", "wk_loc":"E1", "wb2_loc":"F1", "wkn2_loc":"G1", "wr2_loc":"H1", 
"wp1_loc":"A2", "wp2_loc":"B2", "wp3_loc":"C2", "wp4_loc":"D2", "wp5_loc":"E2", "wp6_loc":"F2", "wp7_loc":"G2", "wp8_loc":"H2",
"br1_loc":"A8", "bkn1_loc":"B8", "bb1_loc":"C8", "bq_loc":"D8", "bk_loc":"E8", "bb2_loc":"F8", "bkn2_loc":"G8", "br2_loc":"H8", 
"bp1_loc":"A7", "bp2_loc":"B7", "bp3_loc":"C7", "bp4_loc":"D7", "bp5_loc":"E7", "bp6_loc":"F7", "bp7_loc":"G7", "bp8_loc":"H7"}

loc_co_ords={'A1': [40, 600], 'B1': [120, 600], 'C1': [200, 600], 'D1': [280, 600], 'E1': [360, 600], 'F1': [440, 600],'G1': [520, 600], 'H1': [600, 600],
             'A2': [40, 520], 'B2': [120, 520], 'C2': [200, 520], 'D2': [280, 520], 'E2': [360, 520], 'F2': [440, 520], 'G2': [520, 520], 'H2': [600, 520], 
             'A3': [40, 440], 'B3': [120, 440], 'C3': [200, 440], 'D3': [280, 440], 'E3': [360, 440], 'F3': [440, 440], 'G3': [520, 440], 'H3': [600, 440], 
             'A4': [40, 360], 'B4': [120, 360], 'C4': [200, 360], 'D4': [280, 360], 'E4': [360, 360], 'F4': [440, 360], 'G4': [520, 360], 'H4': [600, 360], 
             'A5': [40, 280], 'B5': [120, 280], 'C5': [200, 280], 'D5': [280, 280], 'E5': [360, 280], 'F5': [440, 280], 'G5': [520, 280], 'H5': [600, 280], 
             'A6': [40, 200], 'B6': [120, 200], 'C6': [200, 200], 'D6': [280, 200], 'E6': [360, 200], 'F6': [440, 200], 'G6': [520, 200], 'H6': [600, 200], 
             'A7': [40, 120], 'B7': [120, 120], 'C7': [200, 120], 'D7': [280, 120], 'E7': [360, 120], 'F7': [440, 120], 'G7': [520, 120], 'H7': [600, 120], 
             'A8': [40, 40], 'B8': [120, 40], 'C8': [200, 40], 'D8': [280, 40], 'E8': [360, 40], 'F8': [440, 40], 'G8': [520, 40], 'H8': [600, 40]}
def find_piece_loc(x1,y1):
    for key,value in loc_co_ords.items():
        if(x1==value[0] and y1==value[1]):
            return key
            #find_piece_name(key)
def find_piece_name(loc):
    for key,value in piece_locs.items():
        if(loc==value):
            return key
            #find_piece_color(key)
    
    
def find_piece_color(key1):
    for key,value in whites_blacks.items():
        if(key1 in value):
            return key
            #print(piece_color)

def update_piece_loc_in_mem(x1,y1,piece):
    loc=find_piece_loc(x1,y1)
    #piece_name=find_piece_name(loc)
    piece_locs[piece]=loc
    print(piece,loc)
    
list3=["A","B","C","D","E","F","G","H"]
def authorize_move(loc1,loc2):
    col1=loc1[0]
    col2=loc2[0]
    row1=int(loc1[1])
    row2=int(loc2[1])
    if(col1==col2):
        row1,row2=min(row1,row2),max(row1,row2)
        for i in range(row1+1,row2+1):
            if(i==row2):
                if(col1+str(i) in piece_locs.values()):
                    piece1_color=find_piece_color(find_piece_name(loc1))
                    piece2_color=find_piece_color(find_piece_name(loc2))
                    if(piece1_color!=piece2_color):
                        return "kill"
                    else:
                        return "no"
                else:
                    return "yes"
            elif(col1+str(i) in piece_locs.values()):
                return "no"
            
    else:
        if(row1==row2):
            i1=list3.index(col1)
            i2=list3.index(col2)
            if(i1<i2):
                rang=list3[min(i1,i2)+1:max(i1,i2)+1]
                print(rang)
            else:
                rang=list3[min(i1,i2):max(i1,i2)][::-1]
                print(rang)
            for i in rang:
                if(i==rang[-1]):
                    if(i+str(row1) in piece_locs.values()):
                        piece1_color=find_piece_color(find_piece_name(loc1))
                        piece2_color=find_piece_color(find_piece_name(loc2))
                        print(piece1_color,piece2_color)
                        if(piece1_color!=piece2_color):
                            #remove piece p2
                            return "kill"
                        else:
                            return "no"
                    else:
                        return "yes"
                elif(i+str(row1) in piece_locs.values()):
                    return "no"
        else:
            return "no"
def knight_auth(loc1,loc2):
    col1=loc1[0]
    col2=loc2[0]
    row1=int(loc1[1])
    row2=int(loc2[1])
    i1=list3.index(col1)
    i2=list3.index(col2)
    if(i1>2 and i1<5):
        rang=list3[i1-2:i1+3]
    elif(col1=="A"):
        rang=["B","C"]
    elif(col1=="B"):
        RANG=LIST[:4]
def bishop_auth(loc1,loc2):
    col1=loc1[0]
    col2=loc2[0]
    row1=int(loc1[1])
    row2=int(loc2[1])
    if(col1!=col2):
        if(row1!=row2):
            len1=abs(row2-row1)
            i1=list3.index(col1)
            i2=list3.index(col2)
            len2=abs(i1-i2)
            if(len1!=len2):
                return "no"
            else:
                if(i1<i2):
                    rang=list3[i1+1:i2+1] # c8:f5
                else:
                    rang=list3[i2:i1][::-1]
                if(row1<row2):
                    rang2=range(row1+1,row2+1)
                else:
                    rang2=range(row1-1,row2-1,-1)
                for k1,k2 in zip(rang,rang2):
                    if(k1==rang[-1]):
                        print("last",k1)
                        if(k1+str(k2) in piece_locs.values()):
                            piece1_color=find_piece_color(find_piece_name(loc1))
                            piece2_color=find_piece_color(find_piece_name(loc2))
                            print(piece1_color,piece2_color)
                            if(piece1_color!=piece2_color):
                                return "kill"
                            else:
                                return "no"
                        else:
                            return "yes"
                    elif(k1+str(k2) in piece_locs.values()):
                        return "no"
        else:
            return "no"
    else:
        return "no"


boxes={"A1":[0,80,561,640],"B1":[81,160,561,640],"C1":[161,240,561,640],"D1":[241,320,561,640],"E1":[321,400,561,640],"F1":[401,480,561,640],"G1":[481,560,561,640],"H1":[561,640,561,640],
"A2":[0,80,481,560],"B2":[81,160,481,560],"C2":[161,240,481,560],"D2":[241,320,481,560],"E2":[321,400,481,560],"F2":[401,480,481,560],"G2":[481,560,481,560],"H2":[561,640,481,560],
"A3":[0,80,401,480],"B3":[81,160,401,480],"C3":[161,240,401,480],"D3":[241,320,401,480],"E3":[321,400,401,480],"F3":[401,480,401,480],"G3":[481,560,401,480],"H3":[561,640,401,480],
"A4":[0,80,321,400],"B4":[81,160,321,400],"C4":[161,240,321,400],"D4":[241,320,321,400],"E4":[321,400,321,400],"F4":[401,480,321,400],"G4":[481,560,321,400],"H4":[561,640,321,400],
"A5":[0,80,241,320],"B5":[81,160,241,320],"C5":[161,240,241,320],"D5":[241,320,241,320],"E5":[321,400,241,320],"F5":[401,480,241,320],"G5":[481,560,241,320],"H5":[561,640,241,320],
"A6":[0,80,161,240],"B6":[81,160,161,240],"C6":[161,240,161,240],"D6":[241,320,161,240],"E6":[321,400,161,240],"F6":[401,480,161,240],"G6":[481,560,161,240],"H6":[561,640,161,240],
"A7":[0,80,81,160],"B7":[81,160,81,160],"C7":[161,240,81,160],"D7":[241,320,81,160],"E7":[321,400,81,160],"F7":[401,480,81,160],"G7":[481,560,81,160],"H7":[561,640,81,160],
"A8":[0,80,0,80],"B8":[81,160,0,80],"C8":[161,240,0,80],"D8":[241,320,0,80],"E8":[321,400,0,80],"F8":[401,480,0,80],"G8":[481,560,0,80],"H8":[561,640,0,80]}


def game():  
    # Set running and moving values
    running = True
    moving = False
    while running:

        for event in pygame.event.get():

            # Close if the user quits the
            # game
            if event.type == QUIT:
                running = False

            # Making the image move
            elif event.type == MOUSEBUTTONDOWN:
                (mx,my)=pygame.mouse.get_pos()
                (cx,cy)=find_center(mx,my)
                if(pygame.mouse.get_pos()!=(cx,cy)):
                    pygame.mouse.set_pos(list((cx,cy)))
                    touched_piece_name=find_piece_name(find_piece_loc(cx,cy))
                    initial_loc=[cx,cy]
                for i in list2:
                    if i.collidepoint(event.pos):
                        moving_piece=i

                        #find_piece_color(i)
                        moving = True
                        break

            # Set moving as False if you want to move the image only with themouse click
            # Set moving as True if you want to move the image without the mouse click
            elif event.type == MOUSEBUTTONUP:
                moving = False
                print(mx,my)
                (pk1,pk2)=correct_pos(mx,my)
               # moving_piece.move_ip(event.rel)
                if(touched_piece_name[1]=="b"):
                    auth=bishop_auth(find_piece_loc(cx,cy),find_piece_loc(pk1,pk2))
                else:
                    auth=authorize_move(find_piece_loc(cx,cy),find_piece_loc(pk1,pk2))
                if(auth=="kill"):
                    dict1={ "wr1_loc":wr1_loc, "wkn1_loc":wkn1_loc, "wb1_loc":wb1_loc, "wq_loc":wq_loc, "wk_loc":wk_loc, "wb2_loc":wb2_loc, "wkn2_loc":wkn2_loc, "wr2_loc":wr2_loc, "br1_loc":br1_loc, "bkn1_loc":bkn1_loc, "bb1_loc":bb1_loc, "bq_loc":bq_loc, "bk_loc":bk_loc, "bb2_loc":bb2_loc, "bkn2_loc":bkn2_loc, "br2_loc":br2_loc, "wp1_loc":wp1_loc, "wp2_loc":wp2_loc, "wp3_loc":wp3_loc, "wp4_loc":wp4_loc, "wp5_loc":wp5_loc, "wp6_loc":wp6_loc, "wp7_loc":wp7_loc, "wp8_loc":wp8_loc, "bp1_loc":bp1_loc, "bp2_loc":bp2_loc, "bp3_loc":bp3_loc, "bp4_loc":bp4_loc, "bp5_loc":bp5_loc, "bp6_loc":bp6_loc, "bp7_loc":bp7_loc, "bp8_loc":bp8_loc}
                    attacked_piece=find_piece_name(find_piece_loc(pk1,pk2))
                    for k,v in dict1.items():
                        if(k==attacked_piece):
                            v.update(1000,1000,80,80)
                            piece_locs.pop(attacked_piece)
                    auth="yes"
                if(auth=="yes"):
                    moving_piece.update(pk1-40,pk2-40,80,80)
                    update_piece_loc_in_mem(pk1,pk2,touched_piece_name)
                elif(auth=="no"):
                    moving_piece.update(cx-40,cy-40,80,80)
                print(pk1,pk2)

            # Make your image move continuously
            elif event.type == MOUSEMOTION and moving:
                moving_piece.move_ip(event.rel)
                (mx,my)=pygame.mouse.get_pos()


        # Set screen color and image on screen
        # Draw the chessboard
        for row in range(board_size):
            for col in range(board_size):
                x = col * square_size
                y = row * square_size
                if (row + col) % 2 == 0:
                    color = white
                else:
                    color = black
                pygame.draw.rect(screen, color, (x, y, square_size, square_size))

        screen.blit(wk, wk_loc)
        screen.blit(wr1, wr1_loc)
        #print(wr1_loc)
        screen.blit(wkn1, wkn1_loc)
        screen.blit(wb1, wb1_loc)
        screen.blit(wq, wq_loc)
        screen.blit(wb2, wb2_loc)
        screen.blit(wkn2, wkn2_loc)
        screen.blit(wr2, wr2_loc)
        screen.blit(wp1, wp1_loc)
        screen.blit(wp2, wp2_loc)
        screen.blit(wp3, wp3_loc)
        screen.blit(wp4, wp4_loc)
        screen.blit(wp5, wp5_loc)
        screen.blit(wp6, wp6_loc)
        screen.blit(wp7, wp7_loc)
        screen.blit(wp8, wp8_loc)

        screen.blit(br1, br1_loc)
        screen.blit(bkn1, bkn1_loc)
        screen.blit(bb1, bb1_loc)
        screen.blit(bq, bq_loc)
        screen.blit(bk, bk_loc)
        screen.blit(bb2, bb2_loc)
        screen.blit(bkn2, bkn2_loc)
        screen.blit(br2, br2_loc)
        screen.blit(bp1, bp1_loc)
        screen.blit(bp2, bp2_loc)
        screen.blit(bp3, bp3_loc)
        screen.blit(bp4, bp4_loc)
        screen.blit(bp5, bp5_loc)
        screen.blit(bp6, bp6_loc)
        screen.blit(bp7, bp7_loc)
        screen.blit(bp8, bp8_loc)


        # Construct the border to the image
        pygame.draw.rect(screen, black, wk_loc, 2)

        # Update the GUI pygame
        pygame.display.update()

#try:
game()
#except Exception as e:
#    print(e)
# Quit the GUI game
pygame.quit()


# In[113]:


authorize_move("F8","B8")


# In[14]:


bishop_auth("A1","D4")


# In[32]:





# In[ ]:




