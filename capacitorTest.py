# Import custom modules
import Plotter
import Capacitor as Cap

def capacitorTest():
    # Initialize the E field Plotter with default arguments
    plotter = Plotter.EFieldVisualizer()
    plotter.title = "Electric Field of Parallel Plate Capacitor"

    plate_length = float(input("Enter plate length (centered at x=0): "))
    plate_separation = float(input("Enter plate separation (distance between plates): "))
    plate_charge = float(input("Enter the plate equilibrium charge (charge will be same on both sides just opposite signs):  "))

    # Build parallel plate capacitor
    Cap.build_parallel_plate_capacitor(plate_charge, plate_length, plate_separation, plotter.charges)
     
    # Count number of charges
    print(f"{len(plotter.charges)} number of charges present in plot")

    # Show the plots for visualization
    plotter.calculate_electric_field()
    plotter.plot_electric_field()

capacitorTest()