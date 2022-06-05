# import flask related
from flask import Flask, request, abort, url_for
from linebot.models import events
import os
from speechrecognition import *
from audioanalysis import *
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import messages
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, 
    PostbackEvent,
    TextMessage, 
    TextSendMessage,  
    TemplateSendMessage,
    ButtonsTemplate,
    PostbackAction,
    MessageAction,
)
line_bot_api = LineBotApi('HY3iXDRKdxHVWkEz33hEV6xlzzjbwq0ckWfuVB2V5WAuOVfx09CDQr618JlU5TQh8qXzIaUTWMOXbbnuhzeb+kWVy6MT09P7I7Mem6Io8LOK8JoAqlNQ27Ig8ApTBF7gviNPsTb1KNFD+XLctEPBQAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9a4a6e35cc2b3096dab16fc0fab764f0')


# create flask server
app = Flask(__name__)

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


@handler.add(MessageEvent)
def handle_something(event):
    if event.message.type=='text':
        recrive_text=event.message.text
        if '正音功能' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='錄製短時英文語音即可隨時開始'))
            line_bot_api.reply_message(event.reply_token, messages)
    elif event.message.type=='audio':
        filename_wav='temp_audio.wav'
        filename_mp3='temp_audio.mp3'
        message_content = line_bot_api.get_message_content(event.message.id)
        with open(filename_mp3, 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)
        os.system(f'ffmpeg -y -i {filename_mp3} {filename_wav} -loglevel quiet')
        text = speechtotext()
        texttospeech(text)
        nums = [SimilarityAnalysis1(),SimilarityAnalysis2(),SimilarityAnalysis3()]
        text1 = '{:.2%}'.format(1-min(nums)/1300)
        messages=[]
        messages.append(TextSendMessage(text))
        if text != 'No speech could be recognized':
            messages.append(TextSendMessage(text=f'相似度為{text1}'))     
        line_bot_api.reply_message(event.reply_token, messages)

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)