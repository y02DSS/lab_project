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
		self.k()

	def k(self):
		x3 = np.linspace(-5, 5, 50)
		y3 = x3**2/4-10
		y1 = np.linspace(-3, 10, 50)
		x1 = y1 - 5
		y2 = np.linspace(-3, 10, 50)
		x2 = -y1 + 20
		for i, j in zip(x1, y1):
			self.x.append(round(i,1))
			self.y.append(round(j,1))
		for i, j in zip(x2, y2):
			self.x.append(round(i,1))
			self.y.append(round(j,1))
		for i, j in zip(x3, y3):
			self.x.append(round(i,1))
			self.y.append(round(j,1))
		plt.axis('equal')
		ax.set_xlim(-self.edge, self.edge)
		ax.set_ylim(-self.edge, self.edge)
		plt.plot(x3, y3)
		plt.plot(x1, y1)
		plt.plot(x2, y2)
		return self.krug(self.x, self.y)


	def krug(self, x0, y0):
		c = 0
		exitFlag=False
		anim_object, = plt.plot([], [], '-', lw=2)

		def update(frame, x0, y0, c, exitFlag):
			theta = np.linspace(0, 2 * np.pi, 50)
			xdata = (frame*np.cos(theta))
			ydata = (frame*np.sin(theta))
			if c == 0:
				for i, j in zip(x0, y0):
					for h in range(len(theta)):
						#print(round(xdata[h],1), round(ydata[h],1), '   ',i,j)
						if round(xdata[h],1) == i and round(ydata[h],1) == j:
							c = 1
							exitFlag=True
							break
					if exitFlag:
						break
			anim_object.set_data(xdata[:50], ydata[:50])

			
			return anim_object,

		ani = FuncAnimation(fig,
							update,
							frames=np.arange(0, 6, 0.1),
							interval=10,
							fargs = (x0, y0, c, exitFlag,),
							blit=True)
		plt.show()
		ani.save('lab7_2_b.gif')


fig, ax = plt.subplots()
lab8()






'''
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
		anim_object, = plt.plot([], [], '-', lw = 2)
		fig, ax = plt.subplots()
		anim_object, = plt.plot([], [], '-', lw = 2)
		xdata, ydata = [], []
		ani = FuncAnimation(fig, self.update, frames = np.arange(0, 5, 0.1), interval = 10)
		plt.axis('equal')
		ax.set_xlim(-5, 5)
		ax.set_ylim(-5, 5)
		ani.save('lab_7_3.gif')

	def update1(self, frames):
		self.anim_object.set_data(self.circle(frames)[0], circle(frames)[1])
		return anim_object,
'''




