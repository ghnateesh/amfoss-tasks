def timeConversion():
    s=input()
    if s[-2]=='P':
        x=s.find(':')
        y=int(s[0:2])
        y=y+12
        print(str(y)+s[2:])
    else:
        print(s)
timeConversion()
