# **** ZONA DE CLASE ****
#se crea la clase
class cliente:
    #se crea el modo constructo de la clase
    def __init__(self):
        #se crea los atributos de la clase
        self.nombre_cliente = ""
        self.apellido_cliente = ""
    
    # crear metodos get y set por atributos
    def get_nombre_cliente(self):
        return self.nombre_cliente
    
    def get_apellido_cliente(self):
        return self.apellido_cliente
    
    def set_nombre_cliente(self, dato_cliente):
        self.nombre_cliente = dato_cliente
        
    def set_apellido_cliente(self, dato_cliente):
        self.apellido_cliente = dato_cliente
            
    #se crea metodos normales de la clase   
    
    def tomar_datos(self):
        pass
        