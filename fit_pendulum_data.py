"""
File: fit_pendulum_data.py
Copyright (c) 2016 Andrew Malfavon
Exercise 5.18
License: MIT
Fits a polynomial to experimental data.
Graphs data points from an separate file.
"""

import numpy as np
import matplotlib.pyplot as plt

#Plot Length vs Period data from pendulum.dat
def plot_data():
    L_arr = []
    T_arr = []
    with open('pendulum.dat', 'r') as data:
        first_line = data.readline()
        for line in data:
            row = line.split()
            L_arr.append(float(row[0]))
            T_arr.append(float(row[1]))
        plt.plot(L_arr, T_arr, 'ko')
        plt.title('Oscillation Period of a Simple Pendulum')
        plt.xlabel('Length (L)')
        plt.ylabel('Period (T)')
        plt.xlim(0.0, 1.1)
        plt.ylim(0.4, 2.1)
        return [L_arr, T_arr]

#Plot the data again, also as first, second, and third degree polynomials
def poly_fit():
    f = plot_data()
    coeff1 = np.polyfit(f[0], f[1], 1)
    p1 = np.poly1d(coeff1)
    y_fitted1 = p1(f[0])
    coeff2 = np.polyfit(f[0], f[1], 2)
    p2 = np.poly1d(coeff2)
    y_fitted2 = p2(f[0])
    coeff3 = np.polyfit(f[0], f[1], 3)
    p3 = np.poly1d(coeff3)
    y_fitted3 = p3(f[0])
    plt.plot(f[0], f[1], 'ro', f[0], y_fitted1, f[0], y_fitted2, f[0], y_fitted3)
    plt.xlim(0.0, 1.1)
    plt.ylim(0.4, 2.3)