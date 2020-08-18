import os
from datetime import datetime

def tstamp(ts):
  print(ts)
#  timestamp_ms=int("000001739b8338a6",16)
  timestamp_ms=int(ts)
  print("Timestamp in milliseconds: " +str(timestamp_ms))
  timestamp_s=int(timestamp_ms/1000)
  print("Timestamp in seconds: " + str(timestamp_s))
  print("Date:" + str(datetime.fromtimestamp(timestamp_s)))
  dstamp=datetime.fromtimestamp(timestamp_s) 
#  dstamp=0
  return dstamp
#  return

def extractData(frame):
  print("frame in function=", frame)
  return
with open("43596.kss","rb") as f:
  s=f.read()
  frames=s.split(b'\xc0\x09')
  i=0
  for fr in frames:
#   print("Frame ",i,": ",fr)
   i=i+1
   print("Timestamp: ",fr[0:8])
   if (len(fr[0:8]) == 8):
     stringtosend=str(int.from_bytes(fr[0:8], byteorder='big'))
     print("stringtosend=",stringtosend)
     print("Datestamp: ",tstamp(stringtosend))
     dataStruct=extractData(fr[10:-1])
#  bytes=list(f.read())
#  for word in bytes:
#   print(word)
#  while byte:
#    if (byte==b'\xc0'):
#      print("C0 detected")
#      byte=f.read(1)
#      if (byte==b'\xc0'):
#        print("Start of frame detected")
#    byte=f.read(1)
#print(bytes)
#print(tstamp(stringtosend))
print(int.from_bytes(b'\x00\x00\x01\x73\x9b\x83\x38\xa6',byteorder='big'))

