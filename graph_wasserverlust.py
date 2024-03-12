import matplotlib.pyplot as plt
import pandas as pd
import os

file_path = " "  # insert path to Excel file here

data = pd.read_excel(file_path, sheet_name='Tabelle1')
save_folder = " "  # insert saving path here
os.makedirs(save_folder, exist_ok=True)


def save_data(plot_name):
    file_name = os.path.join(save_folder, f'{plot_name}.png')
    plt.savefig(file_name, format='png', dpi=400)


# Extracting element column names, excluding non-element columns
element_columns = data.columns[5:]

# Plotting pH
element1 = element_columns[7]
element2 = element_columns[8]

# Create a Figure and an Axis
fig, ax1 = plt.subplots(figsize=(6, 10))

# First x-axis (at the bottom) and corresponding y-axis
color = 'tab:orange'
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
ax1.set_ylabel('Tiefe gemittelt (cm)')
ax1.set_xlabel(element1, color=color)
ax1.plot(data[element1], data['Tiefe gemittelt (cm)'], color=color)
ax1.tick_params(axis='y')
ax1.invert_yaxis()

# Second x-axis (at the top), reusing y-axis from before
ax2 = ax1.twiny()
color = 'tab:purple'
ax2.set_xlabel(element2, color=color)
ax2.plot(data[element2], data['Tiefe gemittelt (cm)'], color=color)
ax2.tick_params(axis='x')
fig.tight_layout()
save_data('Glueh+Wasserverlust.png')
