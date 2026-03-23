import Plotter
import Capacitor as Cap
import numpy as np

# Creates a multipole with 2^n charges of alternating sign, equally spaced on unit circle
def AddMultiPole(plotter, n):
    nq = 2**int(n)
    for i in range(nq):
        # Charge values will either be -1 or 1
        charge = (i%2 * 2) - 1 
        # Around the unit circle
        plotter.place_charge(charge, (np.cos((2*np.pi) * (i/nq))),(np.sin((2*np.pi) * (i/nq))))

def functionCharge():
    # Initialize the E field Plotter with default arguments
    plotter = Plotter.EFieldVisualizer(-5, 5)
    plotter.title = "Electric Field of charges with positions as functions"
    # Lets create a ring of charge!
    plotter.DARKMODE = True
    AddMultiPole(plotter,3) 

    # Count number of charges
    print(f"{len(plotter.charges)} number of charges present in plot")

    # Show the plots for visualization
    plotter.calculate_electric_field()
    plotter.plot_electric_field()

functionCharge()