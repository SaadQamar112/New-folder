class pakistan():
    def capital(self):
        print('the capital of pakistan is islamabad')
    def language(self):
        print('every body speaks urdu here')
    def type(self):
        print('its a developed country')

class USA():
    def capital(self):
        print('washington DC')
    def language(self):
        print('English')
    def type(self):
        print('its a developed country')

obj1=pakistan()
obj2=USA()
for country in (obj1,obj2):
    country.capital()
    country.language()
    country.type()
    