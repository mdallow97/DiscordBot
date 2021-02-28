import discord

class MyClient(discord.Client):
	def __init__(self, channel_id):
		super(MyClient, self).__init__()
		self.groovy_channel_id = channel_id
		self.keywords = ['play', 'p', 'queue', 'q', 'skip', 'stop', 'pause', 'shuffle', 'clear', 'resume']

	async def on_ready(self):
		self.groovy_channel = self.get_channel(self.groovy_channel_id)
		print('Logged on as {0}!'.format(self.user))

	async def on_message(self, message):
		
		if len(message.content) > 0:
			print('Message from {0.author}: {0.content}'.format(message))

		if message.channel == self.groovy_channel:
			return

		if message.author.name == 'Groovy':
			await message.delete()
			for embedded in message.embeds:
				await self.groovy_channel.send(embed=embedded)

		elif len(message.content) > 1 and message.content[0] == '-':
			# Move message to designated channel
			command = ''
			i = 1
			while i < len(message.content) and message.content[i] != ' ':
				command += message.content[i]
				i+=1
			
			if command in self.keywords:
				await message.delete()
				await self.groovy_channel.send(f'\"{message.content}\" requested by {message.author.display_name}')

params = open('token.txt', 'r').read().split('\n')
if len(params) != 2:
	print("tokens.txt must contain two parameters separated by a new line")

token, channel_id = params[0], int(params[1])
client = MyClient(channel_id)
client.run(token)