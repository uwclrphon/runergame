import datetime
time = 0
def start():
    a = datetime.datetime.now()
    b = datetime.timedelta(a.day,a.second,minutes=a.minute,hours=a.hour)
    c = b.total_seconds()
    time = c
def get():
    a = datetime.datetime.now()
    b = datetime.timedelta(a.day,a.second,minutes=a.minute,hours=a.hour)
    c = b.total_seconds()
    return c
def want(second):
    a = datetime.datetime.now()
    b = datetime.timedelta(a.day,a.second,minutes=a.minute,hours=a.hour)
    c = b.total_seconds()
    d = c + second
    while True:
        a = datetime.datetime.now()
        b = datetime.timedelta(a.day,a.second,minutes=a.minute,hours=a.hour)
        c = b.total_seconds()
        if c == d:
            break
def quit():
    time = 0