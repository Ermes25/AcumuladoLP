import os
import sys
sys.path.append(r"C:\Users\ermes\OneDrive\Documentos\LENGUAJES DE PROGRAMACION\SESION_9\ConexionBD\ConexiónBD")
from dao import daoConnection
from models import clases as c

os.system('cls')

conex = daoConnection.Connection("localhost", "root", "", "dbregisters")
conex.connect()


#INGRESO DE LAS CONSULTAS DE LA DATABASE DE CITY

#INSERT CITY 
def insertarciudad():
    os.system("cls")
    name = input("Ingrese el Nombre de la Ciudad")
    ciudad = c.City(name, 1, any)
    daoCity = daoConnection.DaoCity(conex)
    #insertar 
    daoCity.insert(ciudad)

#SHOW EVERY CITY
def MostrarCiudad():
    os.system("cls")
    daoCity = daoConnection.DaoCity(conex)
    cities = daoCity.get_all()
    for City in cities :
        print(City)
#DELETE CITY
def EliminarCiudad():
    os.system("cls")
    NameEliminar = input("Elija el ID de la Ciudad que deseas Eliminar")
    daoCity = daoConnection.DaoCity(conex)
    daoCity.delete(NameEliminar)
#SEARCH CITY
def buscarCiudad():
    os.system("cls")
    idBuscarCiudad = input("Elije el ID de la ciudad que deseas buscar ")
    daoCity = daoConnection.DaoCity(conex)
    cities = daoCity.get_by_id(idBuscarCiudad)
    print(cities)
#EDITH CITY
def editarCiudad():
    os.system("cls")
    MostrarCiudad()
    id_sec = int(input("Que id deseas actualizar"))
    name_new = input("Nuevo nombre : ")
    status_new = input("Nuevo status : ")
    daoCity = daoConnection.DaoCity(conex)
    ciudad = c.City(name_new,status_new, id_sec)
    daoCity.update(ciudad)
#MENU CITY
def menuCiudad():
    print("1. Ingresa la Ciudad")
    print("2. Mostrar Ciudad")
    print("3. Eliminar Ciudad")
    print("4. Editar Ciudad")
    print("5. Buscar Ciudad")
    print("6. Salir")
#MAIN ONLY CITY
def main_ciudad():
    opcion_ciudad = 0
    while(opcion_ciudad != 6):
        menuCiudad()
        opcion_ciudad = int(input("Ingresa tu opcion"))
        if(opcion_ciudad == 1):
            insertarciudad()
            os.system("pause")
        elif(opcion_ciudad == 2):
            MostrarCiudad()
            os.system("pause")
        elif(opcion_ciudad == 3):
            EliminarCiudad()
            os.system("pause")
        elif(opcion_ciudad == 4):
            editarCiudad()
            os.system("pause")
        elif(opcion_ciudad == 5):
            buscarCiudad()
            os.system("pause")

#METODO DE CONSULTAS DE JOB EN LA DATABASE
# INSERT JOB 
def InsertarJob():
    name_job = input("Ingrese el Nombre del Trabajo")
    trabajo = c.Job(name_job,1,any)
    daoJob = daoConnection.DaoJob(conex)
    daoJob.insert(trabajo)
#SHOW EVERY JOBS
def MostrarJob():
    daoJob = daoConnection.DaoJob(conex)
    Jobs = daoJob.get_all()
    for jobsj in Jobs:
        print(jobsj)
#DELETE JOB
def EliminarJob():
    NameJobEliminar = input("Ingresa el ID del Trabajo que desea Eliminar :  ")
    daoJob = daoConnection.DaoJob(conex)
    daoJob.delete(NameJobEliminar)
#SEARCH JOB
def buscarJob():
    idBuscarJob = input("Elija el id del trabajo que desea buscar : ")
    daoJob = daoConnection.DaoJob(conex)
    jobs = daoJob.get_by_id(idBuscarJob)
    print(jobs)
#EDITH JOB
def editarJob():
    os.system("cls")
    MostrarJob()
    id_job_sec = int(input("Que id deseas actualizar : "))
    name_new_job = input("Nuevo trabajo :  ")
    status_new = input("Nuevo status : ")
    daoJob = daoConnection.DaoJob(conex)
    trabajo = c.Job(name_new_job,status_new,id_job_sec)
    daoJob.update(trabajo)
#MENU ONLY JOB
def menujobs():
    print("1. Ingresar Trabajo")
    print("2. Mostrar Trabajo")
    print("3. Eliminar Trabajo")
    print("4. Editar Trabajo")
    print("5. Buscar")
    print("6. Salir")

