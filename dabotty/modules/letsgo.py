from dabotty.client import dabotty, UOPCustomEmojis

async def letsgo(message):
    if  "da" in message.content.lower():
        await message.add_reaction(UOPCustomEmojis.letsgo)


def register():
    dabotty.add_on_message_action(letsgo)