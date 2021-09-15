import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

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

	def circle(r,a,b):
		n = int(input("Введите число точек "))
		self.x = np.linspace(-2*r,2*r,n)
		self.y = np.linspace(-2*r,2*r,n)
		X,Y = np.meshgrid(x, y)
		fxy= (X-a)**2 + (Y-b)**2
		plt.contour(X, Y, fxy, levels=[0])
		plt.show()

	def collusion():
		while x != x0 and y != y0:
			draw()

	def draw():
		fig, ax = plt.subplots()
		anim_object, = plt.plot([], [], '-', lw = 2)
		xdata, ydata = [], []
		ani = FuncAnimation(fig, update, frames = np.arange(0, 5, 0.1), interval = 10)
		plt.axis('equal')
		ax.set_xlim(-5, 5)
		ax.set_ylim(-5, 5)
		ani.save('lab_7_3.gif')

	def update(frames):
		anim_object.set_data(circle(frames)[0], circle(frames)[1])
		return anim_object,

lab8()


