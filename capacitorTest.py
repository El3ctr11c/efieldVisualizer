import matplotlib.pyplot as plt
import numpy as np

# Import the Capcitor.py functions
import Capacitor as Cap

# Domain for plot: X: [min, max], Y: [min, max]
# Also Note that X Domain and Y are the same => Square Plot
MIN = -1000
MAX = 1000

# Density of points in the grid
N = 500 #HIGHER NUMBER == HIGHER RESOLUTION

def capacitorTest():
    ## ----------- PLOT INITIALIZATION ----------- ##
    # Set evenly spaced points within the interval [MIN, MAX]
    a, b = np.linspace(MIN, MAX, N), np.linspace(MIN, MAX, N) 

    # A meshgrid in the xy plane. xa, ya contains the coordinates of the space
    xa, ya = np.meshgrid(a, b)

    #2D Arrays to store Ex and Ey components at every point in space
    Ex, Ey = np.zeros_like(xa), np.zeros_like(xa) # We just initialize them to have zeros

    # Initialize array of charges with value, and position (|Q|, x, y)
    charges = []

    plate_length = float(input("Enter plate length (centered at x=0): "))
    plate_separation = float(input("Enter plate separation (distance between plates): "))
    plate_charge = float(input("Enter the plate equilibrium charge (charge will be same on both sides just opposite signs):  "))


    Cap.build_parallel_plate_capacitor(plate_charge, plate_length, plate_separation, charges)
     
    # Color Charge locations 
    for q in charges:  # mark charge locations
        plt.text(q[1], q[2], 'o', color = 'r' if q[0] < 0 else 'b', fontsize=15, va='center', ha='center')

    # Calculate Ex and Ey at each point in the grid due to all charges
    for i in range(N): # Loop through the X - Axis
        for j in range(N): # Loop throught the Y - Axis
            # Specific Point in space
            x, y = xa[i,j], ya[i,j]

            # Calculates the E field at (x,y) due to ALL CHARGES BRO HOLY MOLY
            for k in range(len(charges)):
                # Add up Ex and Ey components at that point from a specific charge in list
                Ex[i,j] += charges[k][0]*(x-charges[k][1])/ ((x-charges[k][1])**2+(y-charges[k][2])**2)**(1.5)
                Ey[i,j] += charges[k][0]*(y-charges[k][2])/ ((x-charges[k][1])**2+(y-charges[k][2])**2)**(1.5)

                #Remember cuz Ex and Ey are lists which contain
                #the E-field at every point in the grid right???? :OOO
    # Show the plots for visualization 
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title(f"Electric Field of {len(charges)} Charges combined")
    plt.streamplot(xa, ya, Ex, Ey, color='black', density=1.5) #plot the field lines using streamplot
    plt.show() # show the plot

capacitorTest()