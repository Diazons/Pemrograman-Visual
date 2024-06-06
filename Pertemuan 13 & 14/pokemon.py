import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
file_path = 'pokemon_data.csv'
pokemon_data = pd.read_csv(file_path)

# Prepare data for visualizations

# Type by Height
height_data = pokemon_data.groupby('type1')['height'].mean().to_dict()

# Type by Weight
weight_data = pokemon_data.groupby('type1')['weight'].mean().to_dict()

# Type Breakdown
pokemon_type_data = pokemon_data['type1'].value_counts().to_dict()

# Total Power by Year (generation)
power_generation_data = pokemon_data.groupby('generation')['total'].sum().to_dict()

# Update color scheme to match Pokéball theme
colors = ["#FF0000", "#FFFFFF", "#000000"]  # Red, White, Black

# Chart 1: Bar chart of height data
fig1, ax1 = plt.subplots()
ax1.bar(height_data.keys(), height_data.values(), color=colors[0])
ax1.set_title("Type by Height")
ax1.set_xlabel("Type")
ax1.set_ylabel("Height")
ax1.tick_params(axis='x', rotation=90)
ax1.set_xticks(range(len(height_data)))
ax1.set_xticklabels(height_data.keys(), fontsize=8)
ax1.yaxis.set_tick_params(color=colors[2], labelcolor=colors[2])
ax1.xaxis.set_tick_params(color=colors[2], labelcolor=colors[2])
ax1.spines['bottom'].set_color(colors[2])
ax1.spines['left'].set_color(colors[2])
ax1.title.set_color(colors[2])

# Chart 2: Horizontal bar chart of weight data
fig2, ax2 = plt.subplots()
ax2.barh(list(weight_data.keys()), weight_data.values(), color=colors[0])
ax2.set_title("Type by Weight")
ax2.set_xlabel("Weight")
ax2.set_ylabel("Type")
ax2.set_yticks(range(len(weight_data)))
ax2.set_yticklabels(weight_data.keys(), fontsize=8)
ax2.yaxis.set_tick_params(color=colors[2], labelcolor=colors[2])
ax2.xaxis.set_tick_params(color=colors[2], labelcolor=colors[2])
ax2.spines['bottom'].set_color(colors[2])
ax2.spines['left'].set_color(colors[2])
ax2.title.set_color(colors[2])

# Chart 3: Pie chart of type pokemon data
fig3, ax3 = plt.subplots(figsize=(8, 6))
ax3.pie(pokemon_type_data.values(), labels=pokemon_type_data.keys(), autopct='%1.1f%%', textprops={'fontsize': 8, 'color': colors[2]}, colors=[colors[0], colors[1], colors[2]])
ax3.set_title("Type Pokemon \nBreakdown", color=colors[2])

# Chart 4: Line chart of Total Power by Generation
fig4, ax4 = plt.subplots()
ax4.plot(list(power_generation_data.keys()), list(power_generation_data.values()), color=colors[0])
ax4.set_title("Total Power by Generation")
ax4.set_xlabel("Generation")
ax4.set_ylabel("Total Power")
ax4.set_xticks(list(power_generation_data.keys()))
ax4.set_xticklabels(power_generation_data.keys(), fontsize=8)
ax4.yaxis.set_tick_params(color=colors[2], labelcolor=colors[2])
ax4.xaxis.set_tick_params(color=colors[2], labelcolor=colors[2])
ax4.spines['bottom'].set_color(colors[2])
ax4.spines['left'].set_color(colors[2])
ax4.title.set_color(colors[2])

# Create a window and add charts
root = tk.Tk()
root.title("Pokemon")
root.state('zoomed')

side_frame = tk.Frame(root, bg=colors[2])
side_frame.pack(side="left", fill="y")

label = tk.Label(side_frame, text="Pokemon", bg=colors[2], fg=colors[1], font=25)
label.pack(pady=50, padx=20)

charts_frame = tk.Frame(root)
charts_frame.pack()

upper_frame = tk.Frame(charts_frame)
upper_frame.pack(fill="both", expand=True)

canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

lower_frame = tk.Frame(charts_frame)
lower_frame.pack(fill="both", expand=True)

canvas3 = FigureCanvasTkAgg(fig3, lower_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
canvas4.draw()
canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

root.mainloop()
