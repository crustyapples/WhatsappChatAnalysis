import re

path = 'C:\\Users\\user\\pythonTINGS\\dataTOPLAYWITH\\WhatsApp Chat - WHO IS BOOMER BANDICOOT\\_chat.txt'
chat_file = open(path, encoding="utf8")
script = chat_file.read()


class User:
    def __init__(self, text, name, username):
        self.text = text
        self.name = name
        self.username = username

    def script(self):
        pattern = r']\s{}: ([a-z0-9_. ]*)'.format(self.username)
        user_search = re.compile(pattern, re.IGNORECASE)
        user_messages = user_search.findall(self.text)
        return user_messages


#test = User(script, 'somesh', 'Somesh Sahu')
#print(test.script())
