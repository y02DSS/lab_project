import numpy as np
import matplotlib.pyplot as plt

class lab8():
	def __init__(self):
		super().__init__()
		self.k()

	def k(self):
		x = np.linspace(-5, 5, 100)
		y = (x - 2)*(x + 2)
		fig, ax = plt.subplots()
		ax.hlines(0, -5, 5, linewidth = 5)
		ax.hlines(10, -5, 10, linewidth = 5)
		ax.hlines(-10, -10, 15, linewidth = 5)
		ax.vlines(10, -5, 10, linewidth = 5)
		ax.vlines(-15, -15, 15, linewidth = 5)
		edge = 25
		plt.axis('equal')
		ax.set_xlim(-edge, edge)
		ax.set_ylim(-edge, edge)

		plt.show()

lab8()