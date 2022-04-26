#username: ProjectFarm_bot
#API: 5297525041:AAHF0Po_JZdTEJODYj3idHS50LoAIPD8qqk
# Chat_id = 2014190828

from telepot.loop import MessageLoop
import telepot
import time
import enum

class ActionSensor(enum.Enum):
    TemperatureEnclosure = 'Open Fan'
    HumidityEnclosure = 'Open Fan'

class MyBot(object):
    def __init__(self):
        super(MyBot,self).__init__()
        self.Temperature = 35.0
        self.bot = telepot.Bot('5297525041:AAHF0Po_JZdTEJODYj3idHS5OLoAIPD8qqk')
        MessageLoop(self.bot,self.handle).run_as_thread()
        print('bot on the loop..')
        #self.chat = 

    def getBot(self):
        return self.bot
    
    def handle(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        self.chat_id = chat_id  
        if content_type == 'text':
            command = msg['text']

            if command == 'Open Fan':
                hide_keyboard = {'hide_keyboard':True}
                self.bot.sendMessage(self.chat_id, "Fan is opened")
            elif command == 'Continue':
                self.bot.sendMessage(self.chat_id, "Continue")  
    
    def getChatId(self):
        return self.chat_id

    def message(self,type,data,action):
        show_keyboard = {'keyboard':[[action,'Continue']]}
        self.bot.sendMessage(self.chat_id, "Hi, the {type} is {data}, what will you do?", reply_markup=show_keyboard)


while 1:
    time.sleep(10)

