# -*- coding: utf-8 -*-
import tweepy
import json


class StreamProcessor(tweepy.StreamListener):
    def __init__(self, api, numtweets=0):
        self.api = api
        self.count = 0;
        self.limit = int(numtweets)
        super(tweepy.StreamListener, self).__init__()
        
    def on_data(self, tweets):
        
	tweet_data = json.loads(tweets)
        print tweets.rstrip()    
        self.count=self.count+1
	return False if self.count == self.limit else True
	  
        
    
auth = tweepy.OAuthHandler('AfxOYn2BjGoFCqYBPjqmaXMF6', '7OJZJOd75W0bwEu2MsbYAEgqcHh8lK3ltQivOCsBMo4gcKbVzz')
auth.set_access_token('85017375-XWIjYogyZlnpufSdkJcmiVtvaR38XIf1Y3v7XTol9', 'vl8X1PBLbY6vyVnPDS1NgUgedkHCjGXOoZab0HHzVLc6Y')
api=tweepy.API(auth)
sapi=tweepy.streaming.Stream(auth,StreamProcessor(api=api,numtweets=1500))
sapi.sample()
