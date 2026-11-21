import matplotlib.pyplot as plt
import numpy as np

# Prepare some data
# X-axis: 30 evenly spaced points between 0 and 10
x = np.linspace(0, 10, 30)
y1 = np.sin(x)
y2 = np.cos(x)

# 1. Basic Plotting
# 1.1 Line plot
plt.plot(x, y1)

# 1.2 Scatter plot
plt.scatter(x, y1)

# 1.3 Bar chart (Note: x should be discrete categories, taking a few random points here)
plt.bar([1, 2, 3, 4, 5], [10, 20, 15, 30, 25])

# 2. Advanced Plot Styling (passing arguments directly in plot)
# color: line color (e.g., black, blue, '#FF5753')
# linestyle: line style ('-', '--', '-.', ':')
# linewidth: line thickness
# marker: marker style ('o' circle, '*' star, 's' square)
# label: legend name
plt.plot(x, y1, color="black", linestyle="--", linewidth=2, marker="o", label="Sin Line")
plt.plot(x, y2, color="blue", linestyle=":", label="Cos Line")

# 3. Chart Modifications (Title, Axes, Legend, Grid)
# Chart title
plt.title("Trigonometric Functions")
# X-axis label
plt.xlabel("X Axis (0 to 10)")
# Y-axis label
plt.ylabel("Y Axis")

# Show legend (loc sets position, e.g., 'upper left', 'best')
plt.legend(loc="upper right")
# Add grid lines, alpha sets transparency
plt.grid(alpha=0.3, linestyle="--")

# Set axis limits (optional)
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)  # Fixed: changed upper limit from -1.5 to 1.5

# 4. Save and Display
# Save image (must be before plt.show(), otherwise it saves a blank canvas)
plt.savefig("my_plot.png", dpi=300)

# Show chart (will pop up a window if running in a terminal)
plt.show()


# 5. Create Subplots (drawing multiple small charts in one figure)
# fig is the entire canvas, axes is an array containing subplot objects
# 1 row, 2 columns
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4)) # Fixed: changed nrow to nrows
axes[0].plot(x, y1, color='green')
axes[0].set_title("Sin")
axes[1].plot(x, y2, color='purple')
axes[1].set_title("Cos")
# Overall figure title
fig.suptitle("Two Subplots")
plt.show()
