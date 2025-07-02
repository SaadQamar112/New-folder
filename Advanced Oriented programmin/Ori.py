class iosstring:
    def __init__(self):
        self.str1=''
    def getting_string(self):
        self.str1=input('enter a string')
    def upper_case(self):
        print('',self.str1.upper())
str1=iosstring()
str1.getting_string()
str1.upper_case()
