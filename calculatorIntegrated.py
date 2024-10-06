import tkinter as tk
from tkinter import messagebox
import numpy as np
from scipy import interpolate

# Data integrated into the script
data = [
    {
        "mass_fraction": 0.3,
        "density": 1.0,
        "molar_concentration": 0.0306122449
    },
    {
        "mass_fraction": 1.0,
        "density": 1.005,
        "molar_concentration": 0.1025510204
    },
    {
        "mass_fraction": 1.7,
        "density": 1.01,
        "molar_concentration": 0.1752040816
    },
    {
        "mass_fraction": 2.5,
        "density": 1.015,
        "molar_concentration": 0.2589285714
    },
    {
        "mass_fraction": 3.2,
        "density": 1.02,
        "molar_concentration": 0.3330612245
    },
    {
        "mass_fraction": 4.0,
        "density": 1.025,
        "molar_concentration": 0.4183673469
    },
    {
        "mass_fraction": 4.7,
        "density": 1.03,
        "molar_concentration": 0.4939795918
    },
    {
        "mass_fraction": 5.5,
        "density": 1.035,
        "molar_concentration": 0.5808673469
    },
    {
        "mass_fraction": 6.2,
        "density": 1.04,
        "molar_concentration": 0.6579591837
    },
    {
        "mass_fraction": 7.0,
        "density": 1.045,
        "molar_concentration": 0.7464285714
    },
    {
        "mass_fraction": 7.7,
        "density": 1.05,
        "molar_concentration": 0.825
    },
    {
        "mass_fraction": 8.4,
        "density": 1.055,
        "molar_concentration": 0.9042857143
    },
    {
        "mass_fraction": 9.1,
        "density": 1.06,
        "molar_concentration": 0.9842857143
    },
    {
        "mass_fraction": 9.8,
        "density": 1.065,
        "molar_concentration": 1.065
    },
    {
        "mass_fraction": 10.6,
        "density": 1.07,
        "molar_concentration": 1.1573469388
    },
    {
        "mass_fraction": 11.3,
        "density": 1.075,
        "molar_concentration": 1.2395408163
    },
    {
        "mass_fraction": 12.0,
        "density": 1.08,
        "molar_concentration": 1.3224489796
    },
    {
        "mass_fraction": 12.7,
        "density": 1.085,
        "molar_concentration": 1.4060714286
    },
    {
        "mass_fraction": 13.4,
        "density": 1.09,
        "molar_concentration": 1.4904081633
    },
    {
        "mass_fraction": 14.0,
        "density": 1.095,
        "molar_concentration": 1.5642857143
    },
    {
        "mass_fraction": 14.7,
        "density": 1.1,
        "molar_concentration": 1.65
    },
    {
        "mass_fraction": 15.4,
        "density": 1.105,
        "molar_concentration": 1.7364285714
    },
    {
        "mass_fraction": 16.1,
        "density": 1.11,
        "molar_concentration": 1.8235714286
    },
    {
        "mass_fraction": 16.7,
        "density": 1.115,
        "molar_concentration": 1.9000510204
    },
    {
        "mass_fraction": 17.4,
        "density": 1.12,
        "molar_concentration": 1.9885714286
    },
    {
        "mass_fraction": 18.1,
        "density": 1.125,
        "molar_concentration": 2.0778061224
    },
    {
        "mass_fraction": 18.8,
        "density": 1.13,
        "molar_concentration": 2.167755102
    },
    {
        "mass_fraction": 19.4,
        "density": 1.135,
        "molar_concentration": 2.2468367347
    },
    {
        "mass_fraction": 20.1,
        "density": 1.14,
        "molar_concentration": 2.3381632653
    },
    {
        "mass_fraction": 20.7,
        "density": 1.145,
        "molar_concentration": 2.4185204082
    },
    {
        "mass_fraction": 21.4,
        "density": 1.15,
        "molar_concentration": 2.5112244898
    },
    {
        "mass_fraction": 22.0,
        "density": 1.155,
        "molar_concentration": 2.5928571429
    },
    {
        "mass_fraction": 22.7,
        "density": 1.16,
        "molar_concentration": 2.6869387755
    },
    {
        "mass_fraction": 23.3,
        "density": 1.165,
        "molar_concentration": 2.7698469388
    },
    {
        "mass_fraction": 23.9,
        "density": 1.17,
        "molar_concentration": 2.8533673469
    },
    {
        "mass_fraction": 24.6,
        "density": 1.175,
        "molar_concentration": 2.9494897959
    },
    {
        "mass_fraction": 25.2,
        "density": 1.18,
        "molar_concentration": 3.0342857143
    },
    {
        "mass_fraction": 25.8,
        "density": 1.185,
        "molar_concentration": 3.1196938776
    },
    {
        "mass_fraction": 26.5,
        "density": 1.19,
        "molar_concentration": 3.2178571429
    },
    {
        "mass_fraction": 27.1,
        "density": 1.195,
        "molar_concentration": 3.3045408163
    },
    {
        "mass_fraction": 27.7,
        "density": 1.2,
        "molar_concentration": 3.3918367347
    },
    {
        "mass_fraction": 28.3,
        "density": 1.205,
        "molar_concentration": 3.479744898
    },
    {
        "mass_fraction": 28.9,
        "density": 1.21,
        "molar_concentration": 3.5682653061
    },
    {
        "mass_fraction": 29.6,
        "density": 1.215,
        "molar_concentration": 3.6697959184
    },
    {
        "mass_fraction": 30.2,
        "density": 1.22,
        "molar_concentration": 3.7595918367
    },
    {
        "mass_fraction": 30.8,
        "density": 1.225,
        "molar_concentration": 3.85
    },
    {
        "mass_fraction": 31.4,
        "density": 1.23,
        "molar_concentration": 3.9410204082
    },
    {
        "mass_fraction": 32.0,
        "density": 1.235,
        "molar_concentration": 4.0326530612
    },
    {
        "mass_fraction": 32.6,
        "density": 1.24,
        "molar_concentration": 4.1248979592
    },
    {
        "mass_fraction": 33.2,
        "density": 1.245,
        "molar_concentration": 4.217755102
    },
    {
        "mass_fraction": 33.8,
        "density": 1.25,
        "molar_concentration": 4.3112244898
    },
    {
        "mass_fraction": 34.4,
        "density": 1.255,
        "molar_concentration": 4.4053061224
    },
    {
        "mass_fraction": 35.0,
        "density": 1.26,
        "molar_concentration": 4.5
    },
    {
        "mass_fraction": 35.6,
        "density": 1.265,
        "molar_concentration": 4.5953061224
    },
    {
        "mass_fraction": 36.2,
        "density": 1.27,
        "molar_concentration": 4.6912244898
    },
    {
        "mass_fraction": 36.8,
        "density": 1.275,
        "molar_concentration": 4.787755102
    },
    {
        "mass_fraction": 37.4,
        "density": 1.28,
        "molar_concentration": 4.8848979592
    },
    {
        "mass_fraction": 37.9,
        "density": 1.285,
        "molar_concentration": 4.9695408163
    },
    {
        "mass_fraction": 38.5,
        "density": 1.29,
        "molar_concentration": 5.0678571429
    },
    {
        "mass_fraction": 39.1,
        "density": 1.295,
        "molar_concentration": 5.1667857143
    },
    {
        "mass_fraction": 39.7,
        "density": 1.3,
        "molar_concentration": 5.2663265306
    },
    {
        "mass_fraction": 40.2,
        "density": 1.305,
        "molar_concentration": 5.3531632653
    },
    {
        "mass_fraction": 40.8,
        "density": 1.31,
        "molar_concentration": 5.453877551
    },
    {
        "mass_fraction": 41.4,
        "density": 1.315,
        "molar_concentration": 5.5552040816
    },
    {
        "mass_fraction": 41.9,
        "density": 1.32,
        "molar_concentration": 5.6436734694
    },
    {
        "mass_fraction": 42.5,
        "density": 1.325,
        "molar_concentration": 5.7461734694
    },
    {
        "mass_fraction": 43.1,
        "density": 1.33,
        "molar_concentration": 5.8492857143
    },
    {
        "mass_fraction": 43.6,
        "density": 1.335,
        "molar_concentration": 5.9393877551
    },
    {
        "mass_fraction": 44.2,
        "density": 1.34,
        "molar_concentration": 6.0436734694
    },
    {
        "mass_fraction": 44.7,
        "density": 1.345,
        "molar_concentration": 6.1348469388
    },
    {
        "mass_fraction": 45.3,
        "density": 1.35,
        "molar_concentration": 6.2403061224
    },
    {
        "mass_fraction": 45.8,
        "density": 1.355,
        "molar_concentration": 6.3325510204
    },
    {
        "mass_fraction": 46.3,
        "density": 1.36,
        "molar_concentration": 6.4253061224
    },
    {
        "mass_fraction": 46.9,
        "density": 1.365,
        "molar_concentration": 6.5325
    },
    {
        "mass_fraction": 47.4,
        "density": 1.37,
        "molar_concentration": 6.6263265306
    },
    {
        "mass_fraction": 47.9,
        "density": 1.375,
        "molar_concentration": 6.7206632653
    },
    {
        "mass_fraction": 48.4,
        "density": 1.38,
        "molar_concentration": 6.8155102041
    },
    {
        "mass_fraction": 49.0,
        "density": 1.385,
        "molar_concentration": 6.925
    },
    {
        "mass_fraction": 49.5,
        "density": 1.39,
        "molar_concentration": 7.0209183673
    },
    {
        "mass_fraction": 50.0,
        "density": 1.395,
        "molar_concentration": 7.1173469388
    },
    {
        "mass_fraction": 50.5,
        "density": 1.4,
        "molar_concentration": 7.2142857143
    },
    {
        "mass_fraction": 51.0,
        "density": 1.405,
        "molar_concentration": 7.3117346939
    },
    {
        "mass_fraction": 51.5,
        "density": 1.41,
        "molar_concentration": 7.4096938776
    },
    {
        "mass_fraction": 52.0,
        "density": 1.415,
        "molar_concentration": 7.5081632653
    },
    {
        "mass_fraction": 52.5,
        "density": 1.42,
        "molar_concentration": 7.6071428571
    },
    {
        "mass_fraction": 53.0,
        "density": 1.425,
        "molar_concentration": 7.7066326531
    },
    {
        "mass_fraction": 53.5,
        "density": 1.43,
        "molar_concentration": 7.8066326531
    },
    {
        "mass_fraction": 54.0,
        "density": 1.435,
        "molar_concentration": 7.9071428571
    },
    {
        "mass_fraction": 54.5,
        "density": 1.44,
        "molar_concentration": 8.0081632653
    },
    {
        "mass_fraction": 55.0,
        "density": 1.445,
        "molar_concentration": 8.1096938776
    },
    {
        "mass_fraction": 55.4,
        "density": 1.45,
        "molar_concentration": 8.1969387755
    },
    {
        "mass_fraction": 55.9,
        "density": 1.455,
        "molar_concentration": 8.2994387755
    },
    {
        "mass_fraction": 56.4,
        "density": 1.46,
        "molar_concentration": 8.4024489796
    },
    {
        "mass_fraction": 56.9,
        "density": 1.465,
        "molar_concentration": 8.5059693878
    },
    {
        "mass_fraction": 57.4,
        "density": 1.47,
        "molar_concentration": 8.61
    },
    {
        "mass_fraction": 57.8,
        "density": 1.475,
        "molar_concentration": 8.6994897959
    },
    {
        "mass_fraction": 58.3,
        "density": 1.48,
        "molar_concentration": 8.8044897959
    },
    {
        "mass_fraction": 58.8,
        "density": 1.485,
        "molar_concentration": 8.91
    },
    {
        "mass_fraction": 59.2,
        "density": 1.49,
        "molar_concentration": 9.0008163265
    },
    {
        "mass_fraction": 59.7,
        "density": 1.495,
        "molar_concentration": 9.1072959184
    },
    {
        "mass_fraction": 60.2,
        "density": 1.5,
        "molar_concentration": 9.2142857143
    },
    {
        "mass_fraction": 60.6,
        "density": 1.505,
        "molar_concentration": 9.3064285714
    },
    {
        "mass_fraction": 61.1,
        "density": 1.51,
        "molar_concentration": 9.4143877551
    },
    {
        "mass_fraction": 61.5,
        "density": 1.515,
        "molar_concentration": 9.5073979592
    },
    {
        "mass_fraction": 62.0,
        "density": 1.52,
        "molar_concentration": 9.6163265306
    },
    {
        "mass_fraction": 62.4,
        "density": 1.525,
        "molar_concentration": 9.7102040816
    },
    {
        "mass_fraction": 62.9,
        "density": 1.53,
        "molar_concentration": 9.8201020408
    },
    {
        "mass_fraction": 63.4,
        "density": 1.535,
        "molar_concentration": 9.9305102041
    },
    {
        "mass_fraction": 63.8,
        "density": 1.54,
        "molar_concentration": 10.0257142857
    },
    {
        "mass_fraction": 64.3,
        "density": 1.545,
        "molar_concentration": 10.1370918367
    },
    {
        "mass_fraction": 64.7,
        "density": 1.55,
        "molar_concentration": 10.2331632653
    },
    {
        "mass_fraction": 65.1,
        "density": 1.555,
        "molar_concentration": 10.3296428571
    },
    {
        "mass_fraction": 65.6,
        "density": 1.56,
        "molar_concentration": 10.4424489796
    },
    {
        "mass_fraction": 66.0,
        "density": 1.565,
        "molar_concentration": 10.5397959184
    },
    {
        "mass_fraction": 66.5,
        "density": 1.57,
        "molar_concentration": 10.6535714286
    },
    {
        "mass_fraction": 66.9,
        "density": 1.575,
        "molar_concentration": 10.7517857143
    },
    {
        "mass_fraction": 67.8,
        "density": 1.585,
        "molar_concentration": 10.9656122449
    },
    {
        "mass_fraction": 68.2,
        "density": 1.59,
        "molar_concentration": 11.0651020408
    },
    {
        "mass_fraction": 68.7,
        "density": 1.595,
        "molar_concentration": 11.1812755102
    },
    {
        "mass_fraction": 69.1,
        "density": 1.6,
        "molar_concentration": 11.2816326531
    },
    {
        "mass_fraction": 69.5,
        "density": 1.605,
        "molar_concentration": 11.3823979592
    },
    {
        "mass_fraction": 70.0,
        "density": 1.61,
        "molar_concentration": 11.5
    },
    {
        "mass_fraction": 70.4,
        "density": 1.615,
        "molar_concentration": 11.6016326531
    },
    {
        "mass_fraction": 70.8,
        "density": 1.62,
        "molar_concentration": 11.7036734694
    },
    {
        "mass_fraction": 71.2,
        "density": 1.625,
        "molar_concentration": 11.806122449
    },
    {
        "mass_fraction": 71.7,
        "density": 1.63,
        "molar_concentration": 11.9256122449
    },
    {
        "mass_fraction": 72.1,
        "density": 1.635,
        "molar_concentration": 12.0289285714
    },
    {
        "mass_fraction": 72.5,
        "density": 1.64,
        "molar_concentration": 12.1326530612
    },
    {
        "mass_fraction": 72.9,
        "density": 1.645,
        "molar_concentration": 12.2367857143
    },
    {
        "mass_fraction": 73.4,
        "density": 1.65,
        "molar_concentration": 12.3581632653
    },
    {
        "mass_fraction": 73.8,
        "density": 1.655,
        "molar_concentration": 12.4631632653
    },
    {
        "mass_fraction": 74.2,
        "density": 1.66,
        "molar_concentration": 12.5685714286
    },
    {
        "mass_fraction": 74.6,
        "density": 1.665,
        "molar_concentration": 12.6743877551
    },
    {
        "mass_fraction": 75.1,
        "density": 1.67,
        "molar_concentration": 12.7976530612
    },
    {
        "mass_fraction": 75.5,
        "density": 1.675,
        "molar_concentration": 12.9043367347
    },
    {
        "mass_fraction": 75.9,
        "density": 1.68,
        "molar_concentration": 13.0114285714
    },
    {
        "mass_fraction": 76.3,
        "density": 1.685,
        "molar_concentration": 13.1189285714
    },
    {
        "mass_fraction": 76.8,
        "density": 1.69,
        "molar_concentration": 13.2440816327
    },
    {
        "mass_fraction": 77.2,
        "density": 1.695,
        "molar_concentration": 13.3524489796
    },
    {
        "mass_fraction": 77.6,
        "density": 1.7,
        "molar_concentration": 13.4612244898
    },
    {
        "mass_fraction": 78.5,
        "density": 1.71,
        "molar_concentration": 13.6974489796
    },
    {
        "mass_fraction": 78.9,
        "density": 1.715,
        "molar_concentration": 13.8075
    },
    {
        "mass_fraction": 79.4,
        "density": 1.72,
        "molar_concentration": 13.9355102041
    },
    {
        "mass_fraction": 79.8,
        "density": 1.725,
        "molar_concentration": 14.0464285714
    },
    {
        "mass_fraction": 80.2,
        "density": 1.73,
        "molar_concentration": 14.157755102
    },
    {
        "mass_fraction": 80.7,
        "density": 1.735,
        "molar_concentration": 14.2871938776
    },
    {
        "mass_fraction": 81.2,
        "density": 1.74,
        "molar_concentration": 14.4171428571
    },
    {
        "mass_fraction": 81.6,
        "density": 1.745,
        "molar_concentration": 14.5297959184
    },
    {
        "mass_fraction": 82.1,
        "density": 1.75,
        "molar_concentration": 14.6607142857
    },
    {
        "mass_fraction": 82.6,
        "density": 1.755,
        "molar_concentration": 14.7921428571
    },
    {
        "mass_fraction": 83.1,
        "density": 1.76,
        "molar_concentration": 14.9240816327
    },
    {
        "mass_fraction": 83.6,
        "density": 1.765,
        "molar_concentration": 15.0565306122
    },
    {
        "mass_fraction": 84.1,
        "density": 1.77,
        "molar_concentration": 15.1894897959
    },
    {
        "mass_fraction": 84.6,
        "density": 1.775,
        "molar_concentration": 15.3229591837
    },
    {
        "mass_fraction": 85.2,
        "density": 1.78,
        "molar_concentration": 15.4751020408
    },
    {
        "mass_fraction": 85.7,
        "density": 1.785,
        "molar_concentration": 15.6096428571
    },
    {
        "mass_fraction": 86.3,
        "density": 1.79,
        "molar_concentration": 15.7629591837
    },
    {
        "mass_fraction": 87.0,
        "density": 1.795,
        "molar_concentration": 15.9352040816
    },
    {
        "mass_fraction": 87.7,
        "density": 1.8,
        "molar_concentration": 16.1081632653
    },
    {
        "mass_fraction": 88.4,
        "density": 1.805,
        "molar_concentration": 16.2818367347
    },
    {
        "mass_fraction": 89.2,
        "density": 1.81,
        "molar_concentration": 16.4746938776
    },
    {
        "mass_fraction": 90.1,
        "density": 1.815,
        "molar_concentration": 16.6868877551
    },
    {
        "mass_fraction": 91.1,
        "density": 1.82,
        "molar_concentration": 16.9185714286
    },
    {
        "mass_fraction": 92.2,
        "density": 1.825,
        "molar_concentration": 17.1698979592
    },
    {
        "mass_fraction": 95.7,
        "density": 1.835,
        "molar_concentration": 17.9193367347
    },
    {
        "mass_fraction": 97.0,
        "density": 1.836,
        "molar_concentration": 18.1726530612
    },
    {
        "mass_fraction": 98.0,
        "density": 1.84,
        "molar_concentration": 18.4
    }
]

