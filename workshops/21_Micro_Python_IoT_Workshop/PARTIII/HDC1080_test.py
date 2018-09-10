"""Tests for the hdc1080 module"""

#check, if the sensor is connected to a ESP8266 or a pyboard
import machine
try:
    import esp
    esp.osdebug(None)
    i2c = machine.I2C(sda=machine.Pin(4), scl=machine.Pin(5))
except:
    pass
try:
    import pyb
    i2c = machine.I2C(sda=machine.Pin('X10'), scl=machine.Pin('X9'), freq=400000)
except:
    pass
import utime

i2c.scan()

dt = 20
b1 = bytearray(1)
b2 = bytearray(2)

def hdc1080_read(a=0):
    b1[0] = a
    i2c.writeto(64, b1)
    pyb.delay(dt)
    i2c.readfrom_into(64, b2)
    #return '%02x%02x' % (b[0], b[1])
    return (b2[0] << 8) | b2[1]

#calculating temperature
def hdc_temp():
    t = hdc1080_read(0)
    return (t / 0x10000)*165-40

#calculating humidity    
def hdc_hum():
    t = hdc1080_read(1)
    return (t / 0x10000)*100

def read_sensors():
    print("Temperature (degree celsius): %.2f" % (hdc_temp()))
    print("Relative humidity (percent):  %.2f" % (hdc_hum()))
   #print("Both sensors read at once:    %.2f  %.2f" % hdc.temp_hum())
   #print("Battery low: %s" % (hdc.battery_low()))

def main():
    print("Reading sensors 10 times using idle sleeping...")
    for i in range(10):
        read_sensors()
        utime.sleep_ms(100)

#main()
