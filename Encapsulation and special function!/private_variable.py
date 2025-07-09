class myclass:
    __private='hi';
    def __private_method(self):
        print('i am inside this class!')

    def hello(self):
        print('private varible',myclass.__private)
foo=myclass()
foo.hello()
foo._myclass__private_method()