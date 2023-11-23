#importar libreria SQLite3, crar base, conexion y cursor 
import sqlite3
conn = sqlite3.connect('manejo_inventario.db')
c = conn.cursor()

try:
    c.execute("""CREATE TABLE IF NOT EXISTS productos(
              id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
              EAN INTEGER UNIQUE,
              nombre_prod TEXT NOT NULL,
              marca TEXT NOT NULL,
              descripcion_prod TEXT NOT NULL,
              cantidad INTEGER NOT NULL,
              id_proveedor INTEGER
    )""")
    input("Se creo la tabla Productos correctamente!"
          "\nPresiona ENTER para continuar"
          "\n>>>> ENTER <<<<")
except:
    print("Algo no salió bien, revisa el codigo")

conn.commit()
conn.close()