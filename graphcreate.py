import matplotlib.pyplot as plt
import pandas as pd
import os

file_path = ''  # insert string containing the file path

data = pd.read_excel(file_path, sheet_name='Tabelle1')
save_folder = " "  # insert saving path here
os.makedirs(save_folder, exist_ok=True)


def save_data(plot_name):
    file_name = os.path.join(save_folder, f'{plot_name}.png')
    plt.savefig(file_name, format='png', dpi=400)


# Extracting element column names, excluding non-element columns
element_columns = data.columns[5:]

# plot all elements against depth
plt.figure(figsize=(15, 20))
for element in element_columns:
    plt.plot(data[element], data['Tiefe gemittelt (cm)'], label=element)

plot_title = 'Element Concentrations per Depth'
plt.ylabel('Tiefe gemittelt (cm)')
plt.xlabel('Concentration')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.title(plot_title)
plt.legend(loc='best', ncol=2, frameon=True, shadow=True, framealpha=1, facecolor='white',
           edgecolor='black',title='Legende', title_fontsize='13', fontsize='11', fancybox=True)
plt.grid(True)
plt.gca().invert_yaxis()  # invert y-axis to clarify depth
save_data(plot_title)

# Display plot
# plt.show()

# plotting elements Al-Mn
plt.figure(figsize=(15, 20))
for i, element in enumerate(element_columns):
    if i <= 9:
        plt.plot(data[element], data['Tiefe gemittelt (cm)'], label=element)
    else:
        break

plot_title = 'Element Concentrations per Depth'
plt.ylabel('Tiefe gemittelt (cm)')
plt.xlabel('Concentration')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.title(plot_title)
plt.legend(loc='best',ncol = 2, frameon=True, shadow=True, framealpha=1, facecolor='white', edgecolor='black', title='Legende', title_fontsize='13', fontsize='11', fancybox=True)
plt.grid(True)
plt.gca().invert_yaxis()

save_data(plot_title)

# plt.show()

# plotting elements K + Fe
element1 = element_columns[4]
element2 = element_columns[10]

fig, ax1 = plt.subplots(figsize=(6, 10))

# First x-axis (at the bottom) and corresponding y-axis
color = 'tab:red'
ax1.set_ylabel('Tiefe gemittelt (cm)')
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
ax1.set_xlabel(element1, color=color)
ax1.plot(data[element1], data['Tiefe gemittelt (cm)'], color=color)
ax1.tick_params(axis='y')
ax1.invert_yaxis()

# Second x-axis (at the top), reusing y-axis from before
ax2 = ax1.twiny()
color = 'tab:blue'
ax2.set_xlabel(element2, color=color)
ax2.plot(data[element2], data['Tiefe gemittelt (cm)'], color=color)
ax2.tick_params(axis='x')
fig.tight_layout()
save_data('Element_Concentrations_per_Depth_K_Fe')

# plotting elements Si + Al, using same code as before
element1 = element_columns[1]
element2 = element_columns[0]

fig, ax1 = plt.subplots(figsize=(6, 10))

color = 'tab:grey'
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
ax1.set_ylabel('Tiefe gemittelt (cm)')
ax1.set_xlabel(element1, color=color)
ax1.plot(data[element1], data['Tiefe gemittelt (cm)'], color=color)
ax1.tick_params(axis='y')

ax2 = ax1.twiny()
color = 'tab:pink'
ax2.set_xlabel(element2, color=color)
ax2.plot(data[element2], data['Tiefe gemittelt (cm)'], color=color)
ax2.tick_params(axis='x')
ax2.invert_yaxis()
fig.tight_layout()

save_data('Element_Concentrations_per_Depth_Si_Al.png')

# Creating individual plots for each element, with improved aesthetics
for element in element_columns:
    plt.figure(figsize=(6, 10))
    plt.plot(data[element], data['Tiefe gemittelt (cm)'], linestyle='-', color='teal')
    plt.title(f'{element} Concentration vs. Tiefe gemittelt (cm)')
    plt.ylabel('Tiefe gemittelt (cm)')
    plt.xlabel(f'{element} Concentration')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()  # Adjust the layout to make room for the elements
    plt.gca().invert_yaxis()
    save_data(f'{element}.png')
