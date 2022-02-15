import pygame
import random
import os
import sys
pygame.init()
screen=pygame.display.set_mode((640,770))
hi_img = pygame.image.load('sprites/trophy.png')
hi_img = pygame.transform.scale(hi_img,(40,40))
food_img = pygame.image.load('sprites/doughnut.png')
food_img = pygame.transform.scale(food_img,(40,40))
clock = pygame.time.Clock()
r1 = random.randint(0,255)
g1 = random.randint(0,255)
b = random.randint(0,255)
de = random.choice((0,1))
de = 1
red = (255,125,0)
blue = (0,155,255)
green = (0,200,155)
color = random.choice((red,blue,green))
def scor(s,h):
	font = pygame.font.SysFont('Sans',50)
	l = font.render('    :'+ str(s),True,(0,255,255))
	i = font.render('   :'+str(h),True,(0,255,255))
	screen.blit(l,(20,0))
	screen.blit(i,(250,0))
def plot(snk):
    global de
    for x in snk:
        pygame.draw.circle(screen,color,x,10)
    if de == 0:
        for c in range(1,len(snk)-5,7):
            for j in range(c,c+4):
                pygame.draw.circle(screen,(255,255,255),snk[j],10)
    elif de == 1:
        for i in range(0,len(snk),3):
            pygame.draw.circle(screen,(255,255,255),snk[i],10)
def over(s):
	screen.fill((0,0,0))
	font = pygame.font.SysFont('Sans',40)
	font1 = pygame.font.SysFont('Sans',70)
	l = font1.render('Saanp mar gaya !',True,(0,0,255))
	s = font.render('Score :'+str(s),True,(255,255,0))
	screen.blit(l,(screen.get_width()/4-80,screen.get_height()/2-100))
	screen.blit(s,(screen.get_width()/4-80,screen.get_height()/2-130))
def loop():
	global color,de
	color = random.choice((red,blue,green))
	de = random.choice((0,1))
	clock=pygame.time.Clock()
	position_x = 100
	position_y = 100
	velocity_x = 0
	velocity_y = 0
	velocity = 7
	game_over = False
	ix = 100
	iy = 100
	x = 0
	gap = 4
	y = gap
	snk_len = 1
	l = 20
	i = 1.5
	snk_list = []
	score = 0
	food_x = random.randint(50,500)
	food_y = random.randint(50,500)
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	check = os.path.exists('hiscore.txt')
	if not check:
	    f = open('hiscore.txt','w')
	    f.write('0')
	    f.close()
	with open('hiscore.txt','r') as f:
	    data = f.read()
	    hi_score = int(data) 
	sound = pygame.mixer.Sound('sounds/point.ogg')
	hit = pygame.mixer.Sound('sounds/hit.ogg')
	while True:
		screen.fill((0,0,0))
		screen.blit(hi_img,(250,10))
		screen.blit(food_img,(20,10))
		clock.tick(60)
		if position_x < 0 or position_y < 0 or position_x > screen.get_width() or position_y > screen.get_height():
			game_over = True
			hit.play()
			pygame.mixer.music.load('sounds/die.ogg')
			pygame.mixer.music.play()
			if position_x < 0:
				position_x = screen.get_width()
				ix = screen.get_width()
			if position_x > screen.get_width():
				position_x = 0
				ix = 0
			if position_y < 0:
				position_y = 770
				iy = 770
			if position_y > 770:
				position_y = 0
				iy = 0
		if game_over == True:
			velocity = 0
			over(score)
			with open('hiscore.txt','w') as f:
			    f.write(str(hi_score))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
				    pygame.quit()
				    sys.quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						game_over = False
						loop()
						r = random.randint(0,255)
						g = random.randint(0,255)
						b = random.randint(0,255)				
		else:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
				    pygame.quit()
				    sys.quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_w:
						if velocity_y != velocity:
							velocity_x = 0
							velocity_y = -velocity
							l = 1.5
							i = -20
							x = gap
							y = 0
					if event.key == pygame.K_a:
						if velocity_x != velocity:
							velocity_x = -velocity
							velocity_y = 0
							l = -20
							i = 1.5
							x = 0
							y = gap
					if event.key == pygame.K_s:
						if velocity_x != -velocity:
							velocity_x = velocity
							velocity_y = 0
							l = 20
							i = 1.5
							x = 0
							y = gap
					if event.key == pygame.K_z:
						if velocity_y != -velocity:
							velocity_x = 0
							velocity_y = velocity
							l = 1.5
							i = 20
							x = gap
							y = 0
			position_x += velocity_x
			position_y += velocity_y
			ix += velocity_x
			iy += velocity_y
			if abs(position_x - food_x) <= 10 and abs(position_y - food_y) <= 10:
				food_x = random.randint(100,500)
				food_y = random.randint(100,500)
				r = random.randint(150,255)
				g = random.randint(150,255)
				b = random.randint(150,255)
				score += 10
				snk_len += 10
				if score >= hi_score:
				    hi_score = score
				sound.play()
			head =[]
			head.append(position_x)
			head.append(position_y)
			snk_list.append(head)
			clock.tick(60)
			pygame.draw.rect(screen,(255,0,0),[position_x, position_y,l,i])
			if head in snk_list[:-2]:
				hit.play()
				game_over = True
				pygame.mixer.music.load('sounds/die.ogg')
				pygame.mixer.music.play()
			if snk_len < len(snk_list):
				del snk_list[0]
			last = snk_list[0]
			scor(score,hi_score)
			plot(snk_list)
			pygame.draw.circle(screen,(r,g,b),[food_x, food_y],7,4)
			pygame.draw.circle(screen,(0,0,0),[ix-x, iy+y],2)
			pygame.draw.circle(screen,(0,0,0),[ix+x, iy-y],2)
		pygame.display.update()
loop()