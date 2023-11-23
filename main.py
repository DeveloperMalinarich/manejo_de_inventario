#importar libreria SQLite3, crar base, conexion y cursor 
import sqlite3
conn = sqlite3.connect('manejo_inventario.db')
c = conn.cursor()

def menu_principal():
    while True:
        opcion = int(input("** BIENVENIDO AL SISTEMA DE CONTROL DE STOCK **"
                        "\nPara comenzar, por favor selecciona una de las opciones"
                        "\n1. Ver lista de productos en stock"
                        "\n2. Agregar un nuevo producto al inventario"
                        "\n3. Actualizar un producto"
                        "\n4. Buscar un producto"
                        "\n5. Salir del programa"
                        "\n6. Acerca de SISTEMA DE GESTION DE STOCK"
                        "\n>>>  "))
        if opcion == 1:
            ver_productos()
            break        

        elif opcion == 2:
            agrear_producto()
            break
        
        elif opcion == 3:
            modificar_cantidad()
            break

        elif opcion == 4:
            buscar_producto()
            break
        
        elif opcion == 5:
            input("Muchas gracias por utilizar nuestro sistema de stock"
                  "\nPresiona Enter para terminar. >>> ENTER <<<<")
            break

        elif opcion == 6:
            muestra_info()
            break

        else:
            opcion_inex = int(input("Por favor ingresa una opcion valida"
                        "\n1. Ver lista de productos en stock"
                        "\n2. Agregar un nuevo producto al inventario"
                        "\n3. Actualizar un producto"
                        "\n4. Buscar un producto"
                        "\n5. Salir del programa"
                        "\n6. INFO SISTEMA DE GESTION DE STOCK"
                        "\n>>>  "))
            print(opcion_inex)
            continue

    
#definir funcion "VER STOCK"
def ver_productos():
    #realizo consulta a la base
    c.execute("SELECT * FROM productos")

    #almaceno los resultados en la variable "resultados"
    resultados = c.fetchall()
    
    #imprimo resultados
    print(resultados)

    #solicito eleccion al usuario
    submenu_1 = int(input("Seleccioná una opcion: "
                                    "\n1. Volver a mostrar listado"
                                    "\n2. Salir del programa"
                                    "\n3. Volver al menu inicial"
                                    "\n>>>"))

    while True:
        
        #si elije 1
        if submenu_1 == 1:
                        ver_productos()

        #si elije 2    
        elif submenu_1 == 2:
            print("Gracias por utilizar nuestro sistema !"
            "\nHasta la proxima!")
            break

        
        #si elije 3    
        elif submenu_1 == 3:
            menu_principal()
                 
        #si elije cualquier otra opcion                        
        else:
            submenu_1 = int(input("Por favor ingresa una opcion valida: "
                                        "\n1. Volver a mostrar listado"
                                        "\n2. Salir del programa"
                                        "\n3. Volver al menu inicial"
                                        "\n>>>"))
            continue
        break
        
        
            
            


#definir funcion "AGREGAR AL STOCK"
def agrear_producto():
    
    #solicito datos

    EAN = int(input("Ingresá el EAN: \n >>>"))
    nombre = input("Ingresá el nombre del producto: \n >>>")
    marca = input("Ingresá la marca del producto: \n >>>")
    descripcion = input("Ingresá la descripcion del producto: \n >>>")
    cantidad = int(input("Ingresá la cantidad en stock: \n >>>"))
    id_proveedor = int(input("Ingresá el ID de proveedor: \n >>>"))

    
    #almaceno los datos en la variable datos_producto
    datos_producto=(None,EAN,nombre,marca,descripcion,cantidad,id_proveedor)
    
    try:
    #realizo la consulta de insercion de datos en 
        c.execute("INSERT INTO productos VALUES(?,?,?,?,?,?,?)", datos_producto)
        conn.commit()
    except:
        print("No se cargo el producto, por favor vericá los datos")
    
    print("Se cargó el producto correctamente!")

    #solicito eleccion al usuario
    submenu_1 = int(input("Seleccioná una opcion: "
                                    "\n1. Cargar otro producto"
                                    "\n2. Salir del programa"
                                    "\n3. Volver al menu inicial"
                                    "\n>>>"))

    while True:
        
        #si elije 1
        if submenu_1 == 1:
                        agrear_producto()

        #si elije 2    
        elif submenu_1 == 2:
            print("Gracias por utilizar nuestro sistema !"
            "\nHasta la proxima!")
            break

        #si elije 3    
        elif submenu_1 == 3:
            menu_principal()
                 
        #si elije cualquier otra opcion                        
        else:
            submenu_1 = int(input("Por favor ingresa una opcion valida: "
                                    "\n1. Cargar otro producto"
                                    "\n2. Salir del programa"
                                    "\n3. Volver al menu inicial"
                                    "\n>>>"))
            continue



