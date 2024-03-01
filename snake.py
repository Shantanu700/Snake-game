import pygame
import random
import os
import sys
pygame.init()
screen=pygame.display.set_mode((640,770))
pygame.display.set_caption("Snake Game by Shantanu")
hi_img = pygame.image.load('sprites/trophy.png')
hi_img = pygame.transform.scale(hi_img,(40,40))
food_img = pygame.image.load('sprites/doughnut.png')
food_img = pygame.transform.scale(food_img,(40,40))
clock = pygame.time.Clock()
r1 = random.randint(0,255)
g1 = random.randint(0,255)
b = random.randint(0,255)
red = (255,125,0)
blue = (0,155,255)
green = (0,200,155)
color = random.choice((red,blue,green))
c_music = 0
def scor(s,h):
	font = pygame.font.Font('fonts/Grand9K Pixel.ttf',40)
	l = font.render('     :'+ str(s),True,(0, 255, 255))
	i = font.render('    :'+str(h),True,(0, 255, 255))
	screen.blit(l,(20,0))
	screen.blit(i,(250,0))
def plot(snk,col):
	r_in = 255
	g_in = 0
	b_in = 0
	inc = 25.5
	if col in (0,1):
		for x in snk[5:]:
			pygame.draw.circle(screen,color,x,10)
		for index,x in enumerate(snk[4::-1]):
			pygame.draw.circle(screen,color,x,(10-(index**2)))
		if col == 0:
			for c in range(5,len(snk)-5,7):
				for j in range(c,c+4):
					pygame.draw.circle(screen,(255,255,255),snk[j],10)
		elif col == 1:
			for i in range(5,len(snk),3):
				pygame.draw.circle(screen,(255,255,255),snk[i],10)
	else:
		for index,x in enumerate(snk[4::-1]):
			pygame.draw.circle(screen,("RED"),x,(10-(index**2)))
		for i in range(5,len(snk)):
			pygame.draw.circle(screen,(r_in,g_in,b_in),snk[i],10)
			if r_in == 255 and g_in < 255 and b_in == 0:
				g_in += inc
			elif r_in > 0 and g_in == 255 and b_in == 0:
				r_in -= inc
			elif r_in == 0 and g_in == 255 and b_in < 255:
				b_in += inc
			elif r_in == 0 and g_in > 0 and b_in == 255:
				g_in -= inc
			elif r_in < 255 and g_in == 0 and b_in == 255:
				r_in += inc
			elif r_in == 255 and g_in == 0 and b_in > 0:
				b_in -= inc
def over(s):
	screen.fill((0,0,0))
	font = pygame.font.Font('fonts/PIXY.ttf',40)
	font1 = pygame.font.Font('fonts/Grand9K Pixel.ttf',50)
	l = font1.render('Snake is dead',True,(0,0,255))
	s = font.render('Score : '+str(s),True,(255,255,0))
	screen.blit(l,(screen.get_width()/4-80,screen.get_height()/2-90))
	screen.blit(s,(screen.get_width()/4-80,screen.get_height()/2-130))
def loop():
	global color,de,c_music
	color = random.choice((red,blue,green))
	de = random.choice((0,1,2))
	clock = pygame.time.Clock()
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
	t_offsetx = 0
	t_offsety = 0
	snk_list = []
	score = 0
	food_x = random.randint(50,500)
	food_y = random.randint(50,500)
	food_velocity_x = random.choice([0,5,-5])
	food_velocity_y = random.choice([0,5,-5])
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	if not os.path.exists('hiscore.txt'):
	    f = open('hiscore.txt','w')
	    f.write('0')
	    f.close()
	with open('hiscore.txt','r') as f:
	    data = f.read()
	    hi_score = int(data) 
	while True:
		screen.fill((0,0,0))
		screen.blit(hi_img,(250,15))
		screen.blit(food_img,(20,15))
		clock.tick(60)
		if position_x < 15 or position_y < 15 or position_x > screen.get_width()-15 or position_y > screen.get_height()-15:
			game_over = True
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
			if c_music == 0:
				pygame.mixer.music.load('sounds//die.ogg')
				pygame.mixer.music.play()
				c_music = 1
			velocity = 0
			over(score)
			with open('hiscore.txt','w') as f:
			    f.write(str(hi_score))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						game_over = False
						c_music = 0
						loop()
						r = random.randint(0,255)
						g = random.randint(0,255)
						b = random.randint(0,255)
		else:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_y:
						if velocity_y != velocity:
							velocity_x = 0
							velocity_y = -velocity
							l = 1.5
							i = 20
							x = gap
							y = 0
							t_offsety = -20
							t_offsetx = 0
					if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_g:
						if velocity_x != velocity:
							velocity_x = -velocity
							velocity_y = 0
							l = 20
							i = 1.5
							x = 0
							y = gap
							t_offsety = 0
							t_offsetx = -20
					if event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_j:
						if velocity_x != -velocity:
							velocity_x = velocity
							velocity_y = 0
							l = 20
							i = 1.5
							x = 0
							y = gap
							t_offsety = 0
							t_offsetx = 0
					if event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_h:
						if velocity_y != -velocity:
							velocity_x = 0
							velocity_y = velocity
							l = 1.5
							i = 20
							x = gap
							y = 0
							t_offsety = 0
							t_offsetx = 0
			position_x += velocity_x
			position_y += velocity_y
			ix += velocity_x
			iy += velocity_y
			food_x += food_velocity_x
			food_y += food_velocity_y
			if abs(position_x - food_x) <= 10 and abs(position_y - food_y) <= 10:
				pygame.mixer.music.load('sounds//point.ogg')
				pygame.mixer.music.play()
				food_x = random.randint(100,500)
				food_y = random.randint(100,500)
				r = random.randint(150,255)
				g = random.randint(150,255)
				b = random.randint(150,255)
				food_velocity_x = random.choice([0, 5, -5])
				food_velocity_y = random.choice([0, 5, -5])
				score += 10
				snk_len += 10
			if abs(position_x - food_x) <= 50 and abs(position_y - food_y) <= 50:
				pygame.draw.rect(screen,(255,0,0),[position_x+t_offsetx,position_y+t_offsety,l,i])
				if score >= hi_score:
				    hi_score = score
			if food_x <= 15 or food_x >= screen.get_width()-15:
				food_velocity_x *= -1
			if food_y <= 15 or food_y >= screen.get_height()-15:
				food_velocity_y *= -1
			head =[]
			head.append(position_x)
			head.append(position_y)
			snk_list.append(head)
			clock.tick(60)
			pygame.draw.rect(screen,(131, 111, 255),[0,0,screen.get_width(),screen.get_height()],10,50)
			if head in snk_list[:-2]:
				game_over = True
			if snk_len < len(snk_list):
				del snk_list[0]
			last = snk_list[0]
			scor(score,hi_score)
			plot(snk_list,de)
			pygame.draw.circle(screen,(r,g,b),[food_x, food_y],7,4)
			pygame.draw.circle(screen,(0,0,0),[ix-x, iy+y],2)
			pygame.draw.circle(screen,(0,0,0),[ix+x, iy-y],2)
		pygame.display.update()
loop()
