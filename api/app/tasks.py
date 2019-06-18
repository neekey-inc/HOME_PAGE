import json

import requests
from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import get_template

import proj.settings as settings


# メール送信
# @shared_task
# def send_email(message):
#     subject = 'データ更新'
#     from_address = 'from@gmail.com'
#     to_address = ['to@gmail.com']
#     send_mail(subject, message, from_address, to_address)


# Slack投稿(Incoming Webhook)
@shared_task
def send_slack_message(message):
    requests.post(settings.SLACK_WEBHOOK_ENDPOINT,
                  data=json.dumps({
                      'text': message,    # 投稿するテキスト
                      'username': u'me',  # 投稿のユーザー名
                      'icon_emoji': u':ghost:',  # 投稿のプロフィール画像に入れる絵文字
                      'link_names': 1,  # メンションを有効にする
                  }))


# メールの本文を作成する
# def get_message(item, action):
#     template = get_template('app/message.txt')
#     context = {
#         "item": item, "action": action,
#     }
#     message = template.render(context)
#     return message


# 通知処理
def send_notification(objects, action):
    message = get_message(item, action)
    send_slack_message.delay(message)
    send_email.delay(message)