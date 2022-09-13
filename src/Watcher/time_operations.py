def time_difference(a,b): # b - a
    hr = int(b[:2]) - int(a[:2])
    mn = int(b[3:5])-int(a[3:5])
    sec = int(b[6:8])-int(a[6:8])
    if mn < 0 and sec < 0:
        hr = hr - 1
        mn = 60 + mn - 1
        sec = 60 + sec
        if hr < 0:
            hr = hr + 24

    elif mn < 0:
        hr = hr - 1
        mn = 60 + mn
        if hr < 0:
            hr = hr + 24
    elif sec < 0 and mn > 0:
        sec = 60 + sec
        mn = mn - 1
        if hr < 0:
            hr = hr + 24
    elif sec < 0 and mn == 0:
        hr = hr - 1
        mn = 59
        sec = 60 + sec

    hr = str(hr).zfill(2)
    mn = str(mn).zfill(2)
    sec = str(sec).zfill(2)
    return f"{hr}:{mn}:{sec}"

def time_addition(a,b):
    hr = int(b[:2]) + int(a[:2])
    mn = int(b[3:5]) + int(a[3:5])
    sec = int(b[6:8]) + int(a[6:8])
    if mn >= 60 and sec >= 60:
        hr = hr + 1
        mn = mn - 60 + 1
        sec = sec - 60
    elif mn >= 60:
        hr = hr + 1
        mn = mn - 60
    elif sec >= 60:
        mn = mn + 1
        sec = sec - 60

    hr = str(hr).zfill(2)
    mn = str(mn).zfill(2)
    sec = str(sec).zfill(2)
    return f"{hr}:{mn}:{sec}"

def format_time(t):
    #if int(t[0:2]) == 0:
    #    result = t[3:5] + 'm ' + t[6::] + 's'
    #    if int(t[3:5]) == 0:
    #        result = t[6::] + 's'
    #else:
    #    result =  t[0:2] + 'h ' + t[3:5] + 'm ' + t[6::] + 's'
    return t[:2] + 'h ' + t[3:5] + 'm ' + t[6::] + 's'

def convert_into_sec(t):
    return int(t[:2]) * 3600 + int(t[3:5])*60 + int(t[6::])


