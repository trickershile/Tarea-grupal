import numpy as np
import os
import random
import csv
def validarMenu():
    while(True):
        try:
            op=int(input(" Ingrese la opcion deseada "))
            if(op>=1 and op<=7):
                break
            else:
                print("Las opciones del menú deben ser entre 1 y 7")
        except ValueError:
            print("Error, debe ser entero")
    return op
def llenarMatriz(mm):
    for i in range(5):
        for j in range(7):
            mm[i][j]=random.randint(3000,50000)
def mostrarTodo(mat):
    os.system("cls")
    p=1
    for i in range(5): #filas o carritos
          print("Carrito Numero ",p)
          for j in range(7): #columnas o dias de la semana
               print("Venta dia ",j+1, " $",mat[i][j])
          print("")
          os.system("pause")
          os.system("cls")
          p+=1
def mostrarUno(matriz):
    while(True):
        try:
            jj=int(input("Ingrese el número de carrito que desea ver "))
            if(jj>0 and jj<6):
                break
            else:
                print("El numero de carrito debe estar entre 1 y 5")
        except ValueError:
            print("Debe ingresar un número entero")
    print("Carrito Numero ",jj)
    for j in range(7):
        print("Venta dia ",j+1)
        print(matriz[jj-1][j])
    os.system("pause")
    os.system("cls")
def mayorMenor(mat):
    os.system("cls")
    mayor=0
    carrito1=0
    carrito=0
    s=1
    menor=1000000
    for i in range(5):	
          suma=0
          for j in range(7):
               suma+=mat[i][j]
          if(suma>mayor):
               mayor=suma
               carrito=s
          if(suma<menor):
               menor=suma
               carrito1=s
          s+=1
    print("Carrito ", carrito, " tiene la mayor venta con $",mayor)
    print("Carrito ", carrito1, " tiene la menor venta con $",menor)
    os.system("pause")
def crearArchivo(pp):
    with open('sopaipillas.csv','w',newline='') as file:
        es=csv.writer(file)
        es.writerow(['CarritaoNumero','TotalVenta'])#encabezado
        suma=0
        z=1
        for i in range(5):
            for j in range(7):
                suma+=pp[i][j]
            es.writerows([[z,suma],])
            z+=1
    print("Archivo creado!!!")
    os.system("pause")
def listarArchivo():
    try:
        with open('sopaipillas.csv','r',newline='')as ff:
            es=csv.reader(ff)
            for i in es:
                print(i)
    except FileExistsError:
        print("Archivo no existe, imposible mostrar")
    os.system("pause")


            

