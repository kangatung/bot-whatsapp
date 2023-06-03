import requests
import json

idInstance = '1101824663'
myToken = '60d5ff402e1d43749effc6cc84f86178325824a3c2f84a10b0'
urlGet = f"https://api.green-api.com/waInstance{idInstance}/receiveNotification/{myToken}"

x = 0
while x <= 100:
    myData = requests.get(urlGet)
    myByteData = myData.text.encode('utf8')
    myDictData = json.loads(myByteData.decode('utf-8'))

    print(myDictData)

    idLog = myDictData['receiptId']
    try:
        chatID = myDictData['body']['chatId']
    except:
        chatID = myDictData['body']['senderData']['chatId']

    urlDelete = f"https://api.green-api.com/waInstance{idInstance}/deleteNotification/{myToken}/{idLog}"
    deleteLog = requests.delete(urlDelete)
    print(deleteLog)
    print('\n\n')
    x += 1

