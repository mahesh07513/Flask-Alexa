# Simple example of sending and receiving values from Adafruit IO with the REST
# API client.
# Author: Tony DiCola

# Import Adafruit IO REST client.
from Adafruit_IO import Client

# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = '97d7273bc8ab4e38bb894e120154ce9d'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_KEY)

# Send a value to the feed 'Test'.  This will create the feed if it doesn't
# exist already.
aio.send('MaheshBABU', 42)

# Send a string value 'bar' to the feed 'Foo', again creating it if it doesn't 
# exist already.
aio.send('BABU foo', 'Mahesh')

# Now read the most recent value from the feed 'Test'.  Notice that it comes
# back as a string and should be converted to an int if performing calculations
# on it.
data = aio.receive('MaheshBABU')
print('Retrieved value from Test has attributes: {0}'.format(data))
print('Latest value from Test: {0}'.format(data.value))

# Finally read the most revent value from feed 'Foo'.
data = aio.receive('BABU foo')
print('Retrieved value from Foo has attributes: {0}'.format(data))
print('Latest value from Foo: {0}'.format(data.value))