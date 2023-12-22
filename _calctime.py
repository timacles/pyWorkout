from datetime import datetime 


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::

secs = 2190

m = int(secs / 10 / 60)

s =  secs / 10 - (m * 60)

ms = str(secs)[3:]


a = [m, s, ms]

print(a)