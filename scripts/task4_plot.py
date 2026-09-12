import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 200)
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), '--', label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin(x) and cos(x)')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('task4_figure.png', dpi=150, bbox_inches='tight')
