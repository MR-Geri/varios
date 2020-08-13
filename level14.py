from PIL import Image


im = Image.open('wire.png')
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
new = Image.new('RGB', [100, 100])
x, y, p = -1, 0, 0
d = 200
while d / 2 > 0:
    for v in delta:
        for s in range(d // 2):
            x, y = x + v[0], y + v[1]
            new.putpixel((x, y), im.getpixel((p, 0)))
            p += 1
        d -= 1
new.save('wire_new.png')
