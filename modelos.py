# ESTE ARCHIVO DEFINE LAS CLASES , COMO LAS RESERVAS , HABITACION , CLIENTE CON METODOS
# PARA CARGAR , GUARDAD Y VALIDAR DATOS . 



import os
import csv

def inicializar_csv():
    archivos = {
        'datos/clientes.csv': ['id', 'nombre', 'apellido', 'dni', 'telefono', 'email'],
        'datos/habitaciones.csv': ['numero', 'tipo', 'estado', 'precio'],
        'datos/reservas.csv': ['id_reserva', 'id_cliente', 'numero_habitacion', 'fecha_entrada', 'fecha_salida', 'estado', 'total']
    }

    os.makedirs('datos', exist_ok=True)

    for ruta, encabezados in archivos.items():
        if not os.path.exists(ruta):
            with open(ruta, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=encabezados)
                writer.writeheader()
            print(f'✅ Archivo creado: {ruta}')
        else:
            print(f'✔️ Archivo ya existe: {ruta}')




RUTA_CLIENTES = 'datos/clientes.csv'   
RUTA_HABITACIONES = 'datos/habitaciones.csv'
RUTA_RESERVAS = 'datos/reservas.csv'



class Habitacion:
    def __init__(self,numero,tipo,estado,precio):
        self.numero = numero
        self.tipo = tipo 
        self.estado = estado
        self.precio = precio 
        
    def to_dict(self):
        return {
            'numero': self.numero,
            'tipo': self.tipo,
            'estado':self.estado,
            'precio':self.precio
            
            
            
        }    
def cargar_habitaciones():
    habitaciones = []
    with open(RUTA_HABITACIONES, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            habitaciones.append(Habitacion(**fila))
    return habitaciones 


def guardar_habitacion(habitacion):
    with open(RUTA_HABITACIONES, 'a' ,newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['numero','tipo','estado','precio'])
        writer.writerow(habitacion.to_dict())
        
    


    
class Cliente:
    def __init__(self, id, nombre , apellido, dni, telefono, email):
        self.id = id
        self.nombre = nombre 
        self.apellido = apellido
        self.dni = dni 
        self.telefono = telefono
        self.email = email
        
        
    def to_dict(self):
        return{
            'id':self.id,
            'nombre':self.nombre,
            'apellido':self.apellido,
            'dni':self.dni,
            'telefono':self.telefono,
            'email':self.email
            
        }    
def cargar_clientes():
    clientes = []
    with open(RUTA_CLIENTES, newline="", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            clientes.append(Cliente(**fila))
    return clientes


def guardar_cliente(cliente):
    with open(RUTA_CLIENTES, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id','nombre','apellido','dni','telefono','email'])
        writer.writerow(cliente.to_dict())
        
        
        
class Reserva:
    def __init__(self, id_reserva, id_cliente, numero_habitacion, fecha_entrada, fecha_salida, estado, total):
        self.id_reserva = id_reserva
        self.id_cliente = id_cliente
        self.numero_habitacion = numero_habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.estado = estado
        self.total = total
        
        
    def to_dict(self):
        return{
            'id_reserva': self.id_reserva,
            'id_cliente': self.id_cliente,
            'numero_habitacion': self.numero_habitacion,
            'fecha_entrada': self.fecha_entrada,
            'fecha_salida': self.fecha_salida,
            'estado': self.estado,
            'total': self.total
        }  
        
        
def cargar_reserva():
    reservas = []
    with open(RUTA_RESERVAS, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            reservas.append(Reserva(**fila))
    return reservas        

def guardar_reserva(reserva):
    with open(RUTA_RESERVAS,'a',newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=[
            'id_reserva','id_cliente','numero_habitacion',
            'fecha_entrada','fecha_salida','estado','total'])
        writer.writerow(reserva.to_dict())


            
        
        
    

            
        