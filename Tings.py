from Words import Word
from Users import User


class UserTing(User):

    def __init__(self, text, n, un):
        self.text = text
        self.n = n
        self.un = un
        super().__init__(self.text, self.n, self.un)
        self.Words = Word(User.script(self))
        self.Messages = User.script(self)

    def WordCount(self, w, l):
        self.w, self.l = w, l
        self.Words.Count(w, l)

    def MessageCount(self):
        print(len(self.Messages))
