import serial
import time 
import string
import pynmea2
from twilio.rest import Client

def get_location():
	while True:
	    ser=serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)
	    dataout =pynmea2.NMEAStreamReader() 
	    newdata=ser.readline()
	    if '$GPRMC' in str(newdata):
	        try:
	            decoded_data = newdata.decode('utf-8')
	        except UnicodeDecodeError as e:
	            print(f"Error decoding {newdata}: {e}")
	            
	        else:
	            if '$GPRMC' in decoded_data:
	                newmsg = pynmea2.parse(decoded_data)
	                lat=newmsg.latitude 
	                lng=newmsg.longitude 
	                gps = "Latitude=" + str(lat) + "and Longitude=" +str(lng)
	                return(gps)
	        

def sms1():
    
    

    account_sid = "ACb562080d6bfe045131dd922fdbe123a9"
    auth_token = "34d4b11bafeee0e2611688427532bd9f"

    body =  "Unknown face detected at location at latitude is 23.079171666666667 and longitude is 76.85027033333333"

    client = Client(account_sid, auth_token)
    message = client.api.account.messages.create(to = "+917306512974", from_= "+16203496079", body = body )

#get_location()
sms1()





