import datetime

def lastNumber(n):
    return n%10

def stToHour(string):
    st = string.split(':')
    return datetime.datetime.now().replace(hour=int(st[0]), minute=int(st[1]), second=0, microsecond=0)

def verify(l, d, ih, fh, ch):
    if ch>=ih and ch<=fh:
        if d==0 and (l==1 or l==2):
            return 1
        elif d==1 and (l==3 or l==4):
            return 1
        elif d==2 and (l==5 or l==6):
            return 1
        elif d==3 and (l==7 or l==8):
            return 1
        elif d==4 and (l==9 or l==0):
            return 1
        else:
            return 0
    else:
        return 0
    
def PicoYPlaca(number, date, time):
    last = lastNumber(number)
    
    d = date.split(',')
    day = datetime.datetime(int(d[0]), int(d[1]), int(d[2]))
    wd = day.weekday()

    timeH = stToHour(time)

    if day < datetime.datetime(2019,9,9):
        return verify(last, wd, stToHour("7:00"), stToHour("9:30"), timeH) or verify(last, wd, stToHour("16:00"), stToHour("19:30"), timeH)
    else:
        return verify(last, wd, stToHour("5:00"), stToHour("20:00"), timeH)

def main(number, date, time):
    if PicoYPlaca(number, date, time):
        print("Not allowed to circulate!")
    else:
        print("No problem :)")
        
main(2178, "2019,9,5", "12:30")        
main(3478, "2019,9,12", "12:30")
main(2170, "2019,9,6", "17:30")
main(2170, "2019,9,7", "17:30")
