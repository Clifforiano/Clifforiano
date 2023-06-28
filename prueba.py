tipo=[]
nom=[]
rut=[]
peso=[]
precio=[]
ciudad=[]
error="Error: Ingreso un dato erroneo"
menu1="""Seleccione el tipo de paquete
1) Sobre
2) Paquete"""

menu2="""Menu de Caracol Express
1) Grabar encomiendas
2) Buscar encomiendas
3) Listar encomiendas
4) Salir
"""

def grabar():
    while True:
        try:
            n=input("Ingrese el nombre del destinatario\n")
            if len(n)>=2 and len(n)<=30:
                n=n.upper()
                nom.append(n)
                break
            else:
                print("Error: El nombre debe tener de 2 a 30 caracteres")
        except:
            print(error)

    while True:
        try:
            r=input("Ingrese el rut del destinatario\n")
            if r[-2]=="-":
                r=r.upper()
                rut.append(r)
                break
            else:
                print("Error: El rut debe tener un - como penultimo caracter")
        except:
            print(error)
    
    while True:
        try:
            t=int(input(f"{menu1}\n"))
            if t==1:
                tipo.append("SOBRE")
                break
            elif t==2:
                tipo.append("PAQUETE")
                break
            else:
                print("Error: solo existen 2 opciones")
        except:
            print(error)
    
    while True:
        try:
            p=float(input("Ingrese el peso del paquete\n"))
            if p>=0.1:
                peso.append(p)
                break
            else:
                print("Error: El peso minimo es de 0.1 kg")
        except:
            print(error)

    while True:
        try:
            pre=int(input("Ingrese el precio del paquete\n"))
            if pre>=2000:
                precio.append(pre)
                break
            else:
                print("Error: El precio minimo es de $2000 pesos")
        except:
            print(error)

    while True:
        try:
            c=input("Ingrese la ciudad de direccion del paquete\n")
            if len(c)>=3:
                c=c.upper()
                ciudad.append(c)
                break
            else:
                print("Error: Las ciudades deben tener minimo 3 caracteres")
        except:
            print(error)
    

def busca():
        try:
            bus=input("Ingrese el rut para buscar una encomienda\n")
            encontrado=False
            print("El rut tiene registrada las siguientes encomiendas:")
            for i in range (len(rut)):
                if bus==rut[i]:
                    print(f"{i+1}) {tipo[i]}")
                    encontrado=True    
            if not encontrado:
                            print("No existen encomiendas al respectivo rut")
        except:
            print(error)
                    
            
def listar():
    for a in range (len(rut)):
        print("Listado de encomiendas")
        print(f"{a+1}) {nom[a]} {rut[a]} {tipo[a]} {peso[a]} {precio[a]} {ciudad[a]}")
    c=0
    c1=0
    for l in range(len(tipo)):
        if tipo[l]=="SOBRE":
            c=c+1
        elif tipo[l]=="PAQUETE":
            c1=c1+1
    print(f"El total de sobres es: {c}")
    print(f"El total de paquetes es: {c1}")    
        


while True:
    try:
        op=int(input(menu2))
        if op==1:
            grabar()
        elif op==2:
            busca()
        elif op==3:
            listar()
        elif op==4:
            print("Adios")
            print("Cliffer Ramirez 0.1 alpha")
            break
        else:
            print("Error: Este menu solo tiene 4 opciones")
    except:
        print(error)


