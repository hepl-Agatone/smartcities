import machine
import utime
import time

value=0
LED = machine.Pin(16,machine.Pin.OUT)
BUTTON = machine.Pin(18,machine.Pin.IN)
LED.value(0)
t1=utime.ticks_us()
t2=utime.ticks_us()
check = utime.ticks_us()
b=0

while True:
    
    if BUTTON.value() == 1:
        if utime.ticks_diff(t2, check) >= 1000000:
            check = t2
            b=1
            if value % 2 == 1:
                for i in range(10):
                    LED.value(0)
                    utime.sleep(0.05)
                    LED.value(1)
                    utime.sleep(0.05)
                
                    
    if BUTTON.value()==0 and b == 1:

        b=0
        value = (value + 1)
        if value == 6:
            value=0
        
        
    if value == 2 or value == 3 :
        
        if time.ticks_diff(t2,t1) >= 1000000:
            
            LED.value(not LED.value())                 
            t1 = t2
            
           
            
            
    elif value == 4 or value == 5 :
        if time.ticks_diff(t2,t1) >= 200000:
            
            LED.value(not LED.value())                 
            t1 = t2
           
            
    else:
        LED.value(0)
        
    t2 = utime.ticks_us()       
    
        
    
    
    
    
