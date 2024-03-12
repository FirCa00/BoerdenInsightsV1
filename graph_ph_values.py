import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import pandas as pd
import os
from matplotlib.colors import LinearSegmentedColormap

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
element1 = element_columns[1]

colors = [(0, 'red'), (0.93, 'green'), (1, 'blue')]
blue_green_red_cmap = LinearSegmentedColormap.from_list('BlueGreenRed', colors)

fig, ax1 = plt.subplots(figsize=(6, 10))

# Create a LineCollection with a custom color gradient based on pH
points = list(zip(data[element1], data['Tiefe gemittelt (cm)']))
line_segments = [(points[i], points[i+1]) for i in range(len(points)-1)]
lc = LineCollection(line_segments, cmap=blue_green_red_cmap, linewidth=1, array=data[element1])
ax1.add_collection(lc)

# Add colorbar
cbar = plt.colorbar(lc, ax=ax1, label='pH-Wert')

# Scatter plot for original data points
sc = ax1.scatter(data[element1], data['Tiefe gemittelt (cm)'], c=data[element1], cmap=blue_green_red_cmap, edgecolors='k', linewidths=0.7)

# Set the z-order to bring scatter points to the front
sc.set_zorder(10)

plt.ylabel('Tiefe gemittelt (cm)')
plt.xlabel('pH-Wert')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.title('pH-Wert')
plt.grid(True)
plt.gca().invert_yaxis()
fig.tight_layout()
save_data('pH-Werte.png')
