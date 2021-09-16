import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import sympy

class lab8():
	def __init__(self):
		super().__init__()
		self.x = []
		self.y = []
		self.edge = 25
		global fig
		global ax
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
		plt.axis('equal')
		ax.set_xlim(-self.edge, self.edge)
		ax.set_ylim(-self.edge, self.edge)
		plt.plot(x3, y3)
		plt.plot(x1, y1)
		plt.plot(x2, y2)

		return self.krug(self.x, self.y)


	

	def krug(self, x0, y0):
		fig, ax = plt.subplots()
		anim_object, = plt.plot([], [], '-', lw=2)
		xdata, ydata = [], []

	def update(self):
		print(1)
		theta = np.linspace(0, 2 * np.pi, 100)
		xdata = (frame*np.cos(theta)) 
		ydata = (frame*np.sin(theta))
		for i, j in zip(x0, y0):
			if xdata == i or xdata == j:
				print('прик')
		anim_object.set_data(xdata, ydata)
		return anim_object,

		ani = FuncAnimation(fig,
							self.update,
							frames=np.arange(0, 4, 0.1), 

							interval=10,
							blit=True)
		ani.save('add/lab7_2_b.gif')






	def circle(self):
		end = []
		n = int(input("Введите число точек "))
		r = np.linspace(0, self.edge, 100)
		xc = np.linspace(-2*r,2*r,n)
		yc = np.linspace(-2*r,2*r,n)
		end.append(xc)
		end.append(yc)
		return end

	def collusion(self, x, y):
		while self.circle()[0] != x and self.circle()[1] != y:
			for i,j in zip(x,y):
				if self.circle()[0] == i and self.circle()[1] == j:
					self.a = i
					self.b = j

	def draw(self):
		self.anim_object, = plt.plot([], [], '-', lw = 2)
		fig, ax = plt.subplots()
		anim_object, = plt.plot([], [], '-', lw = 2)
		xdata, ydata = [], []
		ani = FuncAnimation(fig, self.update, frames = np.arange(0, 5, 0.1), interval = 10)
		plt.axis('equal')
		ax.set_xlim(-5, 5)
		ax.set_ylim(-5, 5)
		ani.save('lab_7_3.gif')

	def update(self, frames):
		self.anim_object.set_data(self.circle(frames)[0], circle(frames)[1])
		return anim_object,

lab8()


