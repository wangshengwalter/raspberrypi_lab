import Adafruit_DHT
  
# Set sensor type : Options are DHT11,DHT22 or AM2302
#use Adafruit library, install the library first,
#then if u are 4B use may need to change the platform_detect.py
#then install this library.
#may meet the problem with set up, just google it.
sensor=Adafruit_DHT.DHT11
  
# Set GPIO sensor is connected to
#pay attentaion here it is a gpio number not physic pin number
gpio=17

  
# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
      
    # Reading the DHT11 is very sensitive to timings and occasionally
    # the Pi might fail to get a valid reading. So check if readings are valid.
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
