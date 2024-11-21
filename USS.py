from machine import Pin
import utime

# Initialize trigger and echo pins
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def get_distance():
    """
    Measures the distance to an object using an ultrasonic sensor.

    Returns:
        float: Distance to the object in cm, or None if no echo is detected.
    """
    try:
        # Ensure trigger pin is low before starting
        trigger.low()
        utime.sleep_us(2)  # Short delay

        # Send the trigger pulse (5 microseconds)
        trigger.high()
        utime.sleep_us(5)  # Trigger pulse duration
        trigger.low()

        # Wait for echo to go HIGH (signal sent)
        timeout_start = utime.ticks_us()
        while echo.value() == 0:
            if utime.ticks_diff(utime.ticks_us(), timeout_start) > 30000:  # Timeout after 30ms
                print("Timeout: No echo received.")
                return None
            signaloff = utime.ticks_us()

        # Wait for echo to go LOW (signal returned)
        timeout_start = utime.ticks_us()
        while echo.value() == 1:
            if utime.ticks_diff(utime.ticks_us(), timeout_start) > 30000:  # Timeout after 30ms
                print("Timeout: Echo signal stuck HIGH.")
                return None
            signalon = utime.ticks_us()

        # Calculate the time the signal took to travel
        timepassed = signalon - signaloff

        # Calculate the distance (in cm)
        distance = (timepassed * 0.0343) / 2  # Speed of sound is 0.0343 cm per microsecond
        return distance

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example of how to call the function
#while True:
#    print("Measuring distance...")
#    distance = get_distance()
 #   if distance is not None:
  #      print(f"Distance to the object: {distance:.2f} cm")
   # else:
    #    print("Failed to measure distance.")
    ##time.sleep(1)  # Wait before the next measurement

