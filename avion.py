

#### //variables contadores y matrices \\
x="x"
xn="x "
i=0

avion =([[1,2,3,4,5,6] , [7,8,9,10,11,12], [13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36],[37,38,39,40,41,42]])
avion1 =([[1,2,3,4,5,6] , [7,8,9,10,11,12], [13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36],[37,38,39,40,41,42]])

asientos_ocupados=[]
cliente=[]
clientes=[]

###### ///funciones\\



def avion_():
    print("|   ",avion[0][0],"",avion[0][1],"",avion[0][2],"   ",avion[0][3],"",avion[0][4],"",avion[0][5],"   |\n|   ",avion[1][0],"",avion[1][1],"",avion[1][2],"  ",avion[1][3],avion[1][4],avion[1][5],"   |")
    print("|   ",avion[2][0],avion[2][1],avion[2][2]," ",avion[2][3],avion[2][4],avion[2][5],"   |")
    print("|   ",avion[3][0],avion[3][1],avion[3][2]," ",avion[3][3],avion[3][4],avion[3][5],"   |")
    print("|   ",avion[4][0],avion[4][1],avion[4][2]," ",avion[4][3],avion[4][4],avion[4][5],"   |")
    print("|___________     ___________|")
    print("|___________     ___________|")
    print("|   ",avion[5][0],avion[5][1],avion[5][2]," ",avion[5][3],avion[5][4],avion[5][5],"   |")
    print("|   ",avion[6][0],avion[6][1],avion[6][2]," ",avion[6][3],avion[6][4],avion[6][5],"   |")


def cobrar():
    print("")
    avion_()
    print ("\n","estos son nuestros asientos disponibles")
    asiento = int(input("ingrese el asiento que le interesa comprar: "))
    asientos_ocupados.append(asiento)
    cliente.append(asiento)
    clientes.append(cliente)
    banco = int(input("usted es socio de banco-duoc?)\n1)si.\2)no"))

    if banco==1:
        print("a obtenido un descuento del 15%")
        if asiento<=30:
            print("el precio del asiento seleccionado es de: $67.065")
        if asiento>30:
            print("el valor del asiento seleccionado es de $204.000")

    if banco==2:
        print("no es beneficiario de descuentos")
        if asiento<=30:
            print("el precio del asiento seleccionado es de: $78.900")
        if asiento>30:
            print("el valor del asiento seleccionado es de $240.000")
    
def pedir_datos():
    
    print("antes de comprar el voleto igrese los siguientes datos:\n")
    nombre = input("ingrese su nombre: ")
    cliente.append(nombre)
    rut = int(input("ingrese su rut : "))
    cliente.append(rut)
    telefono = int(input("ingrese su telefono: "))
    cliente.append(telefono)
   
  



    

def saludo():
    print("\n\nBienvenido a vuelos-Duoc\ningrese el numero de la opcion que desea \n")

def opcion1():
    print("a elegido la opcion Ver asientos disponibles. ")
   # print (avion)
    avion_()

def opcion2():
    print("a elegido la opcion Comprar voleto.")
    pedir_datos()
    cobrar()
    print(cliente,"\n\n")

    
#####
    for i in range(0, 7):
        for j in range(0, 6):
                for l in range(0, len(asientos_ocupados)):

                        if  avion1[i][j]==asientos_ocupados[l] and avion1[i][j]>=10:
                            avion[i][j]=xn
                        if  avion1[i][j]==asientos_ocupados[l] and avion1[i][j]<10:
                            avion[i][j]=x

def opcion3():
    p=1
    while p==1:
        not_asiento = int(input("ingrese el asiento del voleto que  desea cancelar o un 0 para salir: "))
        if not_asiento==0:
            p=p+1
        else:
            if not_asiento in asientos_ocupados:
                
                for i in range(0, 7):
                 for j in range(0, 6):
                  for l in range(0, len(asientos_ocupados)):

                        if  avion1[i][j]==not_asiento:
                            avion[i][j]=not_asiento
                asientos_ocupados.remove(not_asiento)
                
                
                print("su pasaje a sido cancelado.")
                p=2

                
            else:print("asiento no registrado")
  

def opcion4():
    p=1
    while p==1:
        vasiento = int(input("ingrese el numero de su asiento : "))
        if vasiento in cliente:
            print("")
            p="1"
        else:
            print("asiento no registrado ")
    p=1
    while p==1:
        vrut = int(input("ingrese su rut : "))
        if vrut in cliente:
            print("")
            p="1"
        else:
            print("rut no coincide ")
    print("que informacion dessea modificar?\n1)nombre\n2)telefono")
    mod = int(input())
    if mod==1:
        vnombre = input("ingrese el nombre que desea cambiar : ")
        nnombre = input("ingrese el nuevo nombre : ")
        for l in range(0, len(cliente)):
                        if  cliente[l]==vnombre:
                            cliente[l]=nnombre
        
    if mod==2:
        vnumero = int(input("ingrese el numero de telefono que desea cambiar : "))
        nnumero = int(input("ingrese el nuevo numero de telefono : "))
        for l in range(0, len(cliente)):
                        if  cliente[l]==vnumero:
                            cliente[l]=nnumero

def opcion5():
    print("a elegido la opcion Salir.")


##############//main\\

saludo()
while i<1:
    print("\n")
    print("1)Ver asientos disponibles.\n2)Comprar asiento.\n3)Anular vuelo. \n4)Modificar datos de pasajero.\n5) Salir.\n\n")
    opcion = int(input("ingrese el numero de la opcion elegida : "))
    if(opcion>0 and opcion <7):
            if opcion==1:
                opcion1()
            if opcion==2:
                opcion2()
            if opcion==3:
                opcion3()
            if opcion==4:
                opcion4()
            if opcion==5:
                opcion5()
                i=i+1
    else:print("opcion no valida")
    
    
print("fin del programa")