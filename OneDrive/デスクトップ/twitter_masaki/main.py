import tweepy
import configparser
import json
from requests_oauthlib import OAuth1Session
import pandas as pd
import random
import time
import schedule
import random

conf = configparser.ConfigParser()
conf.read('config.ini')


API_KEY = conf['twitter']['API_KEY']
API_SECRET = conf['twitter']['API_SECRET']
ACCESS_TOKEN = conf['twitter']['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = conf['twitter']['ACCESS_TOKEN_SECRET']




#インスタンス作成
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

list = ['バイト　だるい',  '大学　めんどくさい',  '大学　レポート',  '金欠　きつい',  '成人式', '課題　終わらない',  '当たりますように',  '暇人DM' '誕生日プレゼント',   '20歳　なりました',  '大学　辞めようかな',  'ママ活　してみたい',  'ママ活　やりたい']
reserve = ['バイト　だるい',  '大学　めんどくさい',  '大学　レポート',  '金欠　きつい',  '成人式', '課題　終わらない',  '当たりますように',  '暇人DM' '誕生日プレゼント',   '20歳　なりました',  '大学　辞めようかな',  'ママ活　してみたい',  'ママ活　やりたい']


#ツイートの検索



#いいねの処理
def iine():
    global list
    global reserve
    if list == 0:
        list = reserve
    con = random.choice(list)

    search_results = api.search(q=con, count=20, result_type='recent')
    for result in search_results:
        tweet_id = result.id
        try:
            api.create_favorite(tweet_id)
        except Exception as e:
            print(e)

        time.sleep(10)

    list.remove(con)



#followの処理
def follow():
    global list
    global reserve
    if list == 0:
        list = reserve
    con = random.choice(list)

    search_results4 = api.search(q=con, count=20, result_type='recent')
    for result in search_results:
        user_id = result.user._json['id']
        try:
            api.create_friendship(user_id)
        except Exception as e:
            print(e)
        time.sleep(10)
    list.remove(con)




schedule.every().day.at("09:00").do(iine)
schedule.every().day.at("10:00").do(iine)
schedule.every().day.at("11:00").do(iine)
schedule.every().day.at("12:00").do(iine)
schedule.every().day.at("13:00").do(iine)
schedule.every().day.at("14:00").do(iine)
schedule.every().day.at("15:00").do(iine)
schedule.every().day.at("16:00").do(iine)
schedule.every().day.at("17:00").do(iine)
schedule.every().day.at("18:00").do(iine)
schedule.every().day.at("19:00").do(iine)
schedule.every().day.at("20:00").do(iine)
schedule.every().day.at("21:00").do(iine)
schedule.every().day.at("22:00").do(iine)
schedule.every().day.at("23:00").do(iine)
schedule.every().day.at("00:00").do(iine)
schedule.every().day.at("01:00").do(iine)
schedule.every().day.at("02:00").do(iine)
schedule.every().day.at("03:00").do(iine)



schedule.every().day.at("09:30").do(follow)
schedule.every().day.at("10:30").do(follow)
schedule.every().day.at("11:30").do(follow)
schedule.every().day.at("12:30").do(follow)
schedule.every().day.at("13:30").do(follow)
schedule.every().day.at("14:30").do(follow)
schedule.every().day.at("15:30").do(follow)
schedule.every().day.at("16:30").do(follow)
schedule.every().day.at("17:30").do(follow)
schedule.every().day.at("18:30").do(follow)
schedule.every().day.at("19:30").do(follow)
schedule.every().day.at("20:30").do(follow)
schedule.every().day.at("21:30").do(follow)
schedule.every().day.at("22:30").do(follow)
schedule.every().day.at("23:30").do(follow)
schedule.every().day.at("00:30").do(follow)
schedule.every().day.at("01:30").do(follow)
schedule.every().day.at("02:30").do(follow)

while True:
  schedule.run_pending()
  time.sleep(60)
