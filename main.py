from Twitter import Twitter_client

twitter = Twitter_client()

twitter.login()
print(twitter.get_user_data())
print(twitter.get_latest_tweets())

