# light_sensor.py
from machine import ADC, Pin

# Set up the light sensor (assuming it's an analog sensor connected to GPIO pin)
LIGHT_SENSOR_PIN = 28  # Adjust as necessary
light_sensor = ADC(Pin(LIGHT_SENSOR_PIN))

def read_light_intensity():
    """ Read the current light intensity from the sensor. """
    intensity = light_sensor.read_u16()  # or light_sensor.read() based on your setup
    return intensity
