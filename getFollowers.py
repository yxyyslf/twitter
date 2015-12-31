__author__ = 'Yi'
from tweepy import OAuthHandler
from pymongo import MongoClient
import tweepy
import time


def AddFollower(followers):
        userFollowerList = []
        for follower in followers:
             try:
                for i in range(len(follower)):
                    userFollowerList.append(follower[i])
                print len(userFollowerList)
             except Exception as exc:
                print exc
                time.sleep(60 * 15)
                continue
        return userFollowerList

client = MongoClient()
db = client.twiiter
userIdCol = db.userid
userFollowerIdCol = db.userfollowerid
userIdCursor = userIdCol.find({'_id':{'$gt':0,'$lt':10000}},no_cursor_timeout=True)
userFollowerCursor = userFollowerIdCol.find()
userIdList = []
for document in userFollowerCursor:
    userIdList.append(document['_id'])
#Variables that contains the user credentials to access Twitter API
access_token = "3225871614-tatV4P0d2C32hPJVATASDoxEchqiJsGuwMKF8Yw"
access_token_secret = "BVi3OAG9zgUb04Ryn7gohAJqIP4MkyKPBMNGlmki7Eb6R"
consumer_key = "CqacbnGIuqdD5EctUOC0Itlea"
consumer_secret = "l1m5Q08ooJ19aG2zZVS0oEQR6UDBZPuEvJK1Cgj7u4sWSxBPVq"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

for document in userIdCursor:
    try:
        print(document)
        if document['_id'] in userIdList:
            print('Already in the database!')
            continue
        userScreenName = document['username']
        userTime = document['time']
        userId = document['_id']
        userFollowerNum = document['followerNum']
        followers = tweepy.Cursor(api.followers_ids, screen_name=userScreenName).pages()
        userFollower = AddFollower(followers)
        print(str(userFollowerNum)+' : '+str(len(userFollower)))
        twitterFollower = {
                            '_id':userId,
                            'username':userScreenName,
                            'time':userTime,
                            'follower':userFollower,
                            'followerNum':userFollowerNum
                          }
        userFollowerIdCol.insert(twitterFollower)
    except Exception as e:
        print e
