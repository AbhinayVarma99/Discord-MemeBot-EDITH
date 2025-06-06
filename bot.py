import discord
import requests
import json

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  async def on_message(self, message):
   print(f'Message received from {message.author}: {message.content} (Channel: {message.channel.name})')
   if message.author == self.user:
    return
   if message.content.startswith('$meme'):
       print(f'Detected "$meme" from {message.author}. Sending response...')
       await message.channel.send(get_meme())

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']       

     
intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)
client.run('') # Replace with your own token.