# Function to interpolate between data points to find the desired property
def interpolate_property(data, x_value, x_key, y_key):
    # Extract the x and y values from the data for interpolation
    x_values = [record[x_key] for record in data]
    y_values = [record[y_key] for record in data]
    # Create an interpolation function
    interpolator = interpolate.interp1d(x_values, y_values, fill_value="extrapolate")
    # Use the interpolator to find the y value corresponding to the given x value
    return float(interpolator(x_value))

# Functions to get properties based on different inputs using interpolation

def get_density_from_mass_fraction(data, mass_fraction):
    """
    Given a mass fraction, return the corresponding density.
    """
    return interpolate_property(data, mass_fraction, 'mass_fraction', 'density')

def get_molar_concentration_from_mass_fraction(data, mass_fraction):
    """
    Given a mass fraction, return the corresponding molar concentration.
    """
    return interpolate_property(data, mass_fraction, 'mass_fraction', 'molar_concentration')

def get_mass_fraction_from_density(data, density):
    """
    Given a density, return the corresponding mass fraction.
    """
    return interpolate_property(data, density, 'density', 'mass_fraction')

def get_molar_concentration_from_density(data, density):
    """
    Given a density, return the corresponding molar concentration.
    """
    return interpolate_property(data, density, 'density', 'molar_concentration')