def main_Jobs():
    opcion_Job = 0
    while(opcion_Job !=6):
        menujobs()
        opcion_Job = int(input("Ingresa tu Opcion"))
        if(opcion_Job == 1):
            InsertarJob()
            os.system("pause")
        if(opcion_Job == 2):
            MostrarJob()
            os.system("pause")
        if(opcion_Job == 3):
            EliminarJob()
            os.system("pause")
        if(opcion_Job == 4):
            editarJob()
            os.system("pause")
        if(opcion_Job == 5):
            buscarJob()
            os.system("pause")
#INSERT EMPLOYEES
def insertarEmployees():
    os.system("cls")
    name_employee = input("Ingresa el Nombre del Empleado : ")
    os.system("cls")
    idciudad= MostrarCiudad()
    idciudad = int(input("Elige un id de Ciudad para el empleado : "))
    os.system("cls")
    idJob= MostrarJob()
    idJob = int(input("Elige un id de trabajo para el Empleado : "))
    salario = int(input("Ingresa el Salario del empleado : "))
    
    empleado = c.Employee(name_employee,idciudad,idJob,salario,1,any)
    daoEmployee = daoConnection.DaoEmployee(conex)
    daoEmployee.insert(empleado)
#SHOW EVERY EMPLOYEES
def mostrarEmpleado():
    daoEmployee = daoConnection.DaoEmployee(conex)
    Employee = daoEmployee.get_all()
    for employees in Employee:
        print(employees)
#DELETE EMPLOYEE
def EliminarEmployee():
    os.system("cls")
    ned = input("Ingresa el id del Empleado que desea Eliminar : ")
    daoEmployee = daoConnection.DaoEmployee(conex)
    daoEmployee.delete(ned)
#SEARCH EMPLOYEE
def buscarEmployee():
    os.system("cls")
    id_employee_search = input("Elija el id que desea buscar : ")
    daoEmployee = daoConnection.DaoEmployee(conex)
    Employee = daoEmployee.get_by_id(id_employee_search)
    print(Employee)
#EDITH EMPLOYEES
def editarEmployee():
    os.system("cls")
    mostrarEmpleado()
    ieo = int(input("Que id desea actualizar : "))
    n_new_employee = input("nuevo empleado : ")
    os.system("cls")
    n_new_idCiudad = MostrarCiudad()
    n_new_idCiudad = input("nuevo id de ciudad para el empleado : ")
    os.system("cls")
    n_new_idJob = MostrarJob()
    n_new_idJob = input("nuevo id de trabajo para el Empleado : ")
    os.system("cls")
    status_new = input("nuevo status : ")
    new_salario = int(input("Nuevo salario : "))
    daoEmployee = daoConnection.DaoEmployee(conex)
    employee = c.Employee(n_new_employee,n_new_idCiudad,n_new_idJob,status_new,new_salario,ieo)
    daoEmployee.update(employee)
#MENU EMPLOYEE
def menuEmpleado():
    print("1. Ingresar Empleados")
    print("2. Mostrar Empleados")
    print("3. Eliminar Empleado")
    print("4. Editar Empleado")
    print("5. Buscar")
    print("6. Salir")
#MAIN EMPLOYEE
def main_Employees():
    opcion_Employees = 0
    while(opcion_Employees != 6):
        menuEmpleado()
        opcion_Employees = int(input("Ingresa tu Opcion"))
        if(opcion_Employees ==1):
            insertarEmployees()
            os.system("pause")
        if(opcion_Employees ==2):
            mostrarEmpleado()
            os.system("pause")
        if(opcion_Employees == 3):
            EliminarEmployee()
            os.system("pause")
        if(opcion_Employees == 4):
            editarEmployee()
            os.system("pause")
        if(opcion_Employees == 5):
            buscarEmployee()
            os.system("pause")
#PROPER MAIN WHO CALLs EVERY MAIN THAT WE USE IN THE DATABASE
def main():
    opcion_menu = 0
    while(opcion_menu != 3):
        print("1. MENU CIUDAD")
        print("2. MENU JOBS")
        print("3. MENU EMPLOYEES")
        opcion_menu = int(input("ELIGE UN MENU : "))
        if(opcion_menu == 1):
            main_ciudad()
            os.system("pause")
        if(opcion_menu == 2):
            main_Jobs()
            os.system("pause")
        if(opcion_menu == 3):
            main_Employees()
            os.system("pause")
        else:
            print("Esa Opcion no existe en el programa")

main()