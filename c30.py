class Myclass:
    __privateVar = 27;
    def __privatemeth(self):
        print("I'm insde class Myclass")
    def hello(self):
        print("Private variable value", Myclass.__privateVar)
foo = Myclass()
foo.hello()
foo.__privatemeth