#defino funcion para modificar cantidad en stock
def modificar_cantidad():

    #solicito EAN y CANTIDAD NUEVA al usuario
    producto = int(input("Por favor ingrese el codigo EAN del producto: "))
    nueva_cantidad = int(input("Por favor ingresa la cantidad disponible en stock: "))
    
    #realizo consulta SQL
    try:
        c.execute("UPDATE productos SET cantidad = ? WHERE EAN = ? ", (nueva_cantidad, producto))
        conn.commit()
    except:
        print("No se modificó el stock, revisá el codigo")
    
    
    #Imprimo confirmacion y re-menu
    print("Se modifico correctamente la cantidad en stock, ahora la cantidad es: ", nueva_cantidad)

    submenu_1 = int(input("Seleccioná una opcion: "
                                    "\n1. Modificar cantidad de otro producto"
                                    "\n2. Salir del programa"
                                    "\n3. Volver al menu inicial"
                                    "\n>>>"))
    while True:
        
        #si elije 1
        if submenu_1 == 1:
                        modificar_cantidad()

        #si elije 2    
        elif submenu_1 == 2:
            print("Gracias por utilizar nuestro sistema !"
            "\nHasta la proxima!")
            break

        #si elije 3    
        elif submenu_1 == 3:
            menu_principal()
                 
        #si elije cualquier otra opcion                        
        else:
            submenu_1 = int(input("Por favor ingresa una opcion valida: "
                                    "\n1. Cargar otro producto"
                                    "\n2. Salir del programa"
                                    "\n3. Volver al menu inicial"
                                    "\n>>>"))
            continue


#defino funcion para buscar producto:
def buscar_producto():
    producto = int(input("Ingresá el numero de EAN y prioná Enter: "
                    "\n>>> "))
    
    #ejecutar consulta
    c.execute("SELECT * FROM productos WHERE EAN = ?", (producto,))
    resultado = c.fetchone()

    if resultado:
         print(resultado)
    if not resultado:
         print("El EAN es no existe")

    #solicito eleccion al usuario
    submenu_1 = int(input("Seleccioná una opcion: "
                                    "\n1. buscar otro producto"
                                    "\n2. Salir del programa"
                                    "\n3. Volver al menu inicial"
                                    "\n>>>"))

    while True:
      
        #si elije 1
        if submenu_1 == 1:
                        buscar_producto()

        #si elije 2    
        elif submenu_1 == 2:
            print("Gracias por utilizar nuestro sistema !"
            "\nHasta la proxima!")
            break

        #si elije 3    
        elif submenu_1 == 3:
            menu_principal()
                 
        #si elije cualquier otra opcion                        
        else:
            submenu_1 = int(input("Por favor ingresa una opcion valida: "
                                    "\n1. Buscar otro producto"
                                    "\n2. Salir del programa"
                                    "\n3. Volver al menu inicial"
                                    "\n>>>"))
            continue

    return resultado


#defino funcion MUESTRA INFO

def muestra_info():
    print("Sistema de Manejo de Inventario Base de Datos: Utiliza SQLite para almacenar" 
          "la información del inventario." 
          "\nLa base de datos debe tener al menos una tabla para almacenar los productos" 
          " con campos como nombre, 6\ncódigo, cantidad en stock y precio."
    
            "Menú Principal:" 
            "\nImplementa un menú principal que permita al usuario realizar" 
            "diversas acciones, como:"
            "\nVer lista de productos en stock"
            "\nAgregar un nuevo producto al inventario."
            "\nActualizar la cantidad de un producto."
            "\nBuscar un producto por su código."
            "\nSalir del programa."
            
            "\n \nOperaciones:"
            "\nA) Ver lista de productos: Muestra todos los productos en stock con sus detalles."
            "\nB) Agregar nuevo producto: Permite al usuario ingresar la información de un nuevo producto y lo añade" 
            "\na la base de datos."
            "\nC) Actualizar cantidad: Permite al usuario aumentar o disminuir la cantidad en stock de un producto existente."
            "\nD) Buscar producto por código: Busca un producto por su código y muestra sus detalles.")

    #solicito eleccion al usuario
    submenu_1 = int(input("Seleccioná una opcion: "
                                    "\n1. volver a mostrar la info"
                                    "\n2. Salir del programa"
                                    "\n3. Volver al menu inicial"
                                    "\n>>>"))

    while True:
        
        #si elije 1
        if submenu_1 == 1:
                        muestra_info()

        #si elije 2    
        elif submenu_1 == 2:
            print("Gracias por utilizar nuestro sistema !"
            "\nHasta la proxima!")
            break

        #si elije 3    
        elif submenu_1 == 3:
            menu_principal()
                 
        #si elije cualquier otra opcion                        
        else:
            submenu_1 = int(input("Por favor ingresa una opcion valida: "
                                    "\n1. Buscar otro producto"
                                    "\n2. Salir del programa"
                                    "\n3. Volver al menu inicial"
                                    "\n>>>"))
            continue

menu_principal()
