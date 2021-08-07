# import the module
import tweepy

# assign the values accordingly
def tweetss(wo):
    consumer_key = #api key
    consumer_secret = #api secret
    access_token = #access token
    access_token_secret = #access token secret

    # calling API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    li = []

    # # authorization of consumer key and consumer secret
    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #
    # # set access to user's access key and access secret
    # auth.set_access_token(access_token, access_token_secret)
    #
    # # calling the api
    # api = tweepy.API(auth)

    # WOEID of London
    # woeid = 44418
    woeid = wo

    # fetching the trends
    trends = api.trends_place(id = woeid)

    # printing the information
    #print("The top trends for the location are :")

    for value in trends:
        for trend in value['trends']:
                 li.append(trend['name'])

    return li[:10]

