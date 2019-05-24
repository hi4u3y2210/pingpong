import pygame
import os
from pygame.locals import *
from random import randint

size = (700, 600)
red = (255, 0, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
gray = (150, 150 , 150)
blue = (50, 100, 150)
white = (255, 255, 255)
red_ = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
darkblue = (0, 0, 255)
title = "Ping Pong"
backgrd_image = pygame.image.load("pingpong.jpg")
backgrd_rect = backgrd_image.get_rect()

os.environ['SDL_VIDEO_WINDOW_POS'] = "{},{}".format(50,50)
screen = pygame.display.set_mode(size)
pygame.display.set_caption(title)
pygame.init()

backgrd_image = pygame.image.load("pingpong.jpg").convert()
backgrd_rect = backgrd_image.get_rect()
instr_image = pygame.image.load("instructions.jpg").convert()
instr_image = pygame.transform.scale(instr_image, (700, 600))
instr_rect = instr_image.get_rect()
clock = pygame.time.Clock()
game_end = True
replay = True

class Paddle1:	 #電腦
	def __init__(self, screen):
		self.screen = screen
		self.x = 310
		self.y = 1
		self.l = 80
		self.w = 10
		self.draw(black, (310, 1, 80, 5))
		self.draw(red, (310, 6, 80, 5))
	def move(self, color, point):
		self.draw(color, point)
		self.x = point[0]
		self.y = point[1]
		self.l = point[2]
		self.w = point[3]
	def draw(self, color, point):
		pygame.draw.rect(self.screen, color, point)

class Paddle2:	 #玩家
	def __init__(self, screen):
		self.screen = screen
		self.x = 310
		self.y = 589
		self.l = 80
		self.w = 10
		self.draw(red, (160, 589, 80, 5))
		self.draw(black, (160, 594, 80, 5))
	def move(self, color, point):
		self.draw(color, point)
		self.x = point[0]
		self.y = point[1]
		self.l = point[2]
		self.w = point[3]

	def draw(self, color, point):
		pygame.draw.rect(self.screen, color, point)

class Ball:	  #球
	def __init__(self, screen, radius):
		self.screen = screen
		self.x = 350
		self.y = 30
		self.draw(yellow, (350, 21), radius)
		
	def move(self, point, radius):
		self.draw(yellow, point, radius)
		self.x = point[0]
		self.y = point[1]
		
	def draw(self, color, point, radius):
		pygame.draw.circle(self.screen, color, point, radius)

def Mode():	  #電腦隨機模式回球
	return(str(randint(1, 3)))
		
def background(screen):	  #背景
	screen.fill(blue)
	pygame.draw.line(screen , white, (150, 0), (150, 600), 10)
	pygame.draw.line(screen , white, (150, 600), (550, 600), 10)
	pygame.draw.line(screen , white, (550, 600), (550, 0), 10)
	pygame.draw.line(screen , white, (150, 0), (550, 0), 10)
	pygame.draw.line(screen , white, (350, 0), (350, 600), 1)
	pygame.draw.line(screen , white, (141, 270), (560, 270), 4)
	pygame.draw.line(screen , darkblue, (150, 303), (550, 303), 2)
	pygame.draw.line(screen , darkblue, (150, 275), (550, 275), 1)
	pygame.draw.line(screen , darkblue, (150, 280), (550, 280), 1)
	pygame.draw.line(screen , darkblue, (150, 285), (550, 285), 1)
	pygame.draw.line(screen , darkblue, (150, 290), (550, 290), 1)
	pygame.draw.line(screen , darkblue, (150, 295), (550, 295), 1)
	pygame.draw.line(screen , darkblue, (150, 299), (550, 299), 1)
	pygame.draw.line(screen , black, (150, 305), (145, 270), 10)
	pygame.draw.line(screen , black, (550, 305), (555, 270), 10)
	
	pygame.draw.rect(screen, black, (570,450,64,8))
	pygame.draw.rect(screen, red, (570,500,64,4))
	pygame.draw.rect(screen, black, (570,505,64,4))
	pygame.draw.rect(screen, red, (570,550,64,8))
	font = pygame.font.SysFont("comicsansms", 20)
	text1 = font.render('1', True, white)
	text2 = font.render('2', True, white)
	text3 = font.render('3', True, white)
	screen.blit(text1, (660, 440)) 
	screen.blit(text2, (660, 490))
	screen.blit(text3, (660, 540))

def dxdy(ball):		#球的x, y變量
	dx = randint(0, 3) - (ball.x - 150) //100  
	dy = 6					
	return dx, int(dy)

def playerdxdy(ball, limit): #hard玩家回球模式
	segment = ball.x - limit
	if 0 <= segment and segment <= 10:
			dx = -3
	elif 10 <= segment and segment <= 20:
			dx = -2
	elif 20 <= segment and segment <= 30:
			dx = -1
	elif 30 <= segment and segment <= 50:
			dx = 0
	elif 50 <= segment and segment <= 60:
			dx = 1
	elif 60 <= segment and segment <= 70:
			dx = 2
	else:
			dx = 3
	dy = -6
	return dx, dy

def things_score(screen, count): #分數顯示
	font = pygame.font.SysFont(None, 40,)
	text = font.render("score: " + str(count), True, white)
	screen.blit(text, (570, 15))

def quitgame():
	pygame.quit()
	quit()

def button(screen, msg, x, y, w, h, ic, ac, action = None): #死掉後again, quit按鈕
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(screen, ac, (x, y, w, h))
		if click[0] == 1 and action != None:
			action(screen)		 
	else:
		pygame.draw.rect(screen, ic, (x, y, w, h))
	smallText = pygame.font.SysFont("comicsansms", 20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( (x + (w / 2)), (y + (h / 2)) )
	screen.blit(textSurf, textRect)		

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()
	
def game_over(screen):
	font = pygame.font.SysFont("Britannic Bold", 90)
	text = font.render("GAME OVER ", True, white)
	screen.blit(text, (165, 155))
	
	while game_end:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()
		
		button(screen, "Quit",415,400,100,50,red_,bright_red,restart)
		button(screen, "Play Again",180,400,100,50,green,bright_green, play_again)
		pygame.display.update()
		clock.tick(15)	
	
def restart(screen): #死掉點quit
	global game_end
	game_end = False
	global replay
	replay = False
	
def play_again(screen): #死掉點again
	global game_end
	game_end = False
	
def menu(screen):    #初始選單
	global game_end
	game_end = True
	font = pygame.font.SysFont("comicsansms", 40)
	while game_end:
		for event in pygame.event.get():
			if event.type == QUIT:
				quitgame()
 
		text1 = font.render("Play", True, white)
		text1_1 = font.render("Play", True, darkblue)
		text2 = font.render("Information", True, white)
		text2_1 = font.render("Information", True, darkblue)
		text3 = font.render("Quit", True, white)
		text3_1 = font.render("Quit", True, darkblue)
		text4 = font.render("Instructions", True, white)
		text4_1 = font.render("Instructions", True, darkblue)
 
		x, y = pygame.mouse.get_pos()

		screen.blit(backgrd_image, backgrd_rect.move(-80, 0))

 
		if 80 <= x <= 80 + text1.get_width() and 150 <= y <= 150 + text1.get_height():
			screen.blit(text1_1, (80, 150)) 
			screen.blit(text4, (80, 230))
			screen.blit(text2, (80, 310))
			screen.blit(text3, (80, 390))
			if pygame.mouse.get_pressed()[0]:
				global replay
				replay = True
				while replay:
					set_mode(screen)
		elif 80 <= x <= 80 + text4.get_width() and 230 <= y <= 230 + text1.get_height():
			screen.blit(text1, (80, 150)) 
			screen.blit(text4_1, (80, 230))
			screen.blit(text2, (80, 310))
			screen.blit(text3, (80, 390))
			if pygame.mouse.get_pressed()[0]:
				instructions(screen)
				
		elif 80 <= x <= 80 + text2.get_width() and 310 <= y <= 310 + text1.get_height():
			screen.blit(text1, (80, 150)) 
			screen.blit(text4, (80, 230))
			screen.blit(text2_1, (80, 310))
			screen.blit(text3, (80, 390))
			if pygame.mouse.get_pressed()[0]:
				info(screen)
		elif 80 <= x <= 80 + text3.get_width() and 390 <= y <= 390 + text1.get_height():
			screen.blit(text1, (80, 150)) 
			screen.blit(text4, (80, 230))
			screen.blit(text2, (80, 310))
			screen.blit(text3_1, (80, 390))
			if pygame.mouse.get_pressed()[0]:
				exit()
		else:
			screen.blit(text1, (80, 150)) 
			screen.blit(text4, (80, 230))
			screen.blit(text2, (80, 310))
			screen.blit(text3, (80, 390))
 
		pygame.display.update()

def instructions(screen):#玩法
	font3 = pygame.font.SysFont("Bradley Hand", 40)
	back = True
	while back:
		for event in pygame.event.get():
			if event.type == QUIT:
				quitgame()

		text7 = font3.render('BACK', True, white)
		text7_1 = font3.render('BACK', True, darkblue)
			
		x, y = pygame.mouse.get_pos()

		screen.fill((236, 203, 100))

		screen.blit(instr_image, instr_rect)

		if 550 <= x <= 550 + text7.get_width() and 550 <= y <= 550 + text7.get_height():
			screen.blit(text7_1, (550, 550))
			if pygame.mouse.get_pressed()[0]:
				back = False
		else:
			screen.blit(text7, (550, 550))
		
		pygame.display.update()

def set_mode(screen):#模式
	font = pygame.font.SysFont("Bradley Hand", 60)
	font1 = pygame.font.SysFont("Bradley Hand", 40)
	global difficulty
	while replay:
		for event in pygame.event.get():
			if event.type == QUIT:
				quitgame()
 
		text1 = font.render('Easy', True, white)
		text1_1 = font.render('Easy', True, darkblue)
		text2 = font.render('Moderate', True, white)
		text2_1 = font.render('Moderate', True, darkblue)
		text3 = font.render('Hard', True, white)
		text3_1 = font.render('Hard', True, darkblue)
		text4 = font1.render('BACK', True, white)
		text4_1 = font1.render('BACK', True, darkblue)
 
		x, y = pygame.mouse.get_pos()
 
		screen.fill((220, 170 ,0))
 
		if 250 <= x <= 250 + text1.get_width() and 150 <= y <= 150 + text1.get_height():
			screen.blit(text1_1, (250, 150)) 
			screen.blit(text2, (250, 270))
			screen.blit(text3, (250, 390))
			screen.blit(text4, (550, 550))
			difficulty = 0
			if pygame.mouse.get_pressed()[0]:
				while game_end:
					while replay:
						run()
		elif 250 <= x <= 250 + text2.get_width() and 270 <= y <= 270 + text1.get_height():
			screen.blit(text1, (250, 150)) 
			screen.blit(text2_1, (250, 270))
			screen.blit(text3, (250, 390))
			screen.blit(text4, (550, 550))
			difficulty = 1
			if pygame.mouse.get_pressed()[0]:
				while game_end:
					while replay:
						run()
		elif 250 <= x <= 250 + text3.get_width() and 390 <= y <= 390 + text1.get_height():
			screen.blit(text1, (250, 150)) 
			screen.blit(text2, (250, 270))
			screen.blit(text3_1, (250, 390))
			screen.blit(text4, (550, 550))
			difficulty = 2
			if pygame.mouse.get_pressed()[0]:
				while game_end:
					while replay:
						run()
		elif 550 <= x <= 550 + text3.get_width() and 550 <= y <= 550 + text1.get_height():
			screen.blit(text1, (250, 150)) 
			screen.blit(text2, (250, 270))
			screen.blit(text3, (250, 390))
			screen.blit(text4_1, (550, 550))
			if pygame.mouse.get_pressed()[0]:
				while game_end:
					while replay:
						menu(screen)
						break
		else:
			screen.blit(text1, (250, 150))
			screen.blit(text2, (250, 270))
			screen.blit(text3, (250, 390))
			screen.blit(text4, (550, 550))
		pygame.display.update()

def info(screen):    #簡介
	font = pygame.font.SysFont("Bradley Hand", 30)
	font2 = pygame.font.SysFont("Bradley Hand", 40)
	back = True
	while back:
		for event in pygame.event.get():
			if event.type == QUIT:
				quitgame()
 
		text1 = font2.render('Developers:', True, white)
		text2 = font.render('Bryan Wang', True, white)
		text3 = font.render('David Li', True, white)
		text4 = font.render('Kuo Hsin', True, white)
		text5 = font.render('Liu Ting Hua', True, white)
		text6 = font.render('BACK', True, white)
		text6_1 = font.render('BACK', True, darkblue)
		screen.blit(backgrd_image, backgrd_rect.move(-80, 0))
 
		screen.blit(text1, (80, 150))
		screen.blit(text2, (80, 230))
		screen.blit(text3, (80, 270))
		screen.blit(text4, (80, 310))
		screen.blit(text5, (80, 350))
		x, y = pygame.mouse.get_pos()

		if 550 <= x <= 550 + text1.get_width() and 550 <= y <= 550 + text1.get_height():
			screen.blit(text6_1, (550, 550))
			if pygame.mouse.get_pressed()[0]:
				back = False
		else:
			screen.blit(text6, (550, 550))
		pygame.display.update()
				
def run():		  	 #執行遊戲
	global game_end
	game_end = True
	global difficulty
	ball = Ball(screen, 10)
	paddle1 = Paddle1(screen)
	paddle2 = Paddle2(screen)	
	dx = 0
	dy = 5
	mode = "2"		   #電腦回球模式
	score = 0		   #分數
	playermode = "2"   #使用者輸入的擊球模式
	r = 10			   #半徑
	status = 0		#0代表球往下，1代表往上
	while game_end:	
		background(screen)
		things_score(screen, score)
		# Event Handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()
			elif event.type == pygame.KEYDOWN:	 #讀取玩家回球模式
				if event.key == K_1:
					playermode = "1"
				elif event.key == K_2:
					playermode = "2"
				elif event.key == K_3:
					playermode = "3"
				elif event.key == pygame.K_SPACE:#暫停
					while True:
						event = pygame.event.wait()		
						if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
							break
		limit = pygame.mouse.get_pos()[0] - 40	#鼠標x座標
		if limit > 550:
			limit = 550
		elif limit < 70:
			limit = 70
		
		if playermode == "1":
			paddle2.move(black, (limit, 589, 80, 10))
		elif playermode == "2":
			paddle2.move(red, (limit, 589, 80, 5))
			paddle2.move(black, (limit, 594, 80, 5))
		else:
			paddle2.move(red, (limit, 589, 80, 10))
		if difficulty > 1:
			paddle1.move(black, (ball.x - 40, 1, 80, 10))
		else:		
			if mode == "1":
				paddle1.move(black, (ball.x - 40, 1, 80, 10))
			elif mode == "2":
				paddle1.move(black, (ball.x - 40, 1, 80, 5))
				paddle1.move(red, (ball.x - 40, 6, 80, 5))
			else:
				paddle1.move(red, (ball.x - 40, 1, 80, 10))
		if ball.y > 579 and ball.y < 591:  #球到最下面且玩家有接到
			if	ball.x > limit and ball.x < limit + 80:
				status = 1
				if difficulty > 1:
					dx, dy = playerdxdy(ball, limit)
				else: 
					dx, dy = dxdy(ball)
					dy = -dy
				
				if difficulty > 0:
					if playermode == mode:
						score += 1
					else:
						font = pygame.font.SysFont("Bradley Hand", 25)
						text1 = font.render("mode : " + str(mode), True, white)
						text2 = font.render("player : " + str(playermode), True, white)
						screen.blit(text1, (245, 240))
						screen.blit(text2, (370, 240))
						game_over(screen)
				else:
					score += 1
			
		elif ball.y < 21:	  #球到最上面
			dx, dy = dxdy(ball)
			mode = Mode()
			status = 0
		elif ball.x < limit or ball.x > limit + 80:
			if ball.y > 609:
				game_over(screen)


		if status == 0 :			#球往下
			if score == 0:
				if ball.y >= 100 and ball.y < 120:
					ball.move((ball.x + dx, ball.y + dy), r - 1)
				elif ball.y >= 120 and ball.y < 135:
					ball.move((ball.x + dx, ball.y + dy), r - 2)
				elif ball.y >= 135 and ball.y < 165:
					ball.move((ball.x + dx, ball.y + dy), r - 3)
				elif ball.y >= 165 and ball.y < 180:
					ball.move((ball.x + dx, ball.y + dy), r - 2)
				elif ball.y >= 180 and ball.y < 250:
					ball.move((ball.x + dx, ball.y + dy), r - 1)
				elif ball.y >= 350 and ball.y < 380:
					ball.move((ball.x + dx, ball.y + dy), r - 1)
				elif ball.y >= 380 and ball.y < 405:
					ball.move((ball.x + dx, ball.y + dy), r - 2)
				elif ball.y >= 405 and ball.y <= 420:
					ball.move((ball.x + dx, ball.y + dy), r - 3)
				elif ball.y >= 420 and ball.y < 430:
					ball.move((ball.x + dx, ball.y + dy), r - 2)
				elif ball.y >= 430 and ball.y < 450:
					ball.move((ball.x + dx, ball.y + dy), r - 1)
				else:
					ball.move((ball.x + dx, ball.y + dy), r )
			else:
				if mode == "1":
					if ball.y >= 290 and ball.y < 350:
						ball.move((ball.x + dx, ball.y + dy), r - 1)
					elif ball.y >= 350 and ball.y < 365:
						ball.move((ball.x + dx, ball.y + dy), r - 2)
					elif ball.y >= 365 and ball.y <= 395:
						ball.move((ball.x + dx, ball.y + dy), r - 3)
					elif ball.y >= 395 and ball.y < 411:
						ball.move((ball.x + dx, ball.y + dy), r - 2)
					else:
						ball.move((ball.x + dx, ball.y + dy), r - 1)
				elif mode == "2":
					if ball.y >= 300 and ball.y < 350:
						ball.move((ball.x + dx, ball.y + dy), r - 1)
					elif ball.y >= 350 and ball.y < 375:
						ball.move((ball.x + dx, ball.y + dy), r - 2)
					elif ball.y >= 375 and ball.y <= 405:
						ball.move((ball.x + dx, ball.y + dy), r - 3)
					elif ball.y >= 405 and ball.y < 421:
						ball.move((ball.x + dx, ball.y + dy), r - 2)
					elif ball.y >= 421 and ball.y < 450:
						ball.move((ball.x + dx, ball.y + dy), r - 1)
					else:
						ball.move((ball.x + dx, ball.y + dy), r )
				else:
					if ball.y >= 260 and ball.y < 310:
						ball.move((ball.x + dx, ball.y + dy), r - 1)
					elif ball.y >= 310 and ball.y < 340:
						ball.move((ball.x + dx, ball.y + dy), r - 1)
					elif ball.y >= 340 and ball.y < 375:
						ball.move((ball.x + dx, ball.y + dy), r - 2)
					elif ball.y >= 375 and ball.y <= 415:
						ball.move((ball.x + dx, ball.y + dy), r - 3)
					elif ball.y >= 415 and ball.y < 431:
						ball.move((ball.x + dx, ball.y + dy), r - 2)
					elif ball.y >= 431 and ball.y < 450:
						ball.move((ball.x + dx, ball.y + dy), r - 1)
					elif ball.y >= 450 and ball.y < 470:
						ball.move((ball.x + dx, ball.y + dy), r )
					elif ball.y >= 540:
						ball.move((ball.x + dx, ball.y + dy), r )
					else:
						ball.move((ball.x + dx, ball.y + dy), r + 1)

		elif status == 1:		  #球往上
			if mode == "1":
				if ball.y <= 300 and ball.y > 250:
					ball.move((ball.x + dx, ball.y + dy), r - 1)
				elif ball.y <= 250 and ball.y > 235:
					ball.move((ball.x + dx, ball.y + dy), r - 2)
				elif ball.y <= 235 and ball.y <= 205:
					if ball.x <= 545 and ball.x >= 155:
						ball.move((ball.x + dx, ball.y + dy), r - 3)
					else:
						if difficulty > 1:
							ball.move((ball.x + dx, ball.y + dy), r - 3)
							ball.move((ball.x + dx*2, ball.y + dy*2), r - 4)
							ball.move((ball.x + dx*3, ball.y + dy*3), r - 5)
							ball.move((ball.x + dx*4, ball.y + dy*4), r - 6)
							ball.move((ball.x + dx*5, ball.y + dy*5), r - 7)
							ball.move((ball.x + dx*6, ball.y + dy*6), r - 8)
							ball.move((ball.x + dx*7, ball.y + dy*6), r - 9)
							game_over(screen)
				elif ball.y <= 205 and ball.y < 189:
					ball.move((ball.x + dx, ball.y + dy), r - 2)
				else:
					ball.move((ball.x + dx, ball.y + dy), r - 1)
			elif mode == "2":
				if ball.y <= 290 and ball.y > 240:
					ball.move((ball.x + dx, ball.y + dy), r - 1)
				elif ball.y <= 240 and ball.y > 215:
					ball.move((ball.x + dx, ball.y + dy), r - 2)
				elif ball.y <= 215 and ball.y >= 185:
					if ball.x <= 545 and ball.x >= 155:
						ball.move((ball.x + dx, ball.y + dy), r - 3)
					else:
						if difficulty > 1:
							ball.move((ball.x + dx, ball.y + dy), r - 3)
							ball.move((ball.x + dx*2, ball.y + dy*2), r - 4)
							ball.move((ball.x + dx*3, ball.y + dy*3), r - 5)
							ball.move((ball.x + dx*4, ball.y + dy*4), r - 6)
							ball.move((ball.x + dx*5, ball.y + dy*5), r - 7)
							ball.move((ball.x + dx*6, ball.y + dy*6), r - 8)
							ball.move((ball.x + dx*7, ball.y + dy*7), r - 9)
							game_over(screen)
				elif ball.y <= 185 and ball.y > 169:
					ball.move((ball.x + dx, ball.y + dy), r - 2)
				elif ball.y <= 169 and ball.y > 140:
					ball.move((ball.x + dx, ball.y + dy), r - 1)
				else:
					ball.move((ball.x + dx, ball.y + dy), r )
			else:
				if ball.y <= 60:
					ball.move((ball.x + dx, ball.y + dy), r)
				elif ball.y <= 310 and ball.y > 280:
					ball.move((ball.x + dx, ball.y + dy), r)
				elif ball.y <= 280 and ball.y > 250:
					ball.move((ball.x + dx, ball.y + dy), r - 1)
				elif ball.y <= 250 and ball.y > 215:
					ball.move((ball.x + dx, ball.y + dy), r - 2)
				elif ball.y <= 215 and ball.y >= 175:
					if ball.x <= 545 and ball.x >= 155:
						ball.move((ball.x + dx, ball.y + dy), r - 3)
					else:
						if difficulty > 1:
							ball.move((ball.x + dx, ball.y + dy), r - 3)
							ball.move((ball.x + dx*2, ball.y + dy*2), r - 4)
							ball.move((ball.x + dx*3, ball.y + dy*3), r - 5)
							ball.move((ball.x + dx*4, ball.y + dy*4), r - 6)
							ball.move((ball.x + dx*5, ball.y + dy*5), r - 7)
							ball.move((ball.x + dx*6, ball.y + dy*6), r - 8)
							ball.move((ball.x + dx*7, ball.y + dy*7), r - 9)
							game_over(screen)
				elif ball.y < 175 and ball.y > 159:
					ball.move((ball.x + dx, ball.y + dy), r - 2)
				elif ball.y <= 159 and ball.y > 140:
					ball.move((ball.x + dx, ball.y + dy), r - 1)
				elif ball.y <= 140 and ball.y > 120:
					ball.move((ball.x + dx, ball.y + dy), r )
				else:
					ball.move((ball.x + dx, ball.y + dy), r + 1)

		pygame.display.update()
		if score < 5:
			if mode == "1":			 #三種球
				clock.tick(80)
			elif mode == "2":
				clock.tick(50)
			elif mode == "3":
				clock.tick(20)
		elif score < 10 and score >= 5:
			if mode == "1":			 #三種球
				clock.tick(100)
			elif mode == "2":
				clock.tick(70)
			elif mode == "3":
				clock.tick(40)
		elif score < 15 and score >= 10:
			if mode == "1":			 #三種球
				clock.tick(120)
			elif mode == "2":
				clock.tick(90)
			elif mode == "3":
				clock.tick(60)
		else:
			if mode == "1":			 #三種球
				clock.tick(150)
			elif mode == "2":
				clock.tick(95)
			elif mode == "3":
				clock.tick(80)

while True:				
	menu(screen)
