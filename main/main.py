import os
import sys
sys.path.append(r"C:\Users\ermes\OneDrive\Documentos\LENGUAJES DE PROGRAMACION\SESION_9\ConexionBD\ConexiónBD")
from dao import daoConnection
from models import clases as c

os.system('cls')

conex = daoConnection.Connection("localhost", "root", "", "dbregisters")
conex.connect()

def insertarciudad():
    name = input("Ingrese el Nombre de la Ciudad")
    ciudad = c.City(name, 1, any)
    daoCity = daoConnection.DaoCity(conex)
    #insertar 
    daoCity.insert(ciudad)

def MostrarCiudad():
    
    daoCity = daoConnection.DaoCity(conex)

    cities = daoCity.get_all()
    for City in cities :
        print(City)

def EliminarCiudad():
    NameEliminar = input("Elija el ID de la Ciudad que deseas Eliminar")
    daoCity = daoConnection.DaoCity(conex)
    daoCity.delete(NameEliminar)

def buscarCiudad():
    idBuscarCiudad = input("Elije el ID de la ciudad que deseas buscar ")
    daoCity = daoConnection.DaoCity(conex)
    cities = daoCity.get_by_id(idBuscarCiudad)
    print(cities)

def editarCiudad():
    os.system("cls")
    MostrarCiudad()
    id_sec = int(input("Que id deseas actualizar"))
    name_new = input("Nuevo nombre : ")
    status_new = input("Nuevo status : ")
    daoCity = daoConnection.DaoCity(conex)
    ciudad = c.City(name_new,status_new, id_sec)
    daoCity.update(ciudad)

def menu():
    print("1. Ingresa la Ciudad")
    print("2. Mostrar Ciudad")
    print("3. Eliminar Ciudad")
    print("4. Editar Ciudad")
    print("5. Buscar Ciudad")
    print("6. Salir")

def main():
    opcion = 0
    while(opcion != 6):
        menu()
        opcion = int(input("Ingrese tu Opcion"))
        if(opcion == 1):
            insertarciudad()
            os.system("pause")
        elif(opcion == 2):
            MostrarCiudad()
            os.system("pause")
        elif(opcion == 3):
            EliminarCiudad()
            os.system("pause")
        elif(opcion == 4):
            editarCiudad()
            os.system("pause")
        elif(opcion == 5):
            buscarCiudad()
            os.system("pause")
        


main()


















# def insertarCiudad()
# nombre = input("INGRESA EL NOMBRE")
# city = c.City(nombre,1)

# city1 = c.City(nombre, 1)


# daoCity = daoConnection.DaoCity(conex)

# cities = daoCity.get_all()
# for city in cities:
#     print(city)


# def menu():
#     print("1. AGREGAR UNA CIUDAD")
#     print("2. EDITAR CIUDAD")
#     print("3. MOSTRAR CIUDAD")
#     print("4. ACTUALIZAR CIUDAD")
#     print("5. ELIMINAR CIUDAD")
#     print("6. SALIR")


    

#instanciar modelo

# city2 = c.City("León", 1)
# city3 = c.City("Granada", 1)
# city4 = c.City("Masaya", 1)
# city5 = c.City("Estelí", 1)
# city6 = c.City("Jinotepe", 1)

# #instanciar dao

# #insertar
# daoCity.insert(city1)
# daoCity.insert(city2)
# daoCity.insert(city3)
# daoCity.insert(city4)
# daoCity.insert(city5)
# daoCity.insert(city6)



# #Instaciar modelo
# Job1 = c.Job("Ingeniero de Software",1)
# Job2 = c.Job("Medico",2)
# Job3 = c.Job("Profesor",3)
# Job4 = c.Job("Abogado",4)
# Job5 = c.Job("Contador",5)
# Job6 = c.Job("Chef",6)

# #Instaciar dao
# daoJob = daoConnection.DaoJob(conex)
# #Insertar
# daoJob.insert(Job1)
# daoJob.insert(Job2)
# daoJob.insert(Job3)
# daoJob.insert(Job4)
# daoJob.insert(Job5)
# daoJob.insert(Job6)

# Jobs = daoJob.get_all()
# for jobsj in Jobs:
#     print(jobsj)

# #instanciar modelo
# Employee1 = c.Employee("Juan Garcia",21,8,"10000",1)
# Employee2 = c.Employee("Maria Lopez",22,9,"5000",1)
# Employee3 = c.Employee("Pablo Martinez",23,10,"2000",1)
# Employee4 = c.Employee("Carlos Perez",24,11,"6000",1)
# Employee5 = c.Employee("Jose Torres",25,12,"6000",1)
# Employee6 = c.Employee("Patricia Ruiz",26,13,"7000",1)
# #Instanciar dao
# daoEmployee = daoConnection.DaoEmployee(conex)
# #Insertar
# daoEmployee.insert(Employee1)
# daoEmployee.insert(Employee2)
# daoEmployee.insert(Employee3)
# daoEmployee.insert(Employee4)
# daoEmployee.insert(Employee5)
# daoEmployee.insert(Employee6)
# #consultar

# Employees = daoEmployee.get_all()
# for employees in Employees:
#     print(employees)
