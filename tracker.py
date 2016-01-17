from gps import *
session = gps()
session.stream(WATCH_ENABLE|WATCH_NEWSTYLE)

while True:

   report = session.next()
   if report.keys()[0] == 'epx':
   print("lat=%f\tlon=%f" % (report['lat'],report['lon']))
   time.sleep(0.5)
