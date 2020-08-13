data = open("evil2.gfx", "rb").read()
for i in range(5):
    open(f'image_{i}.jpg', 'wb').write(data[i::5])
