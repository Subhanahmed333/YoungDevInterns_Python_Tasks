import matplotlib.pyplot as plt
import numpy as np

# Create x values from 0 to 4π (two complete cycles)
x = np.linspace(0, 4*np.pi, 1000)

# Calculate sine and cosine values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the plot
plt.figure(figsize=(12, 8))

# Plot sine wave
plt.plot(x, y_sin, 'b-', linewidth=2, label='sin(x)')

# Plot cosine wave
plt.plot(x, y_cos, 'r-', linewidth=2, label='cos(x)')

# Customize the plot
plt.title('Sine and Cosine Functions', fontsize=16, fontweight='bold')
plt.xlabel('x (radians)', fontsize=12)
plt.ylabel('y', fontsize=12)

# Set x-axis ticks at important points (π, 2π, 3π, 4π)
x_ticks = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi, 5*np.pi/2, 3*np.pi, 7*np.pi/2, 4*np.pi]
x_labels = ['0', 'π/2', 'π', '3π/2', '2π', '5π/2', '3π', '7π/2', '4π']
plt.xticks(x_ticks, x_labels)

# Set y-axis limits and ticks
plt.ylim(-1.5, 1.5)
plt.yticks([-1, -0.5, 0, 0.5, 1])

# Add horizontal line at y=0
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)

# Add vertical lines at key x values
for tick in x_ticks:
    plt.axvline(x=tick, color='k', linestyle='--', alpha=0.2)

# Add grid
plt.grid(True, alpha=0.3)

# Add legend
plt.legend(loc='upper right', fontsize=12)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Display the plot
plt.show()

# Optional: Save the plot
plt.savefig('sine_cosine_graph.png', dpi=300, bbox_inches='tight')

print("Graph successfully generated!")
print("Key observations:")
print("- Sine starts at 0, Cosine starts at 1")
print("- Both functions oscillate between -1 and 1")
print("- Sine and Cosine are 90° (π/2 radians) out of phase")
print("- Both have a period of 2π radians")
