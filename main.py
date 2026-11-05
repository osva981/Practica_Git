print("SISTEMA DE REGISTRO DE ESTUDIANTES")
print("1. Registrar estudiante")
print("2. Consultar estudiantes")
print("3. promedio de calificaciones ")
print("3. Salir")

estudiantes = []
def registrar_estudiante(nombre):
 estudiantes.append(nombre)
 print("Estudiante registrado:", nombre)
registrar_estudiante("Juan Pérez")
registrar_estudiante("María López")


print("Lista de estudiantes:")
for estudiante in estudiantes:
 print(estudiante)

def  consultar_estudiantes():
 print("ESTUDIANTES REGISTRADOS")
 for estudiante in estudiantes:
 print(estudiante)

def promedio_de_calificaciones():
    print("estudiantes registrados")
    for estudiante in estudiantes:
    print(estudiante)
 
