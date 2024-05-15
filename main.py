from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, Thread

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True
intents.members = True
client: Client = Client(intents=intents)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

@client.event
async def on_thread_create(thread: Thread) -> None:

    observed_forums: list = ['testforum']

    if thread.parent.name not in observed_forums:
        return

    if duplicate_thread := next((x for x in thread.parent.threads if x.owner_id==thread.owner_id), None):
        reply: str = f"Hey {thread.owner.mention}! It looks like you already have a help thread opened: {duplicate_thread.mention}\nIf that concers the same install/machine please close this thread and update the other. As per the forum guidelines only one thread per install is allowed."
        await thread.send(reply)


def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()