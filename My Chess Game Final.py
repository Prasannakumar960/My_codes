# Import the library pygame
import pygame
from pygame.locals import *

# Take colors input
white = (255, 253, 208)
black = (150, 75, 0)
red=(255, 0, 0)
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
wq_loc=wq.get_rect()
wq_loc.center=(280,600)

wk=pygame.image.load(d["wk"])
wk=pygame.transform.scale(wk,(80,80))
wk_loc=wk.get_rect()
wk_loc.center = (360,600)

wb2=pygame.image.load(d["wb2"])
wb2=pygame.transform.scale(wb2,(80,80))
wb2_loc=wb2.get_rect()
wb2_loc.center =(440,600)

wkn2=pygame.image.load(d["wkn2"])
wkn2=pygame.transform.scale(wkn2,(80,80))
wkn2_loc=wkn2.get_rect()
wkn2_loc.center =(520,600)

wr2=pygame.image.load(d["wr2"])
wr2=pygame.transform.scale(wr2,(80,80))
wr2_loc=wr2.get_rect()
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

check="no"
check_x=320
check_y=40

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

regions_under_attack={"whites":{},"blacks":{}}
piece_type={"pawn":["wp1_loc", "wp2_loc", "wp3_loc", "wp4_loc", "wp5_loc", "wp6_loc", "wp7_loc", "wp8_loc","bp1_loc", "bp2_loc", "bp3_loc", "bp4_loc", "bp5_loc", "bp6_loc", "bp7_loc", "bp8_loc"],
           "rook":["wr1_loc","wr2_loc","br1_loc","br2_loc"],"bishop":["bb1_loc","bb2_loc","wb2_loc","wb1_loc"],"knight":["wkn1_loc","wkn2_loc","bkn2_loc","bkn1_loc"],"queen":["wq_loc","bq_loc"],"king":["wk_loc","bk_loc"]}
def find_piece_type(piece_name):
    for key,value in piece_type.items():
        if(piece_name in value):
            return key
def bishop_attack(col,row):
    bishop_list=[]
    rang1=list3[:list3.index(col)]
    rang1=rang1[::-1]
    for i in range(len(rang1)):
        row2=row-(i+1)
        if(1<=row2<=8):
            loc1=rang1[i]+str(row2)
            if(loc1 in piece_locs.values()):
                bishop_list.append(loc1)
                break
            else:
                bishop_list.append(loc1)
    rang2=list3[list3.index(col)+1:]
    for i in range(len(rang2)):
        row2=row-(i+1)
        if(1<=row2<=8):
            loc1=rang2[i]+str(row2)
            if(loc1 in piece_locs.values()):
                bishop_list.append(loc1)
                break
            else:
                bishop_list.append(loc1)
    for i in range(len(rang1)):
        row2=row+i+1
        if(1<=row2<=8):
            loc1=rang1[i]+str(row2)
            if(loc1 in piece_locs.values()):
                bishop_list.append(loc1)
                break
            else:
                bishop_list.append(loc1)
    for i in range(len(rang2)):
        row2=row+i+1
        if(1<=row2<=8):
            loc1=rang2[i]+str(row2)
            if(loc1 in piece_locs.values()):
                bishop_list.append(loc1)
                break
            else:
                bishop_list.append(loc1)
    return bishop_list

def rook_attack(col,row):
    rook_list=[]
    for i in range(row+1,9):
        loc1=col+str(i)
        if(loc1 in piece_locs.values()):
            rook_list.append(loc1)
            break
        else:
            rook_list.append(loc1)
    for j in range(row-1,0,-1):
        loc1=col+str(j)
        if(loc1 in piece_locs.values()):
            rook_list.append(loc1)
            break
        else:
            rook_list.append(loc1)
    rang1=list3[:list3.index(col)]
    rang1=rang1[::-1]
    for i in rang1:
        loc1=i+str(row)
        if(loc1 in piece_locs.values()):
            rook_list.append(loc1)
            break
        else:
            rook_list.append(loc1)
    rang2=list3[list3.index(col)+1:]
    for i in rang2:
        loc1=i+str(row)
        if(loc1 in piece_locs.values()):
            rook_list.append(loc1)
            break
        else:
            rook_list.append(loc1)
    return rook_list

def find_piece_loc(x1,y1):
    for key,value in loc_co_ords.items():
        if(x1==value[0] and y1==value[1]):
            return key

