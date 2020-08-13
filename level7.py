from PIL import Image


last = 608
ox = Image.open('oxygen.png')
y = 45
for x in range(0, last, 7):
    print(chr(ox.getpixel((x, y))[0]), end='')
print()
next_level = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for i in next_level:
    print(chr(i), end='')
