import requests
import time


idInstance = '1101824663'
myToken = '60d5ff402e1d43749effc6cc84f86178325824a3c2f84a10b0iuytg87'
urlPOST = f"https://api.green-api.com/waInstance{idInstance}/sendMessage/{myToken}"

text = input('Masukkan pesan anda: ')
payload = {
    "chatId": "62857021504251@c.us",
    "message": text
}
print(time.ctime())

sendChat = requests.post(urlPOST, json=payload)
print('Pesan berhasi dikirim')