def find_piece_name(loc):
    for key,value in piece_locs.items():
        if(loc==value):
            return key
    
def find_piece_color(piece_name):
    for key,value in whites_blacks.items():
        if(piece_name in value):
            return key

def update_piece_loc_in_mem(x1,y1,piece):
    loc=find_piece_loc(x1,y1)
    piece_locs[piece]=loc

def find_mover(piece_name):
    if(find_piece_color(piece_name)==mover):
        return "yes"
    else:
        return "no"

mover="whites"
def change_mover():
    global mover
    if(mover=="whites"):
        mover="blacks"
    else:
        mover="whites"
def find_opposite_color(loc1):
    color=find_piece_color(find_piece_name(loc1))
    if(color=="whites"):
        return "blacks"
    else:
        return "whites"
def pawn_move(pawn,loc1,loc2):
    pawn_num=pawn[2]
    color=find_piece_color(pawn)
    col1=loc1[0]
    col2=loc2[0]
    row1=int(loc1[1])
    row2=int(loc2[1])
    if((list3.index(col1)+1==list3.index(col2) or list3.index(col1)-1==list3.index(col2)) and loc2 in piece_locs.values()):
        piece1_color=find_piece_color(find_piece_name(loc1))
        piece2_color=find_piece_color(find_piece_name(loc2))
        if((piece1_color=="whites" and row2-row1==1) or (piece1_color=="blacks" and row1-row2==1)):
            if(piece1_color!=piece2_color):
                return "kill"
            else:
                return "no"
        else:
            return "no"
    elif(col1==col2):
        if((row2>row1 and color=="whites" and row1==2) or (row1>row2 and color=="blacks" and row1==7)):
            if(0<abs(row2-row1)<3):
                return "yes"
            else:
                return "no"
        elif((row2>row1 and color=="whites" and row1!=2) or (row1>row2 and color=="blacks" and row1!=7)):
            if(abs(row1-row2)==1 and loc2 not in piece_locs.values()):
                return "yes"
            else:
                return "no"
        else:
            return "no"
    else:
        return "no"
    
list3=["A","B","C","D","E","F","G","H"]
def rook_authorize(loc1,loc2):
    col1=loc1[0]
    col2=loc2[0]
    row1=int(loc1[1])
    row2=int(loc2[1])
    if(col1==col2):
        if(row1<row2):
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
        elif(row2<row1):
            for i in range(row1-1,row2-1,-1):
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
            return "no"
            
    else:
        if(row1==row2):
            i1=list3.index(col1)
            i2=list3.index(col2)
            if(i1<i2):
                rang=list3[min(i1,i2)+1:max(i1,i2)+1]
            else:
                rang=list3[min(i1,i2):max(i1,i2)][::-1]
            for i in rang:
                if(i==rang[-1]):
                    if(i+str(row1) in piece_locs.values()):
                        piece1_color=find_piece_color(find_piece_name(loc1))
                        piece2_color=find_piece_color(find_piece_name(loc2))
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

list1_kng=["A", "B", "C", "D","E","F","G","H"] 
list3_kng={"B":1,"G":-1,"A":1,"H":-1}
knight_d={-2:1,-1:2,1:2, 2:1}

def knight_attacks(loc1):
    list2_kng=[]
    col=loc1[0]
    i1=list1_kng.index(col)
    row=int(loc1[1])
    if(i1>=2 and i1<=5):
        for k,v in knight_d.items():
            if(row+v<=8):
                loc1=list1_kng[i1+k]+str(row+v) 
                list2_kng.append(loc1)
            if(row-v>=1):
                loc1=list1_kng[i1+k]+str(row-v) 
                list2_kng.append(loc1)
    elif(i1==1 or i1==6):
        for k,v in knight_d.items():
            if(k>-2):
                if(row+v<=8):
                    loc1=list1_kng[i1+k*list3_kng[col]]+str(row+v) 
                    list2_kng.append(loc1)
                if(row-v>=1):
                    loc1=list1_kng[i1+k*list3_kng[col]]+str(row-v) 
                    list2_kng.append(loc1)
    else:
        for k,v in knight_d.items():
            if(k>-1):
                if(row+v<=8):
                    loc1=list1_kng[i1+k*list3_kng[col]]+str(row+v) 
                    list2_kng.append(loc1)
                if(row-v>=1):
                    loc1=list1_kng[i1+k*list3_kng[col]]+str(row-v) 
                    list2_kng.append(loc1)
    return list2_kng

