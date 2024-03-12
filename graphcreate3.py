import matplotlib.pyplot as plt
import pandas as pd
import os

file_path = " "  # insert path to Excel file here

data = pd.read_excel(file_path, sheet_name='')  # insert sheet-name here
save_folder = " "  # insert saving path here
os.makedirs(save_folder, exist_ok=True)


def save_data(plot_name):
    file_name = os.path.join(save_folder, f'{plot_name}.png')
    plt.savefig(file_name, format='png', dpi=400)


# Extracting element column names, excluding non-element columns
element_columns = data.columns[1:]

# plotting TN + TOC
element1 = element_columns[2]
element2 = element_columns[1]

fig, ax1 = plt.subplots(figsize=(6, 10))

# First x-axis (at the bottom) and corresponding y-axis
color = 'tab:blue'
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
ax1.set_ylabel('mittlere Tiefe (cm)')
ax1.set_xlabel(element1, color=color)
ax1.plot(data[element1], data['mittlere Tiefe (cm)'], color=color)
ax1.tick_params(axis='y')

# Second x-axis (at the top), reusing y-axis from before
ax2 = ax1.twiny()
color = 'tab:pink'
ax2.set_xlabel(element2, color=color)
ax2.plot(data[element2], data['mittlere Tiefe (cm)'], color=color)
ax2.tick_params(axis='x')
ax2.invert_yaxis()
fig.tight_layout()
save_data('TOC_TN.png')

# plotting TIC, using same code as before
element3 = element_columns[3]

plt.figure(figsize=(6, 10))

color = 'tab:orange'
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.ylabel('mittlere Tiefe (cm)')
plt.xlabel(element3, color=color)
plt.plot(data[element3], data['mittlere Tiefe (cm)'], color=color)
plt.gca().invert_yaxis()
fig.tight_layout()
save_data('TIC.png')
