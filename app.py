# LINE BOT SDK
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

# 相關套件

import os
import re

# 檔案

import config
import sequence
import student
import exam
import classes
import sequence


app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = str(event.message.text).upper().strip() # 使用者輸入的內容
    profile = line_bot_api.get_profile(event.source.user_id)
    user_name = profile.display_name #使用者名稱
    uid = profile.user_id # 發訊者ID
    
    ### 老師端功能開發
    if uid == config.TEACHER_LINE_ID:
        pass

    ### 學生端功能開發
    else:

        user = student.getUser(uid, user_name)

        if user['state'] == mode.STUDENT_NO_CLASS:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='很抱歉，您尚未被加入課程之中'))
        
        elif user['mode'] == mode.NORMAL:
            if re.match('功能介紹', msg):
                line_bot_api.push_message(uid,TextSendMessage(text='功能介紹'))
                
            elif re.match('顯示本周測驗結果', msg):
                if user['state'] == mode.STUDENT_NOT_TEST:
                    line_bot_api.push_message(uid,TextSendMessage(text='很抱歉，您本周尚未參與任何測驗'))
                
                elif user['state'] == mode.STUDENT_COMPLETE_HALF_TEST:
                    line_bot_api.push_message(uid,TextSendMessage(text='您完成了一份測驗，還有一份測驗'))
                    
                elif user['state'] == mode.STUDENT_COMPLETE_TEST:
                    line_bot_api.push_message(uid,TextSendMessage(text='您完成了所有測驗'))

            elif user['state'] == mode.STUDENT_NOT_TEST:
                if re.match('進行第一次測驗',msg):
                    student.userModeUpdate(user, mode.TESTING)
                    line_bot_api.push_message(uid, TextSendMessage(text='輸入OK開始考試'))
                    # update exam
                    # change state

            elif user['state'] == mode.STUDENT_COMPLETE_HALF_TEST:
                if re.match('進行第二次測驗',msg):
                    student.userModeUpdate(user, mode.TESTING)
                    #change state

            elif user['state'] == mode.STUDENT_COMPLETE_TEST:
                pass
            
            else:
                line_bot_api.push_message(uid,TextSendMessage(text='有任何相關問題請詢問老師'))
        
        elif user['mode'] == mode.TESTING:
            index = user['testing']['index']
            category = user['testing']['exam']
            
            exam = student.getExam(category, index)

            if re.match('OK', msg) and index == 0:
                line_bot_api.push_
                message(uid, TextSendMessage(text=exam['problem']))
                # line_bot_api push quick reply 
            
            elif msg in exam['option']:
                type = 'first' if user['state'] == mode.STUDENT_NOT_TEST else 'second'
                if msg == exam['answer']:
                    student.userScoreUpdate(user, type)
                line_bot_api.push_message(uid, TextSendMessage(text=exam['problem']))
                # line_bot_api push quick reply
                student.userExamUpdate(user, category, index+1)
                if index+1 == 10:
                    line_bot_api.push_message(uid, TextSendMessage(text=''))
                    student.userModeUpdate(user,mode.NORMAL)

            else: line_bot_api.push_message(uid, TextSendMessage(text='請專注考試'))

            # line_bot_api.push_message()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)