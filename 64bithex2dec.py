from datetime import datetime
timestamp_ms=int("000001739b8338a6",16)
print("Timestamp in milliseconds: " +str(timestamp_ms))
timestamp_s=int(timestamp_ms/1000)
print("Timestamp in seconds: " + str(timestamp_s))
print("Date:" + str(datetime.fromtimestamp(timestamp_s))) 