def get_mass_fraction_from_molar_concentration(data, molar_concentration):
    """
    Given a molar concentration, return the corresponding mass fraction.
    """
    return interpolate_property(data, molar_concentration, 'molar_concentration', 'mass_fraction')

def get_density_from_molar_concentration(data, molar_concentration):
    """
    Given a molar concentration, return the corresponding density.
    """
    return interpolate_property(data, molar_concentration, 'molar_concentration', 'density')

# Function to calculate the pH value based on the molar concentration of sulfuric acid
def calculate_ph(molar_concentration, K2=0.0102, Kw=1e-14):
    """
    Calculate the pH of sulfuric acid considering its diprotic nature.
    The first dissociation is complete, while the second is partial.
    """
    # Coefficients of the cubic equation for [H+]
    a = 1
    b = K2 - molar_concentration
    c = -(2 * molar_concentration * K2 + Kw)
    d = -Kw * K2

    # Solve the cubic equation
    coeffs = [a, b, c, d]
    roots = np.roots(coeffs)
    # Select the positive real root as the hydrogen ion concentration
    H_plus = None
    for root in roots:
        if np.isreal(root) and root.real > 0:
            H_plus = root.real
            break
    if H_plus is None:
        return None
    # Calculate and return the pH value
    return -np.log10(H_plus)

