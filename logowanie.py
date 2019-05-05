from requests_oauthlib import OAuth1Session

file = open("credentials", "r")
keys = file.read().splitlines()
file.close()

oauth_user = OAuth1Session(client_key=keys[0],
                           client_secret=keys[1],
                           resource_owner_key=keys[2],
                           resource_owner_secret=keys[3])
url_user = 'https://api.twitter.com/1.1/account/verify_credentials.json'
params = {"include_email": 'true'}
user_data = oauth_user.get(url_user, params=params)
print(user_data.json())

home_timeline = oauth_user.get('https://api.twitter.com/1.1/statuses/home_timeline.json')
print(home_timeline.json())