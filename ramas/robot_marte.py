
#ROBOT MARTE

from numpy import random


class Movimientos:

	def __init__(self):
		self.W = 'W'
		self.N = 'N'
		self.S = 'S'
		self.E = 'E'

	def mover(self,arr, path):

		if path == self.W:
			arr+=self.W
		elif path == self.N:
			arr+=self.N
		elif path == self.S:
			arr+=self.S
		elif path == self.E:
			arr+=self.E



class Robot:

	def __init__(self):
		self.arr = []
		self.mov = Movimientos()


	def avanzar(self,path):
		return self.mov.mover(self.arr,path)

	def obtenerArr(self):
		return "".join(self.arr)




prueba = Robot()
print(prueba.obtenerArr())

def identificarRepetido(arr,word):
	print("...Example...")

cont = 0
while cont<=10:

	randomN = random.randint(1,5)
	if randomN == 1:
		prueba.avanzar('W')
		#identificarRepetido(prueba.obtenerArr(),'W')
	elif randomN == 2:
		prueba.avanzar('E')
		#identificarRepetido(prueba.obtenerArr(),'W')
	elif randomN == 3:
		prueba.avanzar('S')
		#identificarRepetido(prueba.obtenerArr(),'W')
	elif randomN == 4:
		prueba.avanzar('N')
		#identificarRepetido(prueba.obtenerArr(),'W')

	cont+=1

print(prueba.obtenerArr())


