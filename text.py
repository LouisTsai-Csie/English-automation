from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

def getScore(score, type):
    msg = '第一次測驗總得分\n' if type == 'first' else '第二次測驗總得分'
    msg = (msg +  '測驗十題，共拿' + str(score) + '分')
    return TextSendMessage(text=msg)
    