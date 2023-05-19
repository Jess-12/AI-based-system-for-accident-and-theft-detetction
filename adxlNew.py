import spidev
import time
#from gpsnew import sms1
from twilio.rest import Client



spi=spidev.SpiDev()
spi.open(0,0)
spi.mode=3
spi.max_speed_hz=360000

def sms():
    
    

    account_sid = "ACb562080d6bfe045131dd922fdbe123a9"
    auth_token = "34d4b11bafeee0e2611688427532bd9f"

    body =  "accident detected at location at latitude is 23.079171666666667 and longitude is 76.85027033333333"

    client = Client(account_sid, auth_token)
    message = client.api.account.messages.create(to = "+917306512974", from_= "+16203496079", body = body )



def readadc(adcnum):
   r=spi.xfer2([1,8+adcnum<<4,0])
   adcout=((r[1]  & 3) <<8) + r[2]
   return adcout


def out():
       x=readadc(0)
       y=readadc(1)
       z=readadc(2)
       print("x : {} y: {} z:{}".format(x,y,z))
       
       return x,y

past_val_x = []
past_val_y = []
while True:
    x, y = out()
    past_val_x.append(x)
    past_val_y.append(y)
    
    if(len(past_val_x)<2):
        continue

    if(abs(past_val_x[-1]-past_val_x[0])>100 or x<200 or x>400):
        print("Accident Detected")
        sms()
        
        break;
    elif(abs(past_val_y[-1]-past_val_y[0])>100 or y<200 or y>400):
        print("Accident Detected")
        sms()
        
        
        break;
    
    past_val_x.pop(0)
    past_val_y.pop(0)
    