# simpleimage

This library provides a simple image API for educational purposes. It creates a thin wrapper around PIL and matplotlib. It's focused on simplicity, not on performance!

### class Image
  Example usage:
  ```
  from simpleimage import image
  img = Image('image.jpg')
  W = img.getWidth()
  H = img.getHeight()
  x = 3
  y = 5
  pixel = img.getPixelAt(x, y)
  ```
  
### class Pixel
Example usage:
```
# Get values
red = pixel.red
green = pixel.green
blue = pixel.blue
alpha = pixel.alpha
color = pixel.color  # [red, green, blue, alpha]

# set values
average = (red + green + blue) / 3
pixel.red = average
pixel.green = average
pixel.blue = average
# or:
pixel.color = [average, average, average] # alpha is optional
# or:
pixel.setColor(average, average, average)
```

### Installation

```
pip install simpleimage PIL matplotlib
```

### License

MIT
**Free Software**