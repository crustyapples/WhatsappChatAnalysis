from Tings import UserTing
import re

path = 'C:\\Users\\user\\pythonTINGS\\dataTOPLAYWITH\\WhatsApp Chat - WHO IS BOOMER BANDICOOT\\_chat.txt'
chat_file = open(path, encoding="utf8")
script = chat_file.read()

pattern = '].+: ([a-z0-9_. ]*)'
message_search = re.compile(pattern, re.IGNORECASE)
message_list = message_search.findall(script)

sagu = UserTing(script, 'somesh', 'Somesh Sahu')
adu = UserTing(script, 'advait', 'adu')
sagu.WordCount(5,5)

