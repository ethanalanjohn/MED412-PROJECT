#calculate launch angle
import math
from scipy.optimize import fsolve

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
v_0 = 1.74  # Initial velocity (m/s)

# Function to calculate the launch angle that achieves a given horizontal distance
def equation(theta, R, h):
    # Time of flight based on horizontal motion equation
    t = R / (v_0 * math.cos(math.radians(theta)))
    
    # Vertical motion equation to calculate the distance traveled in the vertical direction
    vertical_position = h + (v_0 * math.sin(math.radians(theta)) * t) - (0.5 * g * t**2)
    
    return vertical_position  # Should be 0 when the projectile reaches the ground

# Function to find the launch angle that gives the target range
def find_launch_angle(R, h):
    # Define the equation to solve for theta
    def angle_equation(theta):
        return equation(theta, R, h)
    
    # Initial guess for angle in degrees
    initial_guess = 45  # Start from 45 degrees as a common starting point
    # Solve for the launch angle using fsolve
    angle = fsolve(angle_equation, initial_guess)
    return angle[0]

# Example usage
R = 5.0  # Horizontal distance (in meters)
h = 1.0  # Initial height (in meters)

# Calculate the launch angle
angle = find_launch_angle(R, h)
print(f"The launch angle required to achieve a distance of {R} meters from height {h} meters is: {angle:.2f} degrees")
