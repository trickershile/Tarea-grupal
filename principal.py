import os
import numpy as np
import funcionesJuanita as ff
juanita=np.empty((5,7),type(object))
op=0
sw=0
while(op!=7):
    os.system("cls")
    print("    MENU DE OPCIONES ")
    print("***********************")
    print("1.- LLenar matriz")
    print("2.- Mostrar todo")
    print("3.- Mostrar específico")
    print("4.- Mayor y menor")
    print("5.- Crear archivo .csv")
    print("6.- Listar archivo .csv")
    print("7.- Salir del menú")
    op=ff.validarMenu()
    if(op==1):
        ff.llenarMatriz(juanita)
        print(juanita)
        os.system("pause")
        sw=1
    elif(op==2):
        if(sw==1):
            ff.mostrarTodo(juanita)
        else:
            print("Debe llenar primero la matriz")
            os.system("pause")
    elif(op==3):
        if(sw==1):
            ff.mostrarUno(juanita)
        else:
            print("Debe llenar antes la matriz")
            os.system("pause")
    elif(op==4):
        if(sw==1):
            ff.mayorMenor(juanita)
        else:
            print("Debe llenar antes la matriz")
            os.system("pause")
    elif(op==5):
        if(sw==1):
            ff.crearArchivo(juanita)
        else:
            print("Debe llenar antes la matriz")
            os.system("pause")
    elif(op==6):
        if(sw==1):
            ff.listarArchivo()
        else:
            print("Debe llenar antes la matriz")
            os.system("pause")
    else:
        print("Adios y gracias por susar nuestro menú")
    



    

        


