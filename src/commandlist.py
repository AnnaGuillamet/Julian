class CommandList():
    def __init__(self):
        super(CommandList,self).__init__()
        self.command = []
    
    #def length(self):
        #return len(self.command)
    
    def pop(self):
        if len(self.command) > 0:
            return self.command.pop(0)
    
    def append(self, command):
        return self.command.append(command)

