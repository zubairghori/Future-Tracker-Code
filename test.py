import os
from gps import *
from time import *
import time
import threading
import urllib2
import urllib
import socket
from twisted.internet.defer import Deferred



gpsd = None #seting the global variable
 
os.system('clear') #clear the terminal (optional)
 

def SendLocationToSevrer(Data):
   
    url = "https://zubair-app.herokuapp.com/Map"
    data = Data
    #data.update({'trackerUUID':trackerUUID, 'name':name})
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



class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
 
if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    while True:
      #It may take a second or two to get good data
      #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc
 
      os.system('clear')
 
      print
      print ' GPS reading'
      print '----------------------------------------'
      print 'latitude    ' , gpsd.fix.latitude
      print 'longitude   ' , gpsd.fix.longitude
      print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
      print 'altitude (m)' , gpsd.fix.altitude
      print 'eps         ' , gpsd.fix.eps
      print 'epx         ' , gpsd.fix.epx
      print 'epv         ' , gpsd.fix.epv
      print 'ept         ' , gpsd.fix.ept
      print 'speed (m/s) ' , gpsd.fix.speed
      print 'climb       ' , gpsd.fix.climb
      print 'track       ' , gpsd.fix.track
      print 'mode        ' , gpsd.fix.mode
      print
      print 'sats        ' , gpsd.satellites
 


      if internet_on() == True: 

          # fo = open("/home/pi/Desktop/abc.txt", "wb")
          # fo.write("i am writing:")
          # fo.close()

           location = {'latittude':gpsd.fix.latitude , 'longitude':gpsd.fix.longitude , 'speed':gpsd.fix.speed ,'trackerUUID':'vxcsfsdffsczxc', 'name':'zubair'}
           if location is not None:
               d = Deferred()
               d.addCallback(SendLocationToSevrer)
               d.callback(location)
           else:
              print('Locaiotn is nil\n')


      else:
           print("internet is not connected\n")



      time.sleep(5) #set to whatever
 
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