# Function to get the molar concentration from a given pH value
def get_molar_concentration_from_ph(ph, K2=0.0102, Kw=1e-14):
    """
    Given a pH value, calculate the molar concentration of sulfuric acid.
    """
    H_plus = 10 ** (-ph)
    numerator = H_plus ** 3 + K2 * H_plus ** 2 - Kw * H_plus - Kw * K2
    denominator = H_plus ** 2 + 2 * K2 * H_plus
    return numerator / denominator

# Create the UI using Tkinter
def calculate():
    """
    Calculate the values of mass fraction, density, molar concentration, and pH based on the user's input.
    """
    mass_fraction = mass_fraction_entry.get()
    density = density_entry.get()
    molar_concentration = molar_concentration_entry.get()
    ph_value = ph_entry.get()

    try:
        # Determine which value is provided and calculate the others
        if mass_fraction:
            mass_fraction = float(mass_fraction)
            density = get_density_from_mass_fraction(data, mass_fraction)
            molar_concentration = get_molar_concentration_from_mass_fraction(data, mass_fraction)
            ph_value = calculate_ph(molar_concentration)
        elif density:
            density = float(density)
            mass_fraction = get_mass_fraction_from_density(data, density)
            molar_concentration = get_molar_concentration_from_density(data, density)
            ph_value = calculate_ph(molar_concentration)
        elif molar_concentration:
            molar_concentration = float(molar_concentration)
            mass_fraction = get_mass_fraction_from_molar_concentration(data, molar_concentration)
            density = get_density_from_molar_concentration(data, molar_concentration)
            ph_value = calculate_ph(molar_concentration)
        elif ph_value:
            ph_value = float(ph_value)
            molar_concentration = get_molar_concentration_from_ph(ph_value)
            mass_fraction = get_mass_fraction_from_molar_concentration(data, molar_concentration)
            density = get_density_from_molar_concentration(data, molar_concentration)
        else:
            messagebox.showerror("Input Error", "Please enter at least one value.")
            return

        # Update the entry fields with the calculated values
        mass_fraction_entry.delete(0, tk.END)
        density_entry.delete(0, tk.END)
        molar_concentration_entry.delete(0, tk.END)
        ph_entry.delete(0, tk.END)

        mass_fraction_entry.insert(0, str(mass_fraction))
        density_entry.insert(0, str(density))
        molar_concentration_entry.insert(0, str(molar_concentration))
        ph_entry.insert(0, str(ph_value))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

