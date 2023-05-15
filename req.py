import requests
import json

username = "zlyx234248"
password = "********************" # no peeking ;)

client_id = "30S6ZT3AYYPFYEMWJVMP6YWS"
client_secret = "**********************************"
auth_url = "https://www.reddit.com/api/v1/access_token"
auth_data = {"grant_type": "password", "username": username, "password": password}
auth_headers = {"User-Agent": "MyBot/0.0.1"}
auth_response = requests.post(auth_url, auth=(client_id, client_secret), data=auth_data, headers=auth_headers)
access_token = auth_response.json()["access_token"]

api_url = "https://oauth.reddit.com/user/{}/about.json".format(username)
api_headers = {"User-Agent": "MyBot/0.0.1", "Authorization": "bearer {}".format(access_token)}

api_response = requests.get(api_url, headers=api_headers)

if api_response.status_code == 200:
    api_data = json.loads(api_response.content.decode("utf-8"))
    karma = api_data["data"]["total_karma"]
    created_utc = api_data["data"]["created_utc"]
    print("Username: {}".format(username))
    print("Total Karma: {}".format(karma))
    print("Account Created: {}".format(created_utc))
else:
    print("Error: {}".format(api_response.status_code))
