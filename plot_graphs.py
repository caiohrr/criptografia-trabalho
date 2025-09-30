import matplotlib.pyplot as plt
import numpy as np

labels = ['Carta - São José de Anchieta', 'Categories - Aristotle', 'The Republic - Plato']
# fib_cifra = [0.005274, 0.026209, 0.309004]
# aes_cifra = [0.003669, 0.005245, 0.006711]


fib_decifra = [0.005283, 0.024466, 0.296683]
aes_decifra = [0.003536, 0.003246, 0.005493]


x = np.arange(len(labels))  # positions for comparisons
width = 0.35  # bar width

fig, ax = plt.subplots(figsize=(10, 6)) 
bars1 = ax.bar(x - width/2, fib_decifra, width, label='Fib Decifra')
bars2 = ax.bar(x + width/2, aes_decifra, width, label='AES Decifra')

ax.set_ylabel('Tempo (s)')
ax.set_title('Comparação de decifras')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=15, ha='right')  
ax.legend()

# Mostrar os valores em cima das barras
ax.bar_label(bars1, fmt="%.6f", padding=3)
ax.bar_label(bars2, fmt="%.6f", padding=3)

plt.tight_layout()
plt.show()
