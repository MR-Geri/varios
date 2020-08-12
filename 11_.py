from PIL import Image

image = Image.open('cave.jpg')
w, h = image.size
new = Image.new('RGB', (w, h))
for x in range(0, w, 2):
    for y in range(0, h, 2):
        ev = image.getpixel((x, y))
        ob = image.getpixel((x + 1, y + 1))
        new.putpixel((x, y), ev)
        new.putpixel((x + 1, y + 1), ob)
new.save('cave_new.png')
# Просто рисуем пиксели через один
new_w = Image.new('RGB', (w, h))
for x in range(w):
    for y in range(h):
        if x % 2 != 0 and y % 2 != 0:
            ev = image.getpixel((x, y))
            new_w.putpixel((x, y), ev)
new_w.save('cave_new_w.png')
