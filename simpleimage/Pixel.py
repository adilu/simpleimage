class Pixel:
	def __init__(self, img, x, y):
		self.img = img
		self.__x = x
		self.__y = y
	def __getx(self):
		return self.__x
	x = property(__getx)
	def __gety(self):
		return self.__y
	y = property(__gety)
	def __getcolor(self):
		return self.img.getColorAtPos(self.x, self.y)
	def __setcolor(self, arr):
		return self.setColor(arr)
	color = property(__getcolor, __setcolor)
	def setColor(self, rOrArr, g=False, b=False, a=False):
		if hasattr(rOrArr, "__iter__") and 3 <= len(rOrArr) <= 4:
			return self.img.setColorAtPos(self.x, self.y, rOrArr)
		if a != False:
			return self.img.setColorAtPos(self.x, self.y, [rOrArr, g, b, a])
		return self.img.setColorAtPos(self.x, self.y, [rOrArr, g, b, self.alpha])
	def __getred(self):
		return self.img.getChannelAtPos(self.x, self.y, 0)
	def __setred(self, val):
		return self.img.setChannelAtPos(self.x, self.y, 0, val)
	red = property(__getred, __setred)
	def __getGreen(self):
		return self.img.getChannelAtPos(self.x, self.y, 1)
	def __setGreen(self, val):
		return self.img.setChannelAtPos(self.x, self.y, 1, val)
	green = property(__getGreen, __setGreen)
	def __getBlue(self):
		return self.img.getChannelAtPos(self.x, self.y, 2)
	def __setBlue(self, val):
		return self.img.setChannelAtPos(self.x, self.y, 2, val)
	blue = property(__getBlue, __setBlue)
	def __getAlpha(self):
		return self.img.getChannelAtPos(self.x, self.y, 3)
	def __setAlpha(self, val):
		return self.img.setChannelAtPos(self.x, self.y, 3, val)
	alpha = property(__getAlpha, __setAlpha)
	def __str__(self):
		return "Pixel(%d,%d): {red: %d, green: %d, blue: %d, alpha: %d}"%(self.x, self.y, self.red, self.green, self.blue, self.alpha)
	def getNeighbors(self):
		neighbors = []
		x = self.x
		y = self.y
		H = self.img.getHeight()
		W = self.img.getWidth()
		if y > 0:
			neighbors.append(self.img.getPixel(x, y-1))
		if y < H-1:
			neighbors.append(self.img.getPixel(x, y+1))
		if x > 0:
			neighbors.append(self.img.getPixel(x-1, y))
		if x < W-1:
			neighbors.append(self.img.getPixel(x+1, y))
		return neighbors