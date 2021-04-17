#PRIMERA PRUEBA - PROBLEMA 2

from dotenv import load_dotenv
import os

load_dotenv()
ARCHIVO = os.getenv('NOMBRE_ARCHIVO')
ESTADO = eval(os.getenv('ESTADO_LOG'))

def printLog(arr, estado=False):
	estado = ESTADO
	if estado:
		print(f'[LOG]: {arr}')


def leerArchivo(doc):
	try:
		f = open(doc,'r')
		lineas = list(f.readlines())
		#Mandar a la 2da funcion que separe el archivo.
		f.close()
		return lineas
	except Exception as e:
		printLog(f'[!] ERROR: {e} [!]\n')


#CLASE MOVIMIENTO SE ESPECIALIZA EN LAS ACCIONES DEL ROBOT
# class Movimientos:

# 	def __init__(self):
# 		self.T = 'T' #TOMAR
# 		self.T = 'S' #SOLTAR
# 		self.T = 'A' #AVANZAR
# 		self.T = 'D' #GIRAR DERECHA
# 		self.T = 'I' #GIRAR IZQUIERDA

# 	def valido(self,accion):
# 		pass


class Robot:

	def __init__(self):
		self.__arr = list()
		#self.mov = Movimientos()
		pass

	def verificarInvalido(self,arr):
		'''Si tomo, 2 opciones: volver a tomar o solar
		Si toma, tiene que soltar 2 veces
		Si suelta, no puede volver a tomar o soltar. '''
		verifcando = list(arr)
		combinacion = list()
		indice = list()
		printLog(verifcando)
		#CONDICION 1: NINGUN ELEMENTO.
		if 'T' not in verifcando and 'S' not in verifcando:
			printLog('Valido\n')
			return False
		contador = 0

		for i in verifcando:
			if i == 'T' or i == 'S':
				combinacion.append(i)
				indice.append(contador)

			contador+=1

		printLog(combinacion)
		printLog(indice)

		#CONDICION 2:
		#pillar la 1ra T y verificar si el siguiente que encuentra es una T o un S
		pass


	def recursivo(self,nombre,arr):
		nombre_archivo = nombre
		cadena = list(arr)
		printLog(f'Lista: {cadena}')
		printLog(f'Largo: {len(cadena)}')

		if len(cadena)<1:
			return True

		#COMPROBAR SI ES INVALIDO O NO
		linea = cadena[0]
		linea = linea[:-1]
		printLog(f'Linea revisada: {linea}')

		f = open(nombre_archivo, 'a')

		if self.verificarInvalido(linea):
			text = '\n' + str(linea) + ' (I)'
			f.write(text)
		else:
			text = '\n' + str(linea) + ' (V)'
			f.write(text)



		f.close()
		cadena.pop(0)
		new_cadena = cadena
		return self.recursivo(nombre_archivo,new_cadena)

		#
		pass

	def escritura(self, nombre, arr):
		nombre_archivo = nombre
		nombre_archivo = nombre_archivo[:-4] + 'Respuesta.txt'
		cadena = arr

		if self.recursivo(nombre_archivo,cadena):
			printLog('Termine.')

		pass

	def Iniciar(self):
		self.__nombre = ARCHIVO
		self.__arr = leerArchivo(ARCHIVO)
		self.escritura(self.__nombre,self.__arr)

		pass


def main():
	mr_robot = Robot()
	mr_robot.Iniciar()


if __name__ == '__main__':
	main()