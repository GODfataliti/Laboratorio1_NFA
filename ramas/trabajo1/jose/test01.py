#PRIMERA PRUEBA

from dotenv import load_dotenv
import os


load_dotenv()
#GLOBAL VAR
ARCHIVO = os.getenv('NOMBRE_ARCHIVO')

def verificaCorrupto(arr):
	contador1 = 0
	contador0 = 0

	cadena = arr



	if contador1>=4 or contador0>=3:
		return True
	else:
		return False 


def recursivo(nombre,arr):

	nombre_archivo = nombre
	cadena = arr
	if len(cadena)<1:
		return True

	linea = cadena[0]
	linea = linea[:-1]

	if linea[-3:] == '101':
		new_cadena = linea[:-3]

		if verificaCorrupto(linea):
			f = open(nombre_archivo, 'a')
			text = linea + ' (C)'
			f.write(text)
		else:
			f = open(nombre_archivo, 'a')
			text = linea + ' (L)'
			f.write(text)

	else:
		



	#tomar la cadena - DONE
	#verificar si la cadena tiene elementos - DONE
	#verificar primera linea - DONE
	#decidir si esta bien o no:
	#escribir una nueva linea en el archivo sol con la primera linea de la cadena.
	#eliminarla de la lista (la primera linea)
	#volver a llamar la funcion con la nueva cadena
	pass




def verificadorCadena(nombre,arr):

	nombre_archivo = nombre
	nombre_archivo = nombre_archivo[:-4] + 'Respuesta.txt'
	cadena = arr

	if recursivo(nombre_archivo,cadena):
		print("Termine.")



def leerArchivo(doc):
	try:
		f = open(doc,'r')
		lineas = f.readlines()
		print(lineas)
		#Mandar a la 2da funcion que separe el archivo.
		verificadorCadena(doc,lineas)
		f.close()
	except Exception as e:
		print(f'[!] ERROR: {e} [!]\n')


def main():
	leerArchivo(ARCHIVO)



if __name__ == '__main__':
	main()