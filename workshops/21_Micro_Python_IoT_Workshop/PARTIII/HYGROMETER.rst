Building your own Temperature and Humidity Control Device
---------------------

After exploring the temperature and humidity sensor and runing your first test script in the REPL, we want to combine our
different hardware components. Now we want to build our own Temperature and Humidity meassurement device. Of course, you can buy such devices for a few Euros, but where is the fun in that?

Hardware needed for this task:
----------------

* pyboard lite with accelerometer
* Jumper Wires and male Pins
* Temperature Sensor HDC1080 on break out board
* LCD160CRv1.0 Display with header
* Micro USB cable for connecting to the PC

Wire up your Sensor to one of the I2C Ports (do you remember on which Pins they are? If not, you can always have a look at the
Data sheet of the pyboard). Make sure the SDA
Take a look into the HDC1080 test program. The easiest way to show the meassured temperature and humidity on your
Display is directing the REPL to the Display. If you don't remember how that works. Please go back to Link:

**TASK 1: Using the other I2C connecton on the pyboard**

Have a look at the datasheet of the pyboard lite with accelerometer. Can you adjust the test code in the hdc1080_test.py and use the Temperature sensor with the other I2C? On which Pins is it?

**TASK 2: Temperature and Humidity on screen with the REPL**

Show the Temperature and Humidity on your Display with directing the REPL directly to it.
This looks not very nice. Now we want to show both Temperature and Humidity values on a nice setup.

**TASK 3: Temperature and Humidity on the screen**

Show the Temperature and Humidity values on the Display. Try to show them in different colours. Add the right Temperature in °C and Humidity in %. Feel free to do this in any way you like.

.. image:: /docs/pyboard/tutorial/img/image.png

**TASK 4: Data-logger for the Temperature**

Think about how you would like to log your data in an infinite loop. There are two ways of doing this. There is the internal flash of the pyboard and if you put a SD-Card in your pyboard, the data will be logged to that file.

.. code-block:: python

	rtc = pyb.RTC()

    def writeLog(rtc, temp, hum):
    """Append a line with the current timestamp to the log file"""
    datetime=rtc.datetime()
    timestamp = ("%04d-%02d-%02d %02d:%02d:%02d" % (datetime[0],
	datetime[1], datetime[2], datetime[4], datetime[5], datetime[6]))
    logline = ("%s %s %s" % (timestamp, temp, hum))

    print(logline)
    try:
        with open("/sd/logdata.txt", "a") as f:
            f.write("%s\n" % logline)
            f.close()
            pyb.sync()
    except:
	pass
    try:
	with open("/flash/logdata.txt", "a") as f:
	    f.write("%s\n" % logline)
            f.close()
            pyb.sync()

    except OSError as error:
        print("Error: can not write to SD card. %s" % error)

	def log():
	for i in range(20):
	    writeLog(rtc,hdc_temp(),hdc_hum())
