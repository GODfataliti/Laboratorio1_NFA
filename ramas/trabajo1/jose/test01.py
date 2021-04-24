#PRIMERA PRUEBA - PROBLEMA 1

from dotenv import load_dotenv
import os
import time

load_dotenv()
#GLOBAL VAR
ARCHIVO = os.getenv('NOMBRE_ARCHIVO')
ESTADO = eval(os.getenv('ESTADO_LOG'))
PRINT_ESTADO = eval(os.getenv('PRINT_ESTADO'))

def printLog(arr, error=False):
	estado_print = PRINT_ESTADO
	error = error
	green='\033[92m'
	warning='\033[93m'
	endc='\033[0m'
	if estado_print:
		print(f"{green}[LOG {time.strftime('%b %Y %H:%M:%S')}] {endc}: {arr}")
	elif error:
		print(f"{warning}[LOG {time.strftime('%b %Y %H:%M:%S')}] {endc}: {arr}")
	else:
		print(f"{green}[LOG {time.strftime('%b %Y %H:%M:%S')}] {endc}: {arr}")

class Binario:

	def __init__(self):
		self.archivo = ARCHIVO
		self.archivo_estado = True
		pass

	def verificaCorrupto(self,arr):

		cadena = arr
		largo1 = '1111' #Minimo 4 -> C
		largo0 = '000' #Minimo 3 -> C

		if largo1 in cadena or largo0 in cadena:
			if PRINT_ESTADO:
					printLog('Corrupto\n')
			return True
		else:
			if PRINT_ESTADO:
					printLog('Limpio\n')
			return False

	def recursivo(self,nombre,arr):

		nombre_archivo = nombre
		cadena = list(arr)
		if ESTADO:
			printLog(f'Lista: {cadena}')
			printLog(f'Largo: {len(cadena)}')
		if len(cadena)<1:
			return True

		f = open(nombre_archivo, 'a')

		linea = cadena[0]
		linea = linea[:-1]
		if ESTADO:
			printLog(f'Linea revisada: {linea}\n')

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
					printLog('Limpio\n',)
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
			printLog('\x1b[6;30;42m' + 'Termine.' + '\x1b[0m')

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
			printLog(f'[!] ERROR AL LEER: {e} [!]\n', True)


	def Iniciar(self,doc=ARCHIVO):
		while self.archivo_estado:
			printLog('Ingrese el nombre del archivo:')
			documento = input()
			printLog(f'Archivo ingresado: {documento}')
			printLog(f'Realizar codificacion: S/N')
			opc = input()
			if opc.upper()=='S':
				self.leerArchivo(documento)
				self.archivo_estado=False


def main():
	binario = Binario()
	binario.Iniciar()



if __name__ == '__main__':
	main()