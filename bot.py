from twitchio.ext import commands
from pynput.keyboard import Key, Controller
import time

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token='oauth:yourtoken', client_id='twitchprofile', nick='twitchprofile', prefix='!',
                         initial_channels=['yourchannel'])
        self.keyboard = Controller()

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.content)
        if message.content.lower() == 'start':
            self.keyboard.press(Key.enter)
            time.sleep(.15)
            self.keyboard.release(Key.enter)
        elif message.content.lower() == 'arriba':
            self.keyboard.press(Key.up)
            time.sleep(.15)
            self.keyboard.release(Key.up)
        elif message.content.lower() == 'abajo':
            self.keyboard.press(Key.down)
            time.sleep(.15)
            self.keyboard.release(Key.down)
        elif message.content.lower() == 'izquierda':
            self.keyboard.press(Key.left)
            time.sleep(.15)
            self.keyboard.release(Key.left)
        elif message.content.lower() == 'derecha':
            self.keyboard.press(Key.right)
            time.sleep(.15)
            self.keyboard.release(Key.right)
        elif message.content.lower() == 'a':
            self.keyboard.press(Key.space)
            time.sleep(.15)
            self.keyboard.release(Key.space)
        elif message.content.lower() == 'b':
            self.keyboard.press(Key.backspace)
            time.sleep(.15)
            self.keyboard.release(Key.backspace)
        await self.handle_commands(message)

    # Commands use a different decorator
    @commands.command(name='test')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')

bot = Bot()
bot.run()