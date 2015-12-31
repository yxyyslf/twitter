__author__ = 'Yi'
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

access_token = "2335343755-5rFPfqksbxldri41ikNoaVwClLkTNd4giI0Wuvp"
access_token_secret = "O2s8wrAN3AABFH158ShNOUOaRPlsbPpjoaUZLmsPcqtF8"
consumer_key = "VjqHZrPRjjizOgwJUdfyDe9Q3"
consumer_secret = "Y4JAPy4vtieYGxngoqwHTglFVkMgyCJx2l8iAtMpGbVfmwoSv3"

class StdOutListener(StreamListener):

    def on_data(self, data):
        saveFile = open('raw_tweets.json', 'a')
        saveFile.write(data)
        saveFile.write('\n')
        saveFile.close()
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    try:
        stream.filter(track=['North Korean Girl Band'])
    except Exception as e:
        print e
        time.sleep(300)