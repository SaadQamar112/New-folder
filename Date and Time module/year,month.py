import random
import time

def grandomdate(startDate,endDate):
    print("printing random date between ",startDate,endDate)
    randomgenerator=random.random()
    dateformate='%m/%d/%Y'
    starttime=time.mktime(time.strptime(startDate,dateformate))
    endtime=time.mktime(time.strptime(endDate,dateformate))

    randomtime=starttime+randomgenerator*(endtime-starttime)
    randomdate=time.strftime(dateformate,time.localtime(randomtime))
    return randomdate
print('random date=',grandomdate('1/1/2001','1/1/2025'))
