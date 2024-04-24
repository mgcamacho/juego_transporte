from random import randint, choice, random

class Jugador:
    '''El jugador'''
    def __init__(self, 
                 nombre: str):
        self.nombre = nombre
        self.dinero = 500
        self.ubicacion = 'Hogar'
    
    def elegir_tranporte(self):
        elecciones = ['Transporte empresarial',
                      'Uber',
                      'Urbvan']
    
class Tiempo:
    '''Hora y fecha'''
    def __init__(self):
        self.hora_inicial = '6:00'
        self.hora = self.hora_inicial
    
    def __repr__(self) -> str:
        return f'Hora actual: {self.hora}'

class Conductor:
    '''Conductor de vehículo y de transporte.'''
    def __init__(self,
                 nombre: str,
                 estilo: str = 'Tranquilo',
                 edad: int = 27):
        self.nombre = nombre
        self.estilo = estilo
        self.edad = edad
    
    def __repr__(self) -> str:
        return f'Conductor: {self.nombre}. Estilo {self.estilo}'
        
    def conducir(self):
        pass

class Vehiculo:
    '''Vehículo que se desplaza por la ciudad'''
    def __init__(self,
                 modelo: str,
                 velocidad: range,
                 conductor: Conductor):
        self.modelo = modelo
        self.velocidad = velocidad
        self.conductor = conductor

class Transporte(Vehiculo):
    '''Transporte empresarial que lleva empleados a sus trabajos'''
    def __init__(self,
                 tipo: str,
                 horario_salida: int,
                 conductor: Conductor,
                 costo: int = 0):
        self.tipo = tipo
        self.costo = costo
        self.horario_salida = horario_salida
        self.conductor = conductor
    
    def __repr__(self) -> str:
        return f'Tipo: {self.tipo}. Costo: {self.costo}. Horario: {self.horario_salida}. Maneja: {self.conductor}'

class Clima:
    '''Condiciones meteorológicas'''
    def __init__(self,
                 condicion_actual: str,
                 lluvia: bool = False):
        self.condiciones = ['soleado', 'nublado', 'lluvioso', 'tormentoso', 'aguanieve']
        self.condicion_actual = choice(self.condiciones)
        self.lluvia = self.condicion_actual == 'lluvioso' or self.condicion_actual == 'tormentoso'

    def actualizar_clima(self):
        if random() < 0.3:
            self.condicion_actual = choice(self.condiciones)
            self.lluvia = self.condicion_actual == 'lluvioso' or self.condicion_actual == 'tormentoso'
    
    def __repr(self) -> str:
        return (f'Condiciones actuales: {self.condicion_actual},'
                f'Lluvia: {self.lluvia}')

class Juego:
    pass

