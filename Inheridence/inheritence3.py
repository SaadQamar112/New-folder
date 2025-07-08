class bird:
    def __init__(self):
        print('bird')
    def whoisthis(self):
        print('bird')
    def swim(self):
        print('yes,it can swim')

class penguin(bird):
    def __init__(self):
        super().__init__()
        print('penguin is Ready')
    def whoisthis(self):
        print('penguin')
    def run(self):
        print('yes')

obj=penguin()
obj.whoisthis()
obj.swim()
obj.run()
