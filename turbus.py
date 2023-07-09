#importes

from colorama import Fore,Style,Back
import os

#listas y diccionario

asic=set()
paj={}

#textos

menu1="""Turbus
1) Asientos disponibles.
2) Comprar pasajes.
3) Cancelar pasajes.
4) Listado de pasajeros.
5) Total de ganancias.
6) Salir.
"""
error="""Error: Ingreso un dato no permitido"""

#funciones

def dis():
    os.system("cls")
    print("ASIENTOS\n")
    print(Fore.GREEN+"Disponible"+Style.RESET_ALL)
    print(Fore.RED+"Ocupado\n"+Style.RESET_ALL)
    for i in range (1,46):
        cc=str(i).zfill(2)
        if cc in asic:
            print(Fore.RED+cc+Style.RESET_ALL,end=" ")
        else:
            print(Fore.GREEN+cc+Style.RESET_ALL,end=" ")
        if i%12==0:
            print()
            if i%24==0:
                print()

def com():
    os.system("cls")
    while True:
        try:
            r=input("Digite el rut\n")
            if (len(r))>=8 and (len(r))<=9:
                if r[-2]=="-":
                    break
                else:
                    print(Fore.RED+"Error: El penultimo digito debe ser '-' "+Style.RESET_ALL)
            else:
                print(Fore.RED+"Error: El rut debe tener 7 a 8 caracteres sin contar el '-' "+Style.RESET_ALL)
        except:
            input(Fore.RED+error+Style.RESET_ALL)

    os.system("cls")
    while True:
        try:
            n=input("Digite el nombre\n")
            if (len(n))>=4:
                break
            else:
                print(Fore.RED+"Error: El nombre debe contener minimo 4 caracteres"+Style.RESET_ALL)
        except:
            input(Fore.RED+error+Style.RESET_ALL)
    
    os.system("cls")
    while True:
        try:
            ap=input("Digite el apellido\n")
            if (len(ap))>=4:
                break
            else:
                print(Fore.RED+"Error: El apellido debe contener minimo 4 caracteres"+Style.RESET_ALL)
        except:
            input(Fore.RED+error+Style.RESET_ALL)
    
    os.system("cls")
    while True:
        try:
            asi=int(input("Digite cuantos asientos desea comprar\n"))
            if asi>=1 and asi<=45:
                break
            else:
                print(Fore.RED+"Error: Solo existen 45 asientos"+Style.RESET_ALL)
        except:
            input(Fore.RED+error+Style.RESET_ALL)

    os.system("cls")
    for i in range (asi):
        cc=int(input("Digite el asiento\n"))
        if cc>=1 and cc<=45:
            cc=str(cc).zfill(2)     
            if cc in asic:
                    print(Fore.RED+"Error: El asiento no se encuentra disponible"+Style.RESET_ALL)
            else:
                print(Fore.GREEN+"El asiento fue reservado con exito"+Style.RESET_ALL)
                asic.add(cc)
                paj[cc]={'rut':r,'nombre':n,'apellido':ap,'asiento':cc}
        else:
            input(Fore.RED+"Error solo existen 45 asientos"+Style.RESET_ALL)

def can():
    os.system("cls")
    while True:
        try:
            bus=input("Digite el rut\n")
            en=False
            for b in paj.values():
                if b['rut']==bus:
                    en=True
                    break
            if en:
                os.system("cls")
                while True:
                    try:
                        de=input("Digite el nro de asiento\n")
                        de=str(de).zfill(2)
                        del paj[de]
                        print("Se cancelo el pasaje con exito")
                        break
                    except:
                        print(Fore.RED+"Error: Usted no es dueño del asiento digitado"+Style.RESET_ALL)
                break
            else:
                print(Fore.RED+"Error: rut no encontrado"+Style.RESET_ALL)
                break
        except:
            print(Fore.RED+error+Style.RESET_ALL)

def pa():
    os.system("cls")
    print("Pasajeros ")
    for v in paj.values():
        print(v)

def tot():
    os.system("cls")
    can=len(paj)
    print(f"\nTotal $: {can*8000} CLP")


#main code

while True:
    os.system("cls")
    try:
        op=int(input(menu1))
        if op==1:
            dis()
            input(Fore.GREEN+"\n\nPresione cualquier tecla para continuar\n"+Style.RESET_ALL)
        if op==2:
            com()
            input(Fore.GREEN+"Presione cualquier tecla para continuar\n"+Style.RESET_ALL)
        if op==3:
            can()
            input(Fore.GREEN+"Presione cualquier tecla para continuar\n"+Style.RESET_ALL)
        if op==4:
            pa()
            input(Fore.GREEN+"Presione cualquier tecla para continuar\n"+Style.RESET_ALL)
        if op==5:
            tot()
            input(Fore.GREEN+"Presione cualquier tecla para continuar\n"+Style.RESET_ALL)
        if op==6:
            print("Hasta luego \n")
            input(Fore.GREEN+"Presione cualquier tecla para continuar\n"+Style.RESET_ALL)
            break
    except:
        input(Fore.RED+error+Style.RESET_ALL)
tot()
