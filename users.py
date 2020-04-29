import re
from Chat import ChatStat

path = 'C:\\Users\\user\\pythonTINGS\\dataTOPLAYWITH\\WhatsApp Chat - WHO IS BOOMER BANDICOOT\\_chat.txt'
chat_file = open(path, encoding="utf8")
script = chat_file.read()


class UserChats(ChatStat):
    def __init__(self, name, username, text):
        self.name = name
        self.username = username
        self.text = text
        pattern = r'(]\s{}: [a-z0-9_. ]*)'.format(self.username)
        user_search = re.compile(pattern, re.IGNORECASE)
        user_messages = user_search.findall(self.text)
        user_script = '\n'.join(user_messages)
        super().__init__(user_script)


a = UserChats('advait', 'adu', script)
a.messageCount()
a.wordCount(5,5)
