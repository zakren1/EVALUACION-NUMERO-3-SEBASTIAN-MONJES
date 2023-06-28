import os
os.system ("cls")

listatipo = ['PAQUETE','PAQUETE','SOBRE','PAQUETE','SOBRE']
listanombre = ['SEBASTIAN','MATIAS','SEBASTIAN','JORGE','JORGE']
listarut = ['12345678-9','98765432-1','12345678-9','11111111-1','11111111-1']
listapeso = [3,5,0.7,30,2]
listaprecio = [4000,8000,2000,30000,3000]
listaciudad = ['CONCEPCION','SANTIAGO','CONCEPCION','PTO MONTT','PTO MONTT']

menu = '''
    MENU
 1-. GRABAR
 2-. BUSCAR
 3-. LISTAR
 4-. SALIR
 Digite opcion: '''

def grabar():
    while True:
        try:
            tipo = input("Ingrese el tipo de encomienda (SOBRE/PAQUETE): ")
            if tipo == 'SOBRE' or tipo == 'PAQUETE':
                listatipo.append(tipo)
                break
            else:
                print("Error. Solo se puede ingresar (SOBRE/PAQUETE)")

        except:
            print("Excepcion en tipo")
#end while tipo
    while True:
        try:
            nombre = input("Ingrese el nombre del destinatario: ")
            if len(nombre) >= 2 and len(nombre) <= 30:
                listanombre.append(nombre)
                break
            else:
                print("El nombre del destinatario debe tener entre 2 y 30 caracteres")
        except:
            print("Excepcion en nombre")
#end while nombre
    while True:
        try:
            rut = input("Ingrese el rut del destinatario: ")
            if len(rut) >= 9 and rut[-2] == '-':
                listarut.append(rut)
                break
            else:
                print("El rut debe tener minimo 9 caracteres y un guion (-) en el penultimo caracter")
        except:
            print("Excepcion en rut")
#end while rut
    while True:
        try:
            precio = int(input("Ingrese el precio: "))
            if precio >= 2000:
                listaprecio.append(precio)
                break
            else:
                print("Error. El precio minimo es 2000")
        except:
            print("Excepcion en precio")
#end while precio
    while True:
        try:
            peso = float(input("Ingrese el peso: "))
            if peso >= 0.1:
                listapeso.append(peso)
                break
            else:
                print("Error. El peso minimo es 0.1")
        except:
            print("Excepcion en peso")
#end while peso
    while True:
        try:
            ciudad = input("Ingrese la ciudad: ")
            if len(ciudad) >= 3:
                listaciudad.append(ciudad)
                break
            else:
                print("Error. La ciudad debe tener minimo 3 caracteres,")
        except:
            print("Excepcion en ciudad")
#end while ciudad

def buscar():
    rut = input("RUT A BUSCAR: ")
    print(" LISTADO POR RUT \n")
    print("N°|   TIPO    |   NOMBRE DESTINATARIO          | RUT          |     PRECIO     |   PESO(kg)| CIUDAD                         |")
    print("--+-----------+--------------------------------+--------------+----------------+-----------+--------------------------------|")
    for i in range(len(listatipo)):
         if rut.lower() == listarut[i].lower():
            print(f"{i+1} | {listatipo[i]:9s} | {listanombre[i]:30s} | {listarut[i]:12s} | {listaprecio[i]:14d} | {listapeso[i]:4f} | {listaciudad[i]:30s}")
            print("--+-----------+--------------------------------+--------------+----------------+-----------+--------------------------------|")


def listar():
    totalpaquetes = 0
    totalsobre = 0
    print("       LISTADO DE ENCOMIENDAS\n    ")
    print("N°|   TIPO    |   NOMBRE DESTINATARIO          | RUT          |     PRECIO     |   PESO(kg)| CIUDAD                         |")
    print("--+-----------+--------------------------------+--------------+----------------+-----------+--------------------------------|")
    for i in range(len(listatipo)):
        if listatipo[i] == 'SOBRE':
            totalsobre = totalsobre + 1
        elif listatipo[i] == 'PAQUETE':
            totalpaquetes = totalpaquetes + 1

        print(f"{i+1} | {listatipo[i]:9s} | {listanombre[i]:30s} | {listarut[i]:12s} | {listaprecio[i]:14d} | {listapeso[i]:4f} | {listaciudad[i]:30s}")
        print("--+-----------+--------------------------------+--------------+----------------+-----------+--------------------------------|")
    print(f"Total sobres = {totalsobre}")
    print(f"Total paquetes = {totalpaquetes}")

#MAIN
while True:
    try:
        opc = int(input(menu))
        if opc == 4:
            print("Nombre: Sebastian Monjes")
            print("Version del programa")
            break
        elif opc == 1:
            grabar()
        elif opc == 2:
            buscar()
        elif opc == 3:
            listar()
        else:
            print("Opcion incorrecta")
    except:
        print("Excepcion en menu")
