from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv('TOKEN')

intents : Intents = Intents.default()
intents.message_content = True

client : Client = Client(intents=intents)
async def send_message(message, user_message, username, display_name):
  if not user_message:
    return 
  if is_private := user_message[0] == '?':
    user_message = user_message[1:]
  try:
    response: str = get_response(user_message, username, display_name)
    await message.author.send(response) if is_private else await message.channel.send(response)
  except Exception as e:
    pass

@client.event
async def on_ready():
  pass

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  username = str(message.author)
  display_name = str(message.author.display_name)
  user_message = message.content
  channel = str(message.channel)

  await send_message(message, user_message, username, display_name)

def main():
  client.run(token=TOKEN)

if __name__ == "__main__":
  main()
  