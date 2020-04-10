# Wrapper class for PyGame

import pygame
from pygame.locals import *
from sys import exit

class Game:

	# Color Constants
	Black = (0,0,0)
	White = (255,255,255)
	Red = (255,0,0)
	Lime = (0,255,0)
	Blue = (0,0,255)
	Yellow = (255,255,0)
	Cyan = (0,255,255)
	Magenta = (255,0,255)
	Silver = (192,192,192)
	Grey = (128,128,128)
	Maroon = (128,0,0)
	Olive = (128,128,0)
	Green = (0,128,0)
	Purple = (128,0,128)
	Teal = (0,128,128)
	Navy = (0,0,128)
	
	def __init__(self,width,height,caption="Game",render=0,depth=32):
		pygame.init()
		self.width = width
		self.height = height
		self.dimensions = (width,height)
		self.screen = pygame.display.set_mode(self.dimensions,render,depth)
		self.font = None
		pygame.display.set_caption(caption)

	def setfont(self,font,size):
		self.font = pygame.font.SysFont(font,size)


	def write(self,text,x,y,rgb=(0,0,0)):
		self.screen.blit(self.font.render(text,True,rgb),(x,y))


	def fillscreen(self,rgb=(255,255,255)):
		self.screen.fill(rgb)


	def listen(self):
		event = pygame.event.wait()
		return event

	def get_events(self):
		events = pygame.event.get()
		return events

	def get_dimensions(self):
		return self.dimensions

	def get_width(self):
		return self.width

	def get_height(self):
		return self.height

	def close(self):
		exit()

	def update(self):
		pygame.display.update()

# Inheritance - YAY!
class Shape:

	def __init__(self,color,width=0):
		self.color = color
		self.width = width
		self.bounds = None

	def showbounds(self,surface):
		left = self.bounds.left
		top = self.bounds.top
		width = self.bounds.width
		height = self.bounds.height
		pygame.draw.rect(surface,Game.Red,pygame.Rect(left,top,width,height),1)


class Circle(Shape):

	def __init__(self,center,radius,color,width=0):
		super().__init__(color,width)
		self.center = center
		self.r = radius

	def draw(self,surface):
		self.bounds = pygame.draw.circle(surface,self.color,self.center,self.r,self.width)

class Rect(Shape):

	def __init__(self,x,y,w,h,color,width=0):
		super().__init__(color,width)
		self.left = x
		self.top = y
		self.w = w
		self.h = h

	def draw(self,surface):
		self.bounds = pygame.draw.rect(surface,self.color,
			      pygame.Rect(self.left,self.top,self.w,self.h),self.width)


class Line(Shape):
	
	def __init__(self,start,end,color,width=1):
		super().__init__(color,width)
		self.start = start #(x,y)
		self.end = end

	def draw(self,surface):
		self.bounds = pygame.draw.line(surface,self.color,self.start,self.end,self.width)

class Image:

	def __init__(self,fname,alpha=False):
		self.path = fname
		self.surface = pygame.image.load(self.path)
		self.alpha = alpha

	def render(self,surface,pos):
		if self.alpha:
			surface.blit(self.surface.convert(),pos)
		else:
			surface.blit(self.surface.convert_alpha(),pos)
		
# Seperate class for Mouse?

g = Game(300,300)
g.fillscreen()
g.setfont("arial",16)

while True:
	for event in g.get_events():
		if event.type == QUIT:
			g.close()

	#g.write("Hello, World!",g.get_width()/2,g.get_height()/2)
	#rect = Rect(50,50,100,100,Game.Blue)
	#rect.draw(g.screen)
	#rect.showbounds(g.screen)

	#circ = Circle((200,200),35,Game.Grey)
	#circ.draw(g.screen)
	#circ.showbounds(g.screen)

	img = Image('./reference.png')
	img.render(g.screen,(0,0))	

	g.update()
