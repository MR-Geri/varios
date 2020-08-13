from PIL import Image

image = Image.open('cave.jpg')
w, h = image.size
# Просто рисуем пиксели через один
new_w = Image.new('RGB', (w, h))
for x in range(w):
    for y in range(h):
        if x % 2 != 0 and y % 2 != 0:
            ev = image.getpixel((x, y))
            new_w.putpixel((x, y), ev)
new_w.save('cave_new_w.png')