def knight_authorize(loc1,loc2):
    list2_kng=knight_attacks(loc1)
    if(loc2 in list2_kng):
        if(loc2 in piece_locs.values()):
            piece1_color=find_piece_color(find_piece_name(loc1))
            piece2_color=find_piece_color(find_piece_name(loc2))
            if(piece1_color!=piece2_color):
                return "kill"
            else:
                return "no"
        else:
            return "yes"
    else:
        return "no"
    
def bishop_authorize(loc1,loc2):
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
                        if(k1+str(k2) in piece_locs.values()):
                            piece1_color=find_piece_color(find_piece_name(loc1))
                            piece2_color=find_piece_color(find_piece_name(loc2))
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


def king_attacks(loc1):
    col=loc1[0]
    row=int(loc1[1])
    king_list=[]
    for row1 in range(row-1,row+2):
        i1=list3.index(col)
        if(i1!=0 and i1!=7):
            rang=list3[i1-1:i1+2]
        elif(i1==0):
            rang=list3[i1:i1+2]
        else:
            rang=list3[i1-1:i1+1]
        for col1 in rang:
            if(0<row1<9):
                loc=col1+str(row1)
                if(loc!=loc1):
                    king_list.append(loc)
    return king_list

def king_authorize(loc1,loc2):
    king_list=king_attacks(loc1)
    opposite_color=find_opposite_color(loc1)
    if(loc2 in king_list):
        for val in regions_under_attack[opposite_color].values():
            if(loc2 in val):
                return "no"
        else:
            if(loc2 in piece_locs.values()):
                piece1_color=find_piece_color(find_piece_name(loc1))
                piece2_color=find_piece_color(find_piece_name(loc2))
                if(piece1_color!=piece2_color):
                    return "kill"
                else:
                    return "no"
            else:
                return "yes"
    else:
        return "no"

def region_under_attack(piece_name,loc):
    piece=find_piece_type(piece_name)
    col=loc[0]
    row=int(loc[1])
    if(piece=="pawn"):
        pawn_list=[]
        wp_bp={"whites":1,"blacks":-1}
        color=find_piece_color(piece_name)
        if(row<=7):
            i1=list3.index(col)
            decide_b_w = wp_bp[color]
            if(i1>0 and i1<7):
                loc1=list3[i1+1]+str(row+decide_b_w)
                loc2=list3[i1-1]+str(row+decide_b_w)
                pawn_list=[loc1,loc2]
            elif(i1==0):
                loc1=list3[i1+1]+str(row+decide_b_w)
                pawn_list=[loc1]
            else:
                loc1=list3[i1-1]+str(row+decide_b_w)
                pawn_list=[loc1]
            regions_under_attack[find_piece_color(piece_name)][piece_name]=pawn_list
                
    elif(piece=="rook"):
        rook_list=rook_attack(col,row)
        regions_under_attack[find_piece_color(piece_name)][piece_name]=rook_list
    elif(piece=="bishop"):
        bishop_list=bishop_attack(col,row)
        regions_under_attack[find_piece_color(piece_name)][piece_name]=bishop_list
    elif(piece=="queen"):
        rook_list=rook_attack(col,row)
        bishop_list=bishop_attack(col,row)
        queen_list=list(set(rook_list+bishop_list))
        regions_under_attack[find_piece_color(piece_name)][piece_name]=queen_list
    elif(piece=="king"):
        king_list=king_attacks(loc)
        regions_under_attack[find_piece_color(piece_name)][piece_name]=king_list
    else:
        knight_list=knight_attacks(loc)
        regions_under_attack[find_piece_color(piece_name)][piece_name]=knight_list
        
for piece_name,loc in piece_locs.items():
    region_under_attack(piece_name,loc)

