import discord

class MyClient(discord.Client):
	async def on_ready(self):
		self.groovy_channel = self.get_channel(815014756359340033)
		print('Logged on as {0}!'.format(self.user))

	async def on_message(self, message):
		print('Message from {0.author}: {0.content}'.format(message))

		if len(message.content) > 1 and message.content[0] == '-' and message.content[1] != '-':
			# Move message to designated channel
			user = message.author.display_name
			new_content = message.content[1:]

			await message.delete()
			await self.groovy_channel.send(f'\"{new_content}\" requested by {user}')

token = open('token.txt', 'r').read()
client = MyClient()
client.run(token)