from requests_oauthlib import OAuth1Session

class Twitter_client:

    def __init__(self):
        self.oauth_session = ''

    def login(self):
        file = open("credentials", "r")
        keys = file.read().splitlines()
        file.close()
        self.oauth_session = OAuth1Session(client_key=keys[0],
                                           client_secret=keys[1],
                                           resource_owner_key=keys[2],
                                           resource_owner_secret=keys[3])

    def get_user_data(self):
        user_data = self.oauth_session.get('https://api.twitter.com/1.1/account/verify_credentials.json')
        print(user_data)
        print(user_data.json())
        return user_data.json()

    def get_latest_tweets(self):
        home_timeline = self.oauth_session.get('https://api.twitter.com/1.1/statuses/home_timeline.json')
        print(home_timeline)
        print(home_timeline.json())
        return home_timeline.json()

    def create_a_tweet(self, text):
        url = 'https://api.twitter.com/1.1/statuses/update.json?status='+text
        result = self.oauth_session.post(url)
        resultJson = result.json()
        print(result)
        print(resultJson)