boxes={"A1":[0,80,561,640],"B1":[81,160,561,640],"C1":[161,240,561,640],"D1":[241,320,561,640],"E1":[321,400,561,640],"F1":[401,480,561,640],"G1":[481,560,561,640],"H1":[561,640,561,640],
"A2":[0,80,481,560],"B2":[81,160,481,560],"C2":[161,240,481,560],"D2":[241,320,481,560],"E2":[321,400,481,560],"F2":[401,480,481,560],"G2":[481,560,481,560],"H2":[561,640,481,560],
"A3":[0,80,401,480],"B3":[81,160,401,480],"C3":[161,240,401,480],"D3":[241,320,401,480],"E3":[321,400,401,480],"F3":[401,480,401,480],"G3":[481,560,401,480],"H3":[561,640,401,480],
"A4":[0,80,321,400],"B4":[81,160,321,400],"C4":[161,240,321,400],"D4":[241,320,321,400],"E4":[321,400,321,400],"F4":[401,480,321,400],"G4":[481,560,321,400],"H4":[561,640,321,400],
"A5":[0,80,241,320],"B5":[81,160,241,320],"C5":[161,240,241,320],"D5":[241,320,241,320],"E5":[321,400,241,320],"F5":[401,480,241,320],"G5":[481,560,241,320],"H5":[561,640,241,320],
"A6":[0,80,161,240],"B6":[81,160,161,240],"C6":[161,240,161,240],"D6":[241,320,161,240],"E6":[321,400,161,240],"F6":[401,480,161,240],"G6":[481,560,161,240],"H6":[561,640,161,240],
"A7":[0,80,81,160],"B7":[81,160,81,160],"C7":[161,240,81,160],"D7":[241,320,81,160],"E7":[321,400,81,160],"F7":[401,480,81,160],"G7":[481,560,81,160],"H7":[561,640,81,160],
"A8":[0,80,0,80],"B8":[81,160,0,80],"C8":[161,240,0,80],"D8":[241,320,0,80],"E8":[321,400,0,80],"F8":[401,480,0,80],"G8":[481,560,0,80],"H8":[561,640,0,80]}

def check_color(x1,y1,check):
    if(check=="yes"):
        pygame.draw.rect(screen, red, (x1-40, y1-40, square_size, square_size))

def king_refuge(king_name):
    king_refuge_locs=[]
    king_color=find_piece_color(king_name)
    for loc in regions_under_attack[king_color][king_name]:
        if(loc in piece_locs.values()):
            piece_color=find_piece_color(find_piece_name(loc))
            if(king_color!=piece_color):
                flag=0
                fin_list=[]
                for val in regions_under_attack[find_opposite_color(piece_locs[king_name])].values():
                    fin_list=fin_list+val
                if(loc not in fin_list and loc not in king_refuge_locs):
                    king_refuge_locs.append(loc)
        else:
            fin_list=[]
            for val in regions_under_attack[find_opposite_color(piece_locs[king_name])].values():
                fin_list=fin_list+val
            if(loc not in fin_list and loc not in king_refuge_locs):
                king_refuge_locs.append(loc)
    return king_refuge_locs

def add_to_dict(killers,loc,pawn):
    if(loc not in killers):
        killers[loc]=[]
    else:
        killers[loc].append(pawn) 
