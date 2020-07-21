from Image import Image 

img = Image('3e8.png')

print(img.getWidth(), img.getHeight())

p = img.getPixel(3,3)

print(p.color)

p.color = [255, 0,0,255]
p = img.getPixel(3,4)
p.setColor(0,255,0)


W = img.getWidth()
H = img.getHeight()

for x in range(0, W//2):
	for y in range(0, H):
		pixel = img.getPixel(x, y)
		mirroredPixel = img.getPixel(W-x-1, y)
		c = pixel.color
		pixel.color = mirroredPixel.color
		mirroredPixel.color = c
		#sleep(0)
		#print(pixel)

img.show()