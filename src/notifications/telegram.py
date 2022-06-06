from telepot.loop import MessageLoop
import telepot
from notifications.channel import Channel 

class MyBot(Channel):
    def __init__(self, token, chatId):
        super(MyBot,self).__init__(token, chatId)
        self.token = token
        self.chatId= chatId
        self.bot = telepot.Bot(self.token)
        MessageLoop(self.bot,self.handle).run_as_thread()
        print('bot on the loop..')
        self.bot.sendMessage(self.chatId, "Hi, this channel is used to control a farm od 3D printers.")

    def getBot(self):
        return self.bot
    
    def getToken(self):
        return self.token
    
    def getChatId(self):
        return self.chatId

    def handle(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
                
        if content_type == 'text':
            command = msg['text']

            if command == '/help':
                self.bot.sendMessage(self.chatId, "Don't worry, when there is an emergency we will notify you")
            elif command == 'Open Fan' or command == 'Motor off' or command == 'Motor off and Open Fan':
                hide_keyboard = {'hide_keyboard':True}
                txt = "Control action applied: {}"
                self.bot.sendMessage(self.chatId, txt.format(command), reply_markup=hide_keyboard)
            elif command == 'Continue':
                hide_keyboard = {'hide_keyboard':True}
                self.bot.sendMessage(self.chatId, "Ok, continue printing",reply_markup=hide_keyboard) 
    
    def message(self,type,data,action):
        txt = "Hi, the {} is {}, what will you do?"
        show_keyboard = {'keyboard':[[action,'Continue']]}
        self.bot.sendMessage(self.chatId, txt.format(type,data), reply_markup=show_keyboard)