def checkmate_authorize(attacker,checked_king):
    king_loc=piece_locs[checked_king]
    attackers=[]
    between_locs=[]
    killers={}
    for key,value in regions_under_attack[find_opposite_color(king_loc)].items():
        if(king_loc in value):
            checked_piece=key
            checked_piece_loc=piece_locs[checked_piece]
            attackers.append(checked_piece_loc)
        if(len(attackers)==1):
            col1=king_loc[0]
            row1=int(king_loc[1])
            col2=checked_piece_loc[0]
            row2=int(checked_piece_loc[1])
            i1=list3.index(col1)
            i2=list3.index(col2)
            # if attack is vertical
            if(col1==col2):
                if(row1>row2):
                    for row in range(row2,row1):
                        loc1=col1+str(row)
                        between_locs.append(loc1)
                else:
                    for row in range(row2,row1):
                        loc1=col1+str(row)
                        between_locs.append(loc1)
            # if attack is horizontal
            elif(row1==row2):
                if(i1<i2):
                    rang=list3[i1+1:i2+1]
                    for col in rang:
                        loc1=col+str(row1)
                        between_locs.append(loc1)
                else:
                    rang=list3[i2:i1]
                    for col in rang:
                        loc1=col+str(row1)
                        between_locs.append(loc1)
                    
            #if attack is diagonal
            elif(abs(i1-i2)==abs(row1-row2)):
                if(i1<i2):
                    rang=list3[i1+1:i2+1] # c8:f5
                else:
                    rang=list3[i2:i1][::-1]
                if(row1<row2):
                    rang2=range(row1+1,row2+1)
                else:
                    rang2=range(row1-1,row2-1,-1)
                for k1,k2 in zip(rang,rang2):
                    loc1=k1+str(k2)
                    between_locs.append(loc1)
            # attacker is a scary knight
            else:
                between_locs.append(piece_locs[attacker])
                    
            for loc11 in between_locs:
                killers[loc11]=[]
                
            for key2,val2 in regions_under_attack[find_piece_color(find_piece_name(king_loc))].items():
                for loc11 in between_locs:
                    if(loc11 in val2 and key2!=checked_king):
                        if(key2 in piece_type["pawn"]):
                            if(piece_locs[attacker] in val2):
                                killers[loc11].append(key2)
                        else:
                            killers[loc11].append(key2)
            king_refuge_locs=king_refuge(checked_king)
            
                        
            for pawn in piece_type["pawn"]:
                if(find_piece_color(pawn)==find_piece_color(checked_king) and pawn in piece_locs):
                    pawn_loc=piece_locs[pawn]
                    for btwn_loc in between_locs:
                        if(int(btwn_loc[1])-int(pawn_loc[1])==2 and int(pawn_loc[1])==2 and find_piece_color(pawn)=="whites"):
                            add_to_dict(killers,btwn_loc,pawn)
                        elif(int(pawn_loc[1])-int(btwn_loc[1])==2 and int(pawn_loc[1])==7 and find_piece_color(pawn)=="blacks"):
                            add_to_dict(killers,btwn_loc,pawn)
                        elif(int(btwn_loc[1])-int(pawn_loc[1])==1 and find_piece_color(pawn)=="whites"):
                            add_to_dict(killers,btwn_loc,pawn)
                        elif(int(pawn_loc[1])-int(btwn_loc[1])==1 and find_piece_color(pawn)=="blacks"):
                            add_to_dict(killers,btwn_loc,pawn)
            #print(king_refuge_locs)
            for loc11 in king_refuge_locs:
                if(loc11 in killers):
                    killers[loc11].append(checked_king)
                else:
                    killers[loc11]=[checked_king]
    final_attackers=[]
    for val in killers.values():
        final_attackers=final_attackers+val
    if(len(final_attackers)==0 and len(king_refuge_locs)==0):
        print("checkmate")
        return "checkmate"
    else:
        return killers


def checkmate_check(loc1,loc2,touched_piece,attacker,checked_king):
    king_loc=piece_locs[checked_king]
    attackers=[]
    between_locs=[]
    killers={}
    for key,value in regions_under_attack[find_opposite_color(king_loc)].items():
        if(king_loc in value):
            checked_piece=key
            checked_piece_loc=piece_locs[checked_piece]
            attackers.append(checked_piece_loc)
        if(len(attackers)==1):
            col1=king_loc[0]
            row1=int(king_loc[1])
            col2=checked_piece_loc[0]
            row2=int(checked_piece_loc[1])
            i1=list3.index(col1)
            i2=list3.index(col2)
            # if attack is vertical
            if(col1==col2):
                if(row1>row2):
                    for row in range(row2,row1):
                        loc1=col1+str(row)
                        between_locs.append(loc1)
                else:
                    for row in range(row2,row1):
                        loc1=col1+str(row)
                        between_locs.append(loc1)
            # if attack is horizontal
            elif(row1==row2):
                if(i1<i2):
                    rang=list3[i1+1:i2+1]
                    for col in rang:
                        loc1=col+str(row1)
                        between_locs.append(loc1)
                else:
                    rang=list3[i2:i1]
                    for col in rang:
                        loc1=col+str(row1)
                        between_locs.append(loc1)
                    
            #if attack is diagonal
            elif(abs(i1-i2)==abs(row1-row2)):
                if(i1<i2):
                    rang=list3[i1+1:i2+1] # c8:f5
                else:
                    rang=list3[i2:i1][::-1]
                if(row1<row2):
                    rang2=range(row1+1,row2+1)
                else:
                    rang2=range(row1-1,row2-1,-1)
                for k1,k2 in zip(rang,rang2):
                    loc1=k1+str(k2)
                    between_locs.append(loc1)
            # attacker is a scary knight
            else:
                between_locs.append(piece_locs[attacker])
                    
            for loc11 in between_locs:
                killers[loc11]=[]
            for key2,val2 in regions_under_attack[find_piece_color(find_piece_name(king_loc))].items():
                for loc11 in between_locs:
                    if(loc11 in val2 and key2!=checked_king):
                        if(key2 in piece_type["pawn"]):
                            if(piece_locs[attacker] in val2):
                                killers[loc11].append(key2)
                        else:
                            killers[loc11].append(key2)
            king_refuge_locs=king_refuge(checked_king)

            if(find_piece_type(touched_piece)=="pawn"):
                if(find_piece_color(touched_piece)==find_piece_color(checked_king)):
                    pawn_loc=piece_locs[touched_piece]
                    if(loc2 in between_locs and loc2[0]==pawn_loc[0]):
                        if(int(loc2[1])-int(pawn_loc[1])==2 and int(pawn_loc[1])==2 and find_piece_color(touched_piece)=="whites"):
                            killers[loc2].append(touched_piece)
                        elif(int(pawn_loc[1])-int(loc2[1])==2 and int(pawn_loc[1])==7 and find_piece_color(touched_piece)=="blacks"):
                            killers[loc2].append(touched_piece)
                        elif(int(loc2[1])-int(pawn_loc[1])==1 and find_piece_color(touched_piece)=="whites"):
                            killers[loc2].append(touched_piece)
                        elif(int(pawn_loc[1])-int(loc2[1])==1 and find_piece_color(touched_piece)=="blacks"):
                            killers[loc2].append(touched_piece)
            #print(king_refuge_locs)
            for loc11 in king_refuge_locs:
                if(loc11 in killers):
                    killers[loc11].append(checked_king)
                else:
                    killers[loc11]=[checked_king]
    final_attackers=[]
    for val in killers.values():
        final_attackers=final_attackers+val
    if(len(final_attackers)==0 and len(king_refuge_locs)==0):
        print("checkmate")
        return "checkmate"
    else:
        return killers
