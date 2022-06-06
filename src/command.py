from threading import Thread

class CommandList(object):
    def __init__(self,stackData):
        self.stack = stackData
        self.command = []
      
    def register(self, command):
        return self.command.append(command)
    
    def start(self):
        th = Thread(target = self.bucle)
        th.start()
    
    def bucle(self):
        while True:
            x = self.stack.get()
            for command in self.command:
                command(x)
