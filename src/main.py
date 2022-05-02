import yaml
import json

class Main(object):
    def __init__(self):
        super(Main, self).__init__
        self._get_config()
    
    def _get_config(self):
        with open("julian.yaml") as f:
            self.cfg = yaml.load(f, Loader=yaml.FullLoader)
        self.api = self.cfg["telegram"]["token"]
        self.chatid = self.cfg["telegram"]["chat_id"]