def check_authorize(loc1,loc2,touched_piece,attacker,checked_king):
    killers=checkmate_check(loc1,loc2,touched_piece,attacker,checked_king)
    for key,val in killers.items():
        if(touched_piece in val and loc2==key):
            if(find_piece_name(loc2)==attacker):
                return "kill"
            else:
                return "yes"
    else:
        return "no"

prom_types={"whites":{"queen":wq,"rook":wr1,"knight":wkn1,"bishop":wb1},"blacks":{"queen":bq,"rook":br1,"knight":bkn1,"bishop":bb1}}
def pawn_promotion(pawn,color):
    promotion_loc='C:\\Users\\user\\Music\\chess\\promotion\\'
    promotion_piece={"whites":["wq.jpg","wr.jpg","wkg.jpg","wb.jpg"],"blacks":["bq.jpg","br.jpg","bkg.jpg","bb.jpg"]}
    prom_list={}
    for y_loc,type1,piece in zip(range(200,600,100),prom_types[color].keys(),promotion_piece[color]):
        pro_piece=pygame.image.load(promotion_loc+piece)
        pro_piece=pygame.transform.scale(pro_piece,(100,100))
        pro_piece_rect=pro_piece.get_rect()
        prom_list[type1]=pro_piece_rect
        pro_piece_rect.center=(300,y_loc)
        screen.blit(pro_piece, pro_piece_rect)
    return prom_list

def draw():
    draw_img=pygame.image.load('C:\\Users\\user\\Music\\chess\\draw.png')
    draw_img=pygame.transform.scale(draw_img,(254,168))
    draw_rect=draw_img.get_rect()
    draw_rect.center=(300,300)
    screen.blit(draw_img, draw_rect)

def game_over(piece):
#    text=self.font.render("GameOver",True,black)
#    text_rect=text.get_rect(centre=(300,300))
    if(find_piece_color(piece)=="blacks"):
        winner=pygame.image.load('C:\\Users\\user\\Music\\chess\\white_wins.png')
    else:
        winner=pygame.image.load('C:\\Users\\user\\Music\\chess\\black_wins.png')
    winner=pygame.transform.scale(winner,(254,168))
    winner_rect=winner.get_rect()
    winner_rect.center=(300,300)
    screen.blit(winner, winner_rect)

promoted_pieces={}
    
