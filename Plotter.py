# TODO: Encapsulate all of the functionality for Plotting (E field calculations)
import matplotlib.pyplot as plt
import numpy as np

# this value is to avoid division by zero
epsilon = 1e-12 
k = 1 # We use 1 for simplicity to visualize the e fields

class EFieldVisualizer:
    POSITIVE_COLOR = 'BLUE'
    NEGATIVE_COLOR = 'RED' 
    
    DARKMODE = True  

    def __init__(self, MIN=-10, MAX=10, N=100):
        self.title = ""
        self.MIN = MIN
        self.MAX = MAX
        self.N = N
        # Set evenly spaced points within the interval [MIN, MAX]
        x, y = np.linspace(MIN, MAX, N), np.linspace(MIN, MAX, N) 
        # A meshgrid in the xy plane. xa, ya contains the coordinates of the space
        self.X, self.Y = np.meshgrid(x, y) # Returns two arrays

        #2D Arrays to store Ex and Ey components of every point in space
        self.Ex = np.zeros_like(self.X) # Initally be zero
        self.Ey = np.zeros_like(self.X) # Initally be zero

        # Initialize array of charges with value, and position (|Q|, x, y)
        self.charges = []

    def place_charge(self, q, x, y):
        # Place charge in the array of charges
        self.charges.append((q, x, y))

    # We calculate the e field at every point in our grid due to other charges
    def calculate_electric_field(self):
        # Iterate over the rows of the grid
        for i in range(self.X.shape[0]):
            # Iterate over the xis
            for j in range(self.Y.shape[0]):
                # Look at every charges placed
                x, y = self.X[i,j], self.Y[i,j]
                for charge, chargeX, chargeY in self.charges:
                    # Add specific electric field contribution by that charge
                    # Note that epsilon is added in the denominator to avoid division by zero error!
                    self.Ex[i,j] += k*charge*(x-chargeX) / (((x-chargeX)**2+(y-chargeY)**2)**(1.5) + epsilon)
                    self.Ey[i,j] += k*charge*(y-chargeY) / (((x-chargeX)**2+(y-chargeY)**2)**(1.5) + epsilon)

    def plot_electric_field(self):
        if (self.DARKMODE):
            self.LINE_COLOR = 'WHITE'
            plt.style.use('dark_background')
        else:
            self.LINE_COLOR = 'BLACK'

        plt.streamplot(self.X, self.Y, self.Ex, self.Ey, color=self.LINE_COLOR, density=1.5)
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.title(self.title)
        # Color Charge locations 
        for q in self.charges:  # mark charge locations
            qX, qY = q[1], q[2]
            color = 'r' if q[0] < 0 else 'b'
            circle = plt.Circle((qX, qY), radius=0.2, color=color)
            plt.gca().add_patch(circle)

        # Ensure circles are round
        plt.gca().set_aspect('equal')
        plt.show()

