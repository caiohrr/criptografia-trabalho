import matplotlib.pyplot as plt
import numpy as np

# Example data (3 comparisons, 2 values each)
labels = ['Comparison 1', 'Comparison 2', 'Comparison 3']
group1 = [10, 15, 7]   # Values for first set
group2 = [12, 9, 11]   # Values for second set

x = np.arange(len(labels))  # positions for comparisons
width = 0.35  # bar width

fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, group1, width, label='Group 1')
bars2 = ax.bar(x + width/2, group2, width, label='Group 2')

# Labels and title
ax.set_ylabel('Values')
ax.set_title('Bar Chart with 3 Comparisons')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Auto scale is default, but we can ensure layout fits
plt.tight_layout()
plt.show()
