#PRIMERA PRUEBA - PROBLEMA 1

from dotenv import load_dotenv
import os
import time

load_dotenv()
#GLOBAL VAR
ARCHIVO = os.getenv('NOMBRE_ARCHIVO')
ESTADO = eval(os.getenv('ESTADO_LOG'))
PRINT_ESTADO = eval(os.getenv('PRINT_ESTADO'))


class printsLog:

	def __init__(self):
		self.estado_print = PRINT_ESTADO
		self.__green = '\033[92m'
		self.__warning = '\033[91m'
		self.__endc = '\033[0m'

	def printLog(self,arr, error=False):
		estado_print = PRINT_ESTADO
		error = error

		if estado_print:
			print(self.__green + f"[LOG {time.strftime('%b %d %Y %H:%M:%S')}]: {arr}" + self.__endc)
		elif error:
			print(self.__warning+  f"[LOG {time.strftime('%b %d %Y %H:%M:%S')}]: {arr}"+ self.__endc)
		else:
			print(self.__green+ f"[LOG {time.strftime('%b %d %Y %H:%M:%S')}]: {arr}"+ self.__endc)

class Binario:

	def __init__(self):
		self.archivo = ARCHIVO
		self.archivo_estado = True
		self.__log = printsLog()
		pass

	def verificaCorrupto(self,arr):

		cadena = arr
		largo1 = '1111' #Minimo 4 -> C
		largo0 = '000' #Minimo 3 -> C

		if largo1 in cadena or largo0 in cadena:
			if PRINT_ESTADO:
				self.__log.printLog('Corrupto\n')
			return True
		else:
			if PRINT_ESTADO:
				self.__log.printLog('Limpio\n')
			return False

	def recursivo(self,nombre,arr):

		nombre_archivo = nombre
		cadena = list(arr)
		if ESTADO:
			self.__log.printLog(f'Lista: {cadena}')
			self.__log.printLog(f'Largo: {len(cadena)}')
		if len(cadena)<1:
			return True

		f = open(nombre_archivo, 'a')

		linea = cadena[0]
		linea = linea[:-1]
		if ESTADO:
			self.__log.printLog(f'Linea revisada: {linea}\n')

		if linea[-3:] == '101':

			if self.verificaCorrupto(linea):
				text = '\n' + str(linea) + ' (C)'
				f.write(text)
			else:
				text = '\n' + str(linea) + ' (L)'
				f.write(text)

		else:
			text = '\n' + str(linea) + ' (L)'
			if PRINT_ESTADO:
				self.__log.printLog('Limpio\n',)
			f.write(text)

		f.close()
		cadena.pop(0)
		new_cadena = cadena
		return self.recursivo(nombre_archivo,new_cadena)

		#tomar la cadena - DONE
		#verificar si la cadena tiene elementos - DONE
		#verificar primera linea - DONE
		#decidir si esta bien o no: C o L
		#escribir una nueva linea en el archivo sol con la primera linea de la cadena.
		#eliminarla de la lista (la primera linea) - DONE
		#volver a llamar la funcion con la nueva cadena - DONE
		pass


	def verificadorCadena(self,nombre,arr):

		nombre_archivo = nombre
		nombre_archivo = nombre_archivo[:-4] + 'Respuesta.txt'
		cadena = arr

		if self.recursivo(nombre_archivo,cadena):
			self.__log.printLog('Termine.')

	def leerArchivo(self,doc):
		try:
			f = open(doc,'r')
			lineas = list(f.readlines())
			if ESTADO:
				printLog(f'{lineas}\n')
			#Mandar a la 2da funcion que separe el archivo.
			self.verificadorCadena(doc,lineas)
			f.close()
		except Exception as e:
			self.__log.printLog(f'[!] ERROR AL LEER: {e} [!]\n', True)


	def Iniciar(self,doc=ARCHIVO):
		while self.archivo_estado:
			self.__log.printLog('Ingrese el nombre del archivo:')
			documento = input()
			self.__log.printLog(f'Archivo ingresado: {documento}')
			self.__log.printLog(f'Realizar codificacion: S/N')
			opc = input()
			if opc.upper()=='S':
				self.leerArchivo(documento)
				self.archivo_estado=False


def main():
	binario = Binario()
	binario.Iniciar()



if __name__ == '__main__':
	main()