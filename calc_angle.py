import math

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
v_0 = 1.74  # Initial velocity (m/s)

# Function to calculate the launch angle that achieves a given horizontal distance
def calculate_launch_angle(R, h):
    """
    Calculate the launch angle to hit the target at distance R (meters) from height h (meters).
    """
    angle = 0  # Initial angle guess
    step = 0.01  # Step size for angle increment in degrees
    max_iterations = 180 / step  # Limit the angle search to 0-180 degrees
    
    for _ in range(int(max_iterations)):
        # Time of flight based on horizontal motion equation
        t = R / (v_0 * math.cos(math.radians(angle)))
        
        # Vertical motion equation to calculate the distance traveled in the vertical direction
        vertical_position = h + (v_0 * math.sin(math.radians(angle)) * t) - (0.5 * g * t**2)
        
        # Check if the vertical position is close to zero (target hit)
        if abs(vertical_position) < 0.01:  # Tolerance for solution
            return angle
        
        angle += step  # Increment angle
    
    # If no solution found, return None
    return None

# Example usage
distance = 5.0  # Distance measured from ultrasonic sensor (in meters)
initial_height = 1.0  # Initial height of the projectile (in meters)

# Calculate the launch angle
launch_angle = calculate_launch_angle(distance, initial_height)

if launch_angle is not None:
    print(f"The launch angle required to hit the target at {distance:.2f} meters is: {launch_angle:.2f} degrees")
else:
    print("No valid launch angle found to hit the target at the given range.")
