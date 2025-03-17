class Recetas:
    def __init__(self, id, nombre, objetivo, reactivos_utilizados, procedimiento, valores_a_medir):
        self.id = id
        self.nombre = nombre
        self.objetivo = objetivo
        self.reactivos_utilizados = reactivos_utilizados
        self.procedimiento = procedimiento
        self.valores_a_medir = valores_a_medir

    def show_attr(self):# metodo para mostrar atributos de la clase
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Objetivo: {self.objetivo}")
        print(f"Reactivos utilizados: {self.reactivos_utilizados}")
        print(f"Procedimiento: {self.procedimiento}")
        print(f"Valores a medir: {self.valores_a_medir}")
    
    
        
        
    
       