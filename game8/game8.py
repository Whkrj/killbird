import pygame
import random as r
pygame.init()

screen_width = 1300
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('새 잡기')

background = pygame.image.load('backback.png')
xodzm = pygame.image.load('xodzm1.png')
xodzm1 = pygame.image.load('xodzm1.png')
xodzm2 = pygame.image.load('xodzm2.png')
xodzm3 = pygame.image.load('xodzm3.png')
xodzm4 = pygame.image.load('xodzm4.png')
to1 = pygame.image.load('toto.png')
to2 = pygame.image.load('toto.png')
toto1 = pygame.image.load('toto.png')
toto2 = pygame.image.load('toto2.png')
ento1 = pygame.image.load('ento.png')
ento2 = pygame.image.load('ento2.png')
vlto1 = pygame.image.load('vlto.png')
vlto2 = pygame.image.load('vlto2.png')
qhtm1 = pygame.image.load('qhtm1.png')
qhtm2 = pygame.image.load('qhtm2.png')
qhtm1 = pygame.transform.scale(qhtm1, (300,300))
qhtm2 = pygame.transform.scale(qhtm2, (300,300))
qhtm = qhtm1
rmsqhs1 = toto1
rmsqhs2 = toto2

xodzm_X_pos = 600
xodzm_Y_pos = 500
to_x = 0
kill = 1
to1_X_pos = r.randint(0,1100)
to1_Y_pos = -200
to2_X_pos = r.randint(0,1100)
to2_Y_pos = -200
qhtm_X_pos = r.randint(0,900)
qhtm_Y_pos = -300
totohp = 200
entohp = 500
vltohp = 1000
rmshp = totohp
to1_hp = rmshp
to2_hp = rmshp



runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 10
                xodzm = xodzm4
            elif event.key == pygame.K_RIGHT:
                to_x += 10
                xodzm = xodzm3
            elif event.key == pygame.K_UP:
                xodzm = xodzm2
                xodzm_Y_pos = 20
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            xodzm = xodzm1
            xodzm_Y_pos = 500
    if to1_Y_pos < 20:
        to1_Y_pos += 10
    if to2_Y_pos < 20:
        to2_Y_pos += 10
    
    if xodzm_X_pos+160 >= to1_X_pos+100 and to1_X_pos+100 >= xodzm_X_pos+40:
        if xodzm == xodzm2:
            to1_hp -= r.randint(10,100)
    if xodzm_X_pos+160 >= to2_X_pos+100 and to2_X_pos+100 >= xodzm_X_pos+40:
        if xodzm == xodzm2:
            to2_hp -= r.randint(10,100)
    if to1_hp <= 0:
        to1 = rmsqhs2
    if to2_hp <= 0:
        to2 = rmsqhs2
    if to1 == rmsqhs2:
        to1_Y_pos += 20
    if to2 == rmsqhs2:
        to2_Y_pos += 20
    if to1_Y_pos >= 400:
        to1_X_pos = r.randint(100,1100)
        to1 = rmsqhs1
        to1_Y_pos = -200
        kill -= 1
        to1_hp = rmshp
    if to2_Y_pos >= 400:
        to2_X_pos = r.randint(100,1100)
        to2 = rmsqhs1
        to2_Y_pos = -200
        kill -= 1
        to2_hp = rmshp

    xodzm_X_pos += to_x
    if xodzm_X_pos <= 0:
        xodzm_X_pos = 0
    if xodzm_X_pos >= 1100:
        xodzm_X_pos = 1100
    screen.blit(background, (0,0))
    screen.blit(to1, (to1_X_pos,to1_Y_pos))
    screen.blit(to2, (to2_X_pos,to2_Y_pos))
    screen.blit(xodzm, (xodzm_X_pos,xodzm_Y_pos))

    myFontto1 = pygame.font.SysFont("Arial", 30, True, False)
    text_pointto1 = myFontto1.render("HP:" + str(to1_hp), True, (160,0,160))
    screen.blit(text_pointto1, (to1_X_pos+56,to1_Y_pos+150))

    myFontto2 = pygame.font.SysFont("Arial", 30, True, False)
    text_pointto2 = myFontto2.render("HP:" + str(to2_hp), True, (160,0,160))
    screen.blit(text_pointto2, (to2_X_pos+56,to2_Y_pos+150))

    if kill > 50 and kill <= 100:
        rmsqhs1 = ento1
        rmsqhs2 = ento2
        rmshp = entohp
    if kill > 0 and kill <= 50:
        rmsqhs1 = vlto1
        rmsqhs2 = vlto2
        rmshp = vltohp
    if kill <= 0:
        kill = 0
        to1_Y_pos = -400
        to2_Y_pos = -400
        screen.blit(qhtm, (qhtm_X_pos,qhtm_Y_pos))
        if qhtm_Y_pos <= 10:
            qhtm_Y_pos += 20
        




    myFont = pygame.font.SysFont("Arial", 30, True, False)
    text_point2 = myFont.render("KILL : " + str(kill), True, (255,0,0))
    screen.blit(text_point2, (10,1))

    myFont2 = pygame.font.SysFont("Arial", 300, True, False)
    text_point3 = myFont2.render("clear", True, (0,150,150))
    #screen.blit(text_point3, (300,150))

    pygame.display.update()

pygame.quit()