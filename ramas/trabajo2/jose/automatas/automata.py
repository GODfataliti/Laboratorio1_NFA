#AUTOMATA 1

def leerArchivo(doc):
	try:
		f = open(doc,'r')
		lineas = list(f.readlines())
		#Mandar a la 2da funcion que separe el archivo.
		f.close()
		return lineas
	except Exception as e:
		print(f'[!] ERROR: {e} [!]\n')


class AutomataDFA:

	#ESTADO INICIAL
	def q0(self,arr,index=0):

		if index>=len(arr):
			return False

		target = arr[index]
		if target=='1':
			return self.q1(arr,index+1)
		elif target=='0':
			return self.q5(arr,index+1)
		else:
			return False


	def q1(self,arr,index):

		if index>=len(arr):
			return False

		target = arr[index]
		if target=='1':
			return self.q2(arr,index+1)
		elif target=='0':
			return self.q5(arr,index+1)
		else:
			return False

	def q2(self,arr,index):

		if index>=len(arr):
			return False

		target = arr[index]
		if target=='1':
			return self.q3(arr,index+1)
		elif target=='0':
			return self.q5(arr,index+1)
		else:
			return False


	def q3(self,arr,index):

		if index>=len(arr):
			return False

		target = arr[index]
		if target=='1':
			return self.q4(arr,index+1)
		elif target=='0':
			return self.q5(arr,index+1)
		else:
			return False


	def q4(self,arr,index):

		if index>=len(arr):
			return False

		target = arr[index]
		if target=='1':
			return self.q4(arr,index+1)
		elif target=='0':
			return self.q8(arr,index+1)
		else:
			return False


	def q5(self,arr,index):

		if index>=len(arr):
			return False

		target = arr[index]
		if target=='1':
			return self.q1(arr,index+1)
		elif target=='0':
			return self.q6(arr, index+1)
		else:
			return False


	def q6(self,arr,index):

		if index>=len(arr):
			return False

		target = arr[index]
		if target=='1':
			return self.q1(arr, index+1)
		elif target=='0':
			return self.q7(arr, index+1)
		else:
			return False


	def q7(self,arr,index):

		if index>=len(arr):
			return False

		target = arr[index]
		if target=='1':
			return self.q4(arr, index+1)
		elif target=='0':
			return self.q7(arr,index+1)
		else:
			return False


	def q8(self,arr,index):

		if index>=len(arr):
			return False

		target = arr[index]
		if target=='1':
			return self.q9(arr, index+1)
		elif target=='0':
			return self.q4(arr, index+1)
		else:
			return False


	#ESTADO FINAL
	def q9(self,arr,index):
		
		if index>=len(arr):
			return True

		target = arr[index]
		if target=='1':
			return self.q4(arr, index+1)
		elif target=='0':
			return self.q8(arr, index+1)
		else:
			return False

#True Corrupto
#False Limpio

#VARIABLE GLOBAL
automata = AutomataDFA()

def verificador_recursivo(doc,arr):
	nombre = doc
	cadena = list(arr)

	if len(cadena)<1:
		return True

	f = open(nombre, 'a')

	linea = cadena[0]
	linea = linea[:-1]

	if automata.q0(linea):
		text = '\n' + str(linea) + ' (C)'
		f.write(text)
		print("Corrupto")
	else:
		text = '\n' + str(linea) + ' (L)'
		f.write(text)
		print("Limpio")

	f.close()
	cadena.pop(0)
	new_cadena = cadena
	return verificador_recursivo(nombre,new_cadena)



def main():
	
	while True:
		print('Ingrese el nombre del archivo: ', end="")
		archivo = input()

		print(f'Archivo ingresado: {archivo}, el nombre esta correcto?: s/n : ', end="")
		opc = input()
		if opc.upper()=='S':
			documento = leerArchivo(archivo)
			new_archivo = archivo
			new_archivo = new_archivo[:-4] + 'Respuesta.txt'
			verificador_recursivo(new_archivo,documento)
			print("\n[!] Termine. [!]")
			break
		else:
			continue


if __name__ == '__main__':
	main()