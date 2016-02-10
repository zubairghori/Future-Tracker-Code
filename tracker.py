
from gps import *
import urllib2
import urllib
import socket

def GetCurrentLocation(timeDelay):
       report = session.next()  
       if report.keys()[0] == 'epx':
            # print("lat=%f\tlon=%f" % (report['lat'],report['lon']))
            # print(report['speed'])
             time.sleep(timeDelay)
  
             location = {'latittude':report['lat'] , 'longitude':report['lon'] , 'speed':report['speed'] }
             return location

       else:
             return None 




def SendLocationToSevrer(Data,trackerUUID, name):
   
    url = "https://zubair-app.herokuapp.com/Map"
    data = Data
    data.update({'trackerUUID':trackerUUID, 'name':name})
    encodedData = urllib.urlencode(data)
    req = urllib2.Request(url,encodedData)
    res = urllib2.urlopen(req).read()   
    print(location)
    print(res)



def internet_on():
    REMOTE_SERVER = "www.google.com"
    try:
       host = socket.gethostbyname(REMOTE_SERVER)
       s = socket.create_connection((host,80),2)
       return True
    except:
       pass
    return False



 
session = gps()
session.stream(WATCH_ENABLE|WATCH_NEWSTYLE)       
       
while True:
        
       if internet_on() == True: 

           fo = open("/home/pi/Desktop/abc.txt", "wb")
           fo.write("i am writing:")
           fo.close()

           location =  GetCurrentLocation(4)
           if location is not None:
              SendLocationToSevrer(location,"vxcsfsdffsczxc","zubair")
           else:
              print('Locaiotn is nil\n')


       else:
           print("internet is not connected\n")
