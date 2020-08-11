# Задание 5 - http://www.pythonchallenge.com/pc/def/channel.html
import pickle


with open('banner.p', 'rb') as f:
    p = pickle.load(f)

for i in p:
    for j in i:
        print(j[0] * j[1], end=' ')
    print('')
