import json
import tkinter as tk
from tkinter import messagebox
import numpy as np
from scipy import interpolate

def load_data(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def interpolate_property(data, x_value, x_key, y_key):
    x_values = [record[x_key] for record in data]
    y_values = [record[y_key] for record in data]
    interpolator = interpolate.interp1d(x_values, y_values, fill_value="extrapolate")
    return float(interpolator(x_value))

def get_density_from_mass_fraction(data, mass_fraction):
    return interpolate_property(data, mass_fraction, 'mass_fraction', 'density')

def get_molar_concentration_from_mass_fraction(data, mass_fraction):
    return interpolate_property(data, mass_fraction, 'mass_fraction', 'molar_concentration')

def get_mass_fraction_from_density(data, density):
    return interpolate_property(data, density, 'density', 'mass_fraction')

def get_molar_concentration_from_density(data, density):
    return interpolate_property(data, density, 'density', 'molar_concentration')

def get_mass_fraction_from_molar_concentration(data, molar_concentration):
    return interpolate_property(data, molar_concentration, 'molar_concentration', 'mass_fraction')

def get_density_from_molar_concentration(data, molar_concentration):
    return interpolate_property(data, molar_concentration, 'molar_concentration', 'density')

def calculate_ph(molar_concentration, K2=0.0102, Kw=1e-14):
    # Solve cubic equation for [H+]
    a = 1
    b = K2 - molar_concentration
    c = -(2 * molar_concentration * K2 + Kw)
    d = -Kw * K2

    coeffs = [a, b, c, d]
    roots = np.roots(coeffs)
    H_plus = None
    for root in roots:
        if np.isreal(root) and root.real > 0:
            H_plus = root.real
            break
    if H_plus is None:
        return None
    return -np.log10(H_plus)

def get_molar_concentration_from_ph(ph, K2=0.0102, Kw=1e-14):
    H_plus = 10 ** (-ph)
    numerator = H_plus ** 3 + K2 * H_plus ** 2 - Kw * H_plus - Kw * K2
    denominator = H_plus ** 2 + 2 * K2 * H_plus
    return numerator / denominator

# Load the data
json_file_path = 'mass_density_molar_data.json'
data = load_data(json_file_path)

# Create the UI using Tkinter
def calculate():
    mass_fraction = mass_fraction_entry.get()
    density = density_entry.get()
    molar_concentration = molar_concentration_entry.get()
    ph_value = ph_entry.get()

    try:
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