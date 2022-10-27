import os 
import threading
import requests, random
from discord_webhook import DiscordWebhook, DiscordEmbed
import time

time.sleep(1)

def Finder():
  id = random.randint(1, 115000000)
  r = requests.get(f"https://roblox.com/groups/{id}")
  if "owned" not in r.text:
    re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
    if 'isLocked' not in re.text and 'owner' in re.text:
            if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
              print(f"Group Found: {id}")
              json = re.json
              members = json['memberCount']
              desc = json['description']
              embed = DiscordEmbed(title='New Group Found! Group', color=242424)
              embed.add_embed_field(name='ID', value=f'{id}')
              embed.add_embed_field(name='Description', value=f'"{desc}"')
              embed.add_embed_field(name='Members', value=f'{members}')
              embed.add_embed_field(name='Link', value=f'https://www.roblox.com/groups/{id}')
              webhook.add_embed(embed)
              response = webhook.execute()
            else:
              print(f"No entry: {id}")
    else:
      print(f"Locked: {id}")
  else:
    print(f"Owned: {id}")
webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/985655474156363796/K5WGxwRuteNHax94mQ6PXsN09u-zxWJBSA7SYyvTPRNhHqlcXAsZYOohdAsXktnNimDL")
threads = (int(input("How many threads: ")))
while True:
    if threading.active_count() <= threads:
        threading.Thread(target=Finder).start()
