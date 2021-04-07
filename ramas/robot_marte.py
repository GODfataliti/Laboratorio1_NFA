
#ROBOT MARTE



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





