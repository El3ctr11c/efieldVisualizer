import matplotlib.pyplot as plt
import numpy as np

# These are the intervals for the axii with both [min, max]
MIN = -100
MAX = 100

# Number of points in x-coordinate and y-coordinate each 
N = 1000 #HIGHER NUMBER == HIGHER RESOLUTION

def main():
    ## ----------- PLOT INITIALIZATION ----------- ##
    # Set evenly spaced points within the interval [MIN, MAX]
    a, b = np.linspace(MIN, MAX, N), np.linspace(MIN, MAX, N) 

    # A meshgrid in the xy plane. xa, ya contains the coordinates of the space
    xa, ya = np.meshgrid(a, b)
    #2D Arrays to store Ex and Ey components
    Ex, Ey = np.zeros_like(xa), np.zeros_like(xa)

    # Initialize array of charges with value, and position (|Q|, x, y)
    Q = []

    # Ask User to place charges
    keepAsking = True
    while (keepAsking):
        chargeMagnitude = float(input("Enter the value of the charge: "))
        chargeX = float(input("Enter the x - position of the charge: "))
        chargeY = float(input("Enter the y - position of the charge: "))

        # Add charge to list of charges
        Q.append((chargeMagnitude, chargeX, chargeY))

        # Ask user if they want to continue placing charges
        choice = input("Do you want to continue placing charges? (Y/N)")
        if (choice == 'N'):
            keepAsking = False
     
    # Color Charge locations 
    for q in Q:  # mark charge locations
        plt.text(q[1], q[2], 'o', color = 'r' if q[0] < 0 else 'b', fontsize=15, va='center', ha='center')

    # Calculate Ex and Ey at each point in the grid due to all charges
    for i in range(N):
        for j in range(N):
            # Specific Point in space
            x, y = xa[i,j], ya[i,j]
            for k in range(len(Q)): # sum over the charges
                Ex[i,j] += Q[k][0]*(x-Q[k][1])/ ((x-Q[k][1])**2+(y-Q[k][2])**2)**(1.5)
                Ey[i,j] += Q[k][0]*(y-Q[k][2])/ ((x-Q[k][1])**2+(y-Q[k][2])**2)**(1.5)

    plt.streamplot(xa, ya, Ex, Ey, color='black', density=1.5) #plot the field lines using streamplot
    plt.show() # show the plot

if __name__ == "__main__":
    main()