def game():  
    # Set running and moving values
    running = True
    moving = False
    gameover=False
    promote=False
    show=False
    global check_x,check_y,check,wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8
    while running:

        for event in pygame.event.get():
            # Close if the user quits the game
            if event.type == QUIT:
                running = False
            # Making the image move
            elif event.type == MOUSEBUTTONDOWN:
                (mouse_x,mouse_y)=pygame.mouse.get_pos()
                (initial_x,initial_y)=find_center(mouse_x,mouse_y)
                if(pygame.mouse.get_pos()!=(initial_x,initial_y)):
                    pygame.mouse.set_pos(list((initial_x,initial_y)))
                    touched_piece_name=find_piece_name(find_piece_loc(initial_x,initial_y))
                    initial_loc=[initial_x,initial_y]
                if(promote):
                    for piece,prom_loc in prom_list.items():
                        if(prom_loc.collidepoint(event.pos)):
                            if("kn" in piece):
                                letter2="kn"
                            else:
                                letter2=piece[0]
                            piece_locs[letter1+letter2+prom_num+"_loc"]=pawn_loc
                            piece_type[piece].append(letter1+letter2+prom_num+"_loc")
                            whites_blacks[pawn_color].append(letter1+letter2+prom_num+"_loc")
                            promoted_pieces[touched_pawn]=letter1+letter2+prom_num+"_loc"
                            piece_color=find_piece_color(touched_pawn)
                            wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8 = prom_types[piece_color][piece] if touched_pawn=="wp1_loc" else wp1, prom_types[piece_color][piece] if touched_pawn=="wp2_loc" else wp2, prom_types[piece_color][piece] if touched_pawn=="wp3_loc" else wp3, prom_types[piece_color][piece] if touched_pawn=="wp4_loc" else wp4, prom_types[piece_color][piece] if touched_pawn=="wp5_loc" else wp5, prom_types[piece_color][piece] if touched_pawn=="wp6_loc" else wp6, prom_types[piece_color][piece] if touched_pawn=="wp7_loc" else wp7, prom_types[piece_color][piece] if touched_pawn=="wp8_loc" else wp8
                            bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8 = prom_types[piece_color][piece] if touched_pawn=="bp1_loc" else bp1, prom_types[piece_color][piece] if touched_pawn=="bp2_loc" else bp2, prom_types[piece_color][piece] if touched_pawn=="bp3_loc" else bp3, prom_types[piece_color][piece] if touched_pawn=="bp4_loc" else bp4, prom_types[piece_color][piece] if touched_pawn=="bp5_loc" else bp5, prom_types[piece_color][piece] if touched_pawn=="bp6_loc" else bp6, prom_types[piece_color][piece] if touched_pawn=="bp7_loc" else bp7, prom_types[piece_color][piece] if touched_pawn=="bp8_loc" else bp8
                            promote=False

                for i in list2:
                    if i.collidepoint(event.pos):
                        moving_piece=i
                        moving = True
                        break



            # Set moving as False if you want to move the image only with themouse click
            # Set moving as True if you want to move the image without the mouse click
            elif event.type == MOUSEBUTTONUP and find_mover(touched_piece_name)=="yes":
                moving = False
                (final_x,final_y)=correct_pos(mouse_x,mouse_y)
                touched_piece_type=find_piece_type(touched_piece_name)
                initial_pos=find_piece_loc(initial_x,initial_y)
                final_pos=find_piece_loc(final_x,final_y)
                if(check=="yes"):
                    authorize=check_authorize(initial_pos,final_pos,touched_piece_name,attacker,checked_king)
                elif(touched_piece_type=="bishop"):
                    authorize=bishop_authorize(initial_pos,final_pos)
                elif(touched_piece_type=="pawn"):
                    authorize=pawn_move(touched_piece_name,initial_pos,final_pos)
                elif(touched_piece_type=="knight"):
                    authorize=knight_authorize(initial_pos,final_pos)
                elif(touched_piece_type=="queen"):
                    authorize=rook_authorize(initial_pos,final_pos)
                    if(authorize=="no"):
                        authorize=bishop_authorize(initial_pos,final_pos)
                elif(touched_piece_type=="rook"):
                    authorize=rook_authorize(initial_pos,final_pos)
                else:
                    authorize=king_authorize(initial_pos,final_pos)
                if(authorize=="kill"):
                    dict1={ "wr1_loc":wr1_loc, "wkn1_loc":wkn1_loc, "wb1_loc":wb1_loc, "wq_loc":wq_loc, "wk_loc":wk_loc, "wb2_loc":wb2_loc, "wkn2_loc":wkn2_loc, "wr2_loc":wr2_loc, "br1_loc":br1_loc, "bkn1_loc":bkn1_loc, "bb1_loc":bb1_loc, "bq_loc":bq_loc, "bk_loc":bk_loc, "bb2_loc":bb2_loc, "bkn2_loc":bkn2_loc, "br2_loc":br2_loc, "wp1_loc":wp1_loc, "wp2_loc":wp2_loc, "wp3_loc":wp3_loc, "wp4_loc":wp4_loc, "wp5_loc":wp5_loc, "wp6_loc":wp6_loc, "wp7_loc":wp7_loc, "wp8_loc":wp8_loc, "bp1_loc":bp1_loc, "bp2_loc":bp2_loc, "bp3_loc":bp3_loc, "bp4_loc":bp4_loc, "bp5_loc":bp5_loc, "bp6_loc":bp6_loc, "bp7_loc":bp7_loc, "bp8_loc":bp8_loc}
                    attacked_piece=find_piece_name(final_pos)
                    for key,val in promoted_pieces.items():
                        val1=dict1[key]
                        dict1.pop(key)
                        dict1[val]=val1
                    for k,v in dict1.items():
                        if(k==attacked_piece):
                            v.update(1000,1000,80,80)
                            piece_locs.pop(attacked_piece)
                            regions_under_attack[find_piece_color(attacked_piece)].pop(attacked_piece)
                    authorize="yes"
                if(authorize=="yes"):
                    moving_piece.update(final_x-40,final_y-40,80,80)
                    update_piece_loc_in_mem(final_x,final_y,touched_piece_name)

                    if(touched_piece_type=="pawn"):
                        pawn_loc=piece_locs[touched_piece_name]
                        pawn_color=find_piece_color(touched_piece_name)
                        if((pawn_color=="whites" and int(pawn_loc[1])==8) or (pawn_color=="blacks" and int(pawn_loc[1])==1)):
                            promote=True
                            pawn_num=touched_piece_name[2]
                            prom_num=str(int(pawn_num)+2)
                            letter1=pawn_color[0]
                            pawn_loc=piece_locs[letter1+"p"+pawn_num+"_loc"]
                            piece_locs.pop(letter1+"p"+pawn_num+"_loc")
                            touched_pawn=touched_piece_name

                    for piece,loc in piece_locs.items():
                        region_under_attack(piece,loc)
                    white_king=piece_locs["wk_loc"]
                    black_king=piece_locs["bk_loc"]
                    for val in regions_under_attack[find_opposite_color(white_king)].values():
                        if(white_king in val):
                            check="yes"
                            checked_king="wk_loc"
                            attacker=touched_piece_name
                            check_x=loc_co_ords[white_king][0]
                            check_y=loc_co_ords[white_king][1]
                            break
                        else:
                            check="no"

                    if(check=="no"):
                        for val in regions_under_attack[find_opposite_color(black_king)].values():
                            if(black_king in val):
                                check="yes"
                                checked_king="bk_loc"
                                attacker=touched_piece_name
                                check_x=loc_co_ords[black_king][0]
                                check_y=loc_co_ords[black_king][1]
                                break
                            else:
                                check="no"
                    if(check=="yes"):
                        mate=checkmate_authorize(attacker,checked_king)
                        if(mate=="checkmate"):
                            gameover=True
                            break

                    change_mover()
                elif(authorize=="no"):
                    moving_piece.update(initial_x-40,initial_y-40,80,80)

            # Make your image move continuously
            elif event.type == MOUSEMOTION and moving:
                if(find_mover(touched_piece_name)=="yes"):
                    moving_piece.move_ip(event.rel)
                (mouse_x,mouse_y)=pygame.mouse.get_pos()
                
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
        check_color(check_x,check_y,check)
        screen.blit(wk, wk_loc)
        screen.blit(wr1, wr1_loc)
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

        if(promote):
            prom_list=pawn_promotion(touched_piece_name,pawn_color)
        if(gameover):
            game_over(checked_king)
        if(len(piece_locs)==2):
            draw()
        # Construct the border to the image
        pygame.draw.rect(screen, black, wk_loc, 2)

        # Update the GUI pygame
        pygame.display.update()

try:
    game()
except Exception as e:
    print(e)
# Quit the GUI game
pygame.quit()

