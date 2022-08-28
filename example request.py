import requests
from dotenv import dotenv_values

team = "frc293"
event = "2022njski" # monty

config = dotenv_values('.env')

url = f"https://www.thebluealliance.com/api/v3/team/{team}/event/{event}/matches"

headers = {
    "X-TBA-Auth-Key": config['X-TBA-Auth-Key'],
}

response = requests.request("GET", url, headers=headers)

print(response.text)