import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import sympy

class lab8():
	def __init__(self):
		super().__init__()
		self.x = []
		self.y = []
		self.k()

	def k(self):
		x3 = np.linspace(-5, 5, 300)
		y3 = x3**2/4-10
		y1 = np.linspace(-3, 10, 300)
		x1 = y1 - 5
		y2 = np.linspace(-3, 10, 300)
		x2 = -y1 + 20
		for i, j in zip(x1, y1):
			self.x.append(i)
			self.y.append(j)
		for i, j in zip(x2, y2):
			self.x.append(i)
			self.y.append(j)
		for i, j in zip(x3, y3):
			self.x.append(i)
			self.y.append(j)
		fig, ax = plt.subplots()
		edge = 25
		plt.axis('equal')
		ax.set_xlim(-edge, edge)
		ax.set_ylim(-edge, edge)
		plt.plot(x3, y3)
		plt.plot(x1, y1)
		plt.plot(x2, y2)
		return collusion(self.x, self.y)

	def circle(r,a,b):
		n = int(input("Введите число точек "))
		self.x = np.linspace(-2*r,2*r,n)
		self.y = np.linspace(-2*r,2*r,n)
		X,Y = np.meshgrid(x, y)
		fxy= (X-a)**2 + (Y-b)**2
		plt.contour(X, Y, fxy, levels=[0])
		plt.show()

	def collusion():
		while x != edge and y != edge:
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


