#PRIMERA PRUEBA - PROBLEMA 1

from dotenv import load_dotenv
import os

load_dotenv()
#GLOBAL VAR
ARCHIVO = os.getenv('NOMBRE_ARCHIVO')
ESTADO = eval(os.getenv('ESTADO_LOG'))

def printLog(arr, estado=False):
	estado = ESTADO
	if estado:
		print(f'[LOG]: {arr}')



class Binario:

	def __init__(self):
		self.archivo = ARCHIVO
		pass

	def verificaCorrupto(self,arr):

		cadena = arr
		largo1 = '1111' #Minimo 4 -> C
		largo0 = '000' #Minimo 3 -> C

		if largo1 in cadena or largo0 in cadena:
			printLog('Corrupto\n')
			return True
		else:
			printLog('Limpio\n')
			return False


	def recursivo(self,nombre,arr):

		nombre_archivo = nombre
		cadena = list(arr)
		printLog(f'Lista: {cadena}')
		printLog(f'Largo: {len(cadena)}')
		if len(cadena)<1:
			return True

		f = open(nombre_archivo, 'a')

		linea = cadena[0]
		linea = linea[:-1]
		printLog(f'Linea revisada: {linea}')

		if linea[-3:] == '101':

			if self.verificaCorrupto(linea):
				text = '\n' + str(linea) + ' (C)'
				f.write(text)
			else:
				text = '\n' + str(linea) + ' (L)'
				f.write(text)

		else:
			text = '\n' + str(linea) + ' (L)'
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
			printLog('Termine.')


	def leerArchivo(self,doc):
		try:
			f = open(doc,'r')
			lineas = list(f.readlines())
			#Mandar a la 2da funcion que separe el archivo.
			self.verificadorCadena(doc,lineas)
			f.close()
		except Exception as e:
			printLog(f'[!] ERROR: {e} [!]\n')



	def Iniciar(self,doc):
		self.leerArchivo(doc)



def main():
	binario = Binario()
	binario.Iniciar(ARCHIVO)



if __name__ == '__main__':
	main()