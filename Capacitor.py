import matplotlib.pyplot as plt
import numpy as np

# Helper function for capacitor
def place_line_of_charge(charge, length, y0, q_list):
    """
    Place a horizontal line of discrete charges to simulate a charged plate.
    
    Parameters:
    charge: magnitude of each discrete charge element
    length: total length of the line (centered at x=0)
    y0: y-coordinate of the line
    q_list: list to append charges to
    """
    number = 100  # Number of discrete charges to approximate the continuous line
    start_x = -length/2
    end_x = length/2
    spacing = length / number
    
    i = 0
    while i < number:
        # Keep adding charges in a line
        chargeMagnitude = charge
        chargeX = start_x + i * spacing + spacing/2  # Center each charge element
        chargeY = y0
        
        q_list.append((chargeMagnitude, chargeX, chargeY))
        i += 1

def build_parallel_plate_capacitor(plate_length, plate_separation, surface_charge_density, q_list):
    """
    Build a parallel plate capacitor with two horizontal plates.
    
    Parameters:
    plate_length: length of each plate (centered at x=0)
    plate_separation: distance between the plates (centered at y=0)
    surface_charge_density: charge per unit length (σ) for the plates
    q_list: list to append charges to
    """
    # Convert surface charge density to discrete charge magnitude
    # Each discrete charge represents a small segment of length dx
    number_of_elements = 100
    segment_length = plate_length / number_of_elements
    discrete_charge = surface_charge_density * segment_length
    
    # Top plate (positive charge)
    place_line_of_charge(discrete_charge, plate_length, plate_separation/2, q_list)
    
    # Bottom plate (negative charge)
    place_line_of_charge(-discrete_charge, plate_length, -plate_separation/2, q_list)
