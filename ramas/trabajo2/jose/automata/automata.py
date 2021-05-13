#AUTOMATA 2

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

	def q0(self,arr,index=0):

		if index>=len(arr):
			return False

		target = arr[index]
		if target.upper()=='A':
			return self.q0(arr,index+1)
		elif target.upper()=='I':
			return self.q0(arr,index+1)
		elif target.upper()=='D':
			return self.q0(arr, index+1)
		elif target.upper()=='T':
			return self.q1(arr,index+1)
		elif target.upper()=='S':
			return self.q8(arr, index+1)
		else:
			return False


	def q1(self,arr,index):

		if index>=len(arr):
			return False

		target = arr[index]
		if target.upper()=='A':
			return self.q2(arr, index+1)
		elif target.upper()=='I':
			return self.q1(arr, index+1)
		elif target.upper()=='D':
			return self.q1(arr, index+1)
		elif target.upper()=='T':
			return self.q8(arr, index+1)
		elif target.upper()=='S':
			return self.q8(arr, index+1)
		else:
			return False

	def q2(self,arr,index):

		if index>=len(arr):
			return False

		target = arr[index]
		if target.upper()=='A':
			return self.q2(arr, index+1)
		elif target.upper()=='I':
			return self.q2(arr, index+1)
		elif target.upper()=='D':
			return self.q2(arr, index+1)
		elif target.upper()=='T':
			return self.q3(arr, index+1)
		elif target.upper()=='S':
			return self.q7(arr, index+1)
		else:
			return False


	def q3(self,arr,index):

		if index>=len(arr):
			return False

		target = arr[index]
		if target.upper()=='A':
			return self.q4(arr, index+1)
		elif target.upper()=='I':
			return self.q3(arr, index+1)
		elif target.upper()=='D':
			return self.q3(arr, index+1)
		elif target.upper()=='T':
			return self.q8(arr, index+1)
		elif target.upper()=='S':
			return self.q8(arr, index+1)
		else:
			return False

	def q4(self,arr,index):

		if index>=len(arr):
			return False

		target = arr[index]
		if target.upper()=='A':
			return self.q4(arr,index+1)
		elif target.upper()=='I':
			return self.q4(arr, index+1)
		elif target.upper()=='D':
			return self.q4(arr, index+1)
		elif target.upper()=='T':
			return self.q8(arr, index+1)
		elif target.upper()=='S':
			return self.q5(arr, index+1)
		else:
			return False

	def q5(self,arr,index):

		if index>=len(arr):
			return False

		target = arr[index]
		if target.upper()=='A':
			return self.q6(arr, index+1)
		elif target.upper()=='I':
			return self.q5(arr, index+1)
		elif target.upper()=='D':
			return self.q5(arr, index+1)
		elif target.upper()=='T':
			return self.q8(arr, index+1)
		elif target.upper()=='S':
			return self.q8(arr, index+1)
		else:
			return False

	def q6(self,arr,index):

		if index>=len(arr):
			return False

		target = arr[index]
		if target.upper()=='A':
			return self.q6(arr, index+1)
		elif target.upper()=='I':
			return self.q6(arr, index+1)
		elif target.upper()=='D':
			return self.q6(arr, index+1)
		elif target.upper()=='T':
			return self.q8(arr, index+1)
		elif target.upper()=='S':
			return self.q7(arr, index+1)
		else:
			return False

	def q7(self,arr,index):

		if index>=len(arr):
			return True

		target = arr[index]
		if target.upper()=='A':
			return self.q7(arr, index+1)
		elif target.upper()=='I':
			return self.q7(arr, index+1)
		elif target.upper()=='D':
			return self.q7(arr, index+1)
		elif target.upper()=='T':
			return self.q8(arr, index+1)
		elif target.upper()=='S':
			return self.q8(arr, index+1)
		else:
			return False

	def q8(self,arr,index):

		if index>=len(arr):
			return False

		target = arr[index]
		if target.upper()=='A':
			return self.q8(arr, index+1)
		elif target.upper()=='I':
			return self.q8(arr, index+1)
		elif target.upper()=='D':
			return self.q8(arr, index+1)
		elif target.upper()=='T':
			return self.q8(arr, index+1)
		elif target.upper()=='S':
			return self.q8(arr, index+1)
		else:
			return False


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
		text = '\n' + str(linea) + ' (V)'
		f.write(text)
		print("Valida")
	else:
		text = '\n' + str(linea) + ' (I)'
		f.write(text)
		print("Invalida")

	f.close()
	cadena.pop(0)
	new_cadena = cadena
	return verificador_recursivo(nombre,new_cadena)



def main():
	try:
		while True:
			print('Ingrese el nombre del archivo: ', end="")
			archivo = input()

			print(f'Archivo ingresado: {archivo}, el nombre esta correcto?: s/n : ', end="")
			opc = input()
			if opc.upper()=='S':
				documento = leerArchivo(archivo)
				if documento==None:
					continues
				else:
					new_archivo = archivo
					new_archivo = new_archivo[:-4] + 'Respuesta.txt'
					verificador_recursivo(new_archivo,documento)
					print("\n[!] Archivo creado exitosamente. [!]")
					break
			else:
				continue
	except Exception as e:
		print(f'[!] ERROR: {e} [!]\n')



if __name__ == '__main__':
	main()