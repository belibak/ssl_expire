#!/usr/bin/env python
import datetime, time, sys
import subprocess

def get_exp_date_src():
    file = sys.argv[1]
    cmd = ['openssl', 'x509', '-in', file, '-noout', '-enddate']
    date_src = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out = date_src.communicate()
    date = out[0].split('=')
    date = date[1].split(" ")
    for ind, i in enumerate(date):
        #print(ind)
        if i == '':
            date.pop(ind)
    #print(date)
    return date

def set_exp_seconds(dt = get_exp_date_src()):
    monthDict = {'Jan' : 1,'Feb':1,'Mar':3,'Apr' : 4, 'May' : 5,'Jun' :6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,
                 'Nov':11,'Dec':12}
    day = int(dt[1])
    month = int(monthDict[dt[0]])
    year = int(dt[3])
    t = datetime.datetime(year, month, day, 0, 0)
    t = time.mktime(t.timetuple())
    return t

def from_now():
    exp = set_exp_seconds()
    now = time.time()
    diff = exp - now
    diff_days = int(diff/60/60/24)
    print(diff_days)
    return diff_days

if __name__ == '__main__':
    from_now()