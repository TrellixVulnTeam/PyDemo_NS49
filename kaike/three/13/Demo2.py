import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def sinplot():
	x = np.linspace(0, 15, 100)
	for i in range(1, 3):
		plt.plot(x, np.sin(x + i))
sns.set()
sinplot()
plt.show()