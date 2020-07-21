import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
from Pixel import Pixel

id = 0

class Image:
	def __init__(self, src):
		global id
		self.id = id
		id = id + 1
		self.data = self.open(src)
		self.pending = []
		
	def show(self):
		imgplot = plt.imshow(self.data)
		plt.show()

	def getId(self):
		return self.id    

	def runCommandImmediate(self, command, value):
		signal = False
		show({'command': command, 'value': value, 'readysignal': signal})

	def open(self, src):
		data = mpimg.imread(src)
		self.W = len(data[0])
		self.H = len(data)
		rgba = numpy.insert(
			data,
			3, #position in the pixel value [ r, g, b, a <-index [3]  ]
			255, # or 1 if you're going for a float data type as you want the alpha to be fully white otherwise the entire image will be transparent.
			axis=2, #this is the depth where you are inserting this alpha channel into
		)
		return rgba

	def getWidth(self):
		return self.W
	def getHeight(self):
		return self.H
	def getPixel(self, x, y):
		# memoize pixels: if not ((x,y) in self.pixels):
		# memoize pixels:     self.pixels[(x, y)] = Pixel(self, x, y)
		# memoize pixels: return self.pixels[(x, y)]
		return Pixel(self, x, y)
	def getColorAtPos(self, x, y):
		return self.data[y][x]
	def setColorAtPos(self, x, y, values):
		for i, v in enumerate(values):
			self.data[y][x][i] = v
	def getChannelAtPos(self, x, y, channel):
		return self.data[y][x][channel]
	def setChannelAtPos(self, x, y, channel, val):
		self.data[y][x][channel] = val