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
	print("Verificando...")


	if contador1>=4 or contador0>=3:
		return True
	else:
		return False


def recursivo(nombre,arr):

	nombre_archivo = nombre
	cadena = list(arr)
	print(f'Lista: {cadena} \nLargo: {len(cadena)}')
	if len(cadena)<1:
		return True

	f = open(nombre_archivo, 'a')

	linea = cadena[0]
	linea = linea[:-1]
	print(f'Linea revisada: {linea}')

	if linea[-3:] == '101':

		if verificaCorrupto(linea):
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
	print(f'Cadena Enviada: {new_cadena}\n')
	return recursivo(nombre_archivo,new_cadena)




	#tomar la cadena - DONE
	#verificar si la cadena tiene elementos - DONE
	#verificar primera linea - DONE
	#decidir si esta bien o no: C o L
	#escribir una nueva linea en el archivo sol con la primera linea de la cadena.
	#eliminarla de la lista (la primera linea) - DONE
	#volver a llamar la funcion con la nueva cadena - DONE
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
		lineas = list(f.readlines())
		#Mandar a la 2da funcion que separe el archivo.
		verificadorCadena(doc,lineas)
		f.close()
	except Exception as e:
		print(f'[!] ERROR: {e} [!]\n')


def main():
	leerArchivo(ARCHIVO)



if __name__ == '__main__':
	main()