def clear_fields():
    """
    Clear all input and output fields.
    """
    mass_fraction_entry.delete(0, tk.END)
    density_entry.delete(0, tk.END)
    molar_concentration_entry.delete(0, tk.END)
    ph_entry.delete(0, tk.END)

# Set up the Tkinter window
root = tk.Tk()
root.title("Mass Fraction, Density, Molar Concentration, and pH Converter")

# Create and place labels and entry widgets
mass_fraction_label = tk.Label(root, text="Mass Fraction (%):")
mass_fraction_label.grid(row=0, column=0, padx=10, pady=5)
mass_fraction_entry = tk.Entry(root)
mass_fraction_entry.grid(row=0, column=1, padx=10, pady=5)

density_label = tk.Label(root, text="Density (g/cm3):")
density_label.grid(row=1, column=0, padx=10, pady=5)
density_entry = tk.Entry(root)
density_entry.grid(row=1, column=1, padx=10, pady=5)

molar_concentration_label = tk.Label(root, text="Molar Concentration (mol/L):")
molar_concentration_label.grid(row=2, column=0, padx=10, pady=5)
molar_concentration_entry = tk.Entry(root)
molar_concentration_entry.grid(row=2, column=1, padx=10, pady=5)

ph_label = tk.Label(root, text="pH Value:")
ph_label.grid(row=3, column=0, padx=10, pady=5)
ph_entry = tk.Entry(root)
ph_entry.grid(row=3, column=1, padx=10, pady=5)

# Create and place the Calculate and Clear buttons side by side
button_frame = tk.Frame(root)
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

calculate_button = tk.Button(button_frame, text="Calculate", command=calculate)
calculate_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_fields)
clear_button.grid(row=0, column=1, padx=5)

# Start the Tkinter main loop
root.mainloop()