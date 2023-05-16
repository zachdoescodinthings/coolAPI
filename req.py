import requests
import json


# Set up OAuth2 authentication with LinkedIn
client_id = '30S6ZT3AYYPFYEMWJVMP6YWS'
client_secret = '***************************************'
redirect_uri = 'https://bit.ly/43eYTkf'
auth_url = 'https://www.linkedin.com/oauth/v2/authorization'
access_token_url = 'https://www.linkedin.com/oauth/v2/accessToken'
scope = 'r_liteprofile'  # Request basic profile information

# Step 1: Redirect the user to the LinkedIn OAuth2 authentication page
params = {
    'response_type': 'code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'scope': scope,
}
r = requests.get(auth_url, params=params)
print(f'Open this URL in your browser: {r.url}')
auth_code = input('Enter the authorization code from the redirected URL: ')

# Step 2: Exchange the authorization code for an access token
data = {
    'grant_type': 'authorization_code',
    'code': auth_code,
    'redirect_uri': redirect_uri,
    'client_id': client_id,
    'client_secret': client_secret,
}
r = requests.post(access_token_url, data=data)
access_token = r.json()['access_token']

# Step 3: Use the access token to retrieve some basic profile information
headers = {
    'Authorization': f'Bearer {access_token}',
    'Connection': 'Keep-Alive',
}
r = requests.get('https://api.linkedin.com/v2/me?projection=(id,firstName,lastName)', headers=headers)
if r.ok:
    data = r.json()
    print(f'First name: {data["firstName"]["localized"]["en_US"]}')
    print(f'Last name: {data["lastName"]["localized"]["en_US"]}')
else:
    print(f'Request failed with status code {r.status_code}: {r.text}')

   
import tweepy

# Set up authentication with Twitter API
consumer_key = '**************************************'
consumer_secret = '**************************************'
access_token = '**************************************'
access_token_secret = '**************************************'
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Get user's profile information
username = 'allziswell_'
user = api.get_user(username)

# Print user information
print(f'Name: {user.name}')
print(f'Screen name: {user.screen_name}')
print(f'Followers count: {user.followers_count}')
print(f'Friends count: {user.friends_count}')

    

