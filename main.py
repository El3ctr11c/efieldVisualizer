import matplotlib.pyplot as plt
import numpy as np

import Plotter

def main():
    # Initialize the E field Plotter with default arguments
    plotter = Plotter.EFieldVisualizer()
    # Ask which file to open (including file type)
    fileName = input("Enter the file to visualize: ").strip()

    # Open and read file
    with open("tests\\" + fileName, 'r') as file:
        for line in file:
            numbers = line.strip().split()
            if len(numbers) == 3:
                charge = float(numbers[0])
                chargeX = float(numbers[1])
                chargeY = float(numbers[2])
                plotter.place_charge(charge, chargeX, chargeY)
            else:
                print("Invalid text file format! Exiting Program")
                return -1
    print("File opened and read successfully")

    plotter.calculate_electric_field()
    plotter.plot_electric_field()
    

if __name__ == "__main__":
    main()