class Duck:
    def talk(self):
        print("quack quack")

class Human:
    def talk(self):
        print("hello")

def callTalk(self):
    self.talk()

d=Duck()
h=Human()
callTalk(d)
callTalk(h)
