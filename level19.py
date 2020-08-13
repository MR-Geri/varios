import requests
import base64
import wave


response = requests.get('http://www.pythonchallenge.com/pc/hex/bin.html', auth=('butter', 'fly'))
b64 = ''.join(response.text.split('--===============1295515792==')[-2].split('\n')[4:-2])
h = open('indian.wav', 'wb')
h.write(base64.b64decode(b64))
h.close()
w = wave.open('indian.wav', 'rb')

h = wave.open("result.wav", "wb")

print(w.getnchannels())
print(w.getsampwidth())
print(w.getframerate())
h.setnchannels(w.getnchannels())
h.setsampwidth(w.getsampwidth()//2)
h.setframerate(w.getframerate()*2)
frames = w.readframes(w.getnframes())
wave.big_endiana = 1
h.writeframes(frames)

h.close()
