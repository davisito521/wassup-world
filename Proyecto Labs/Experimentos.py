class Experimentos:
    def __init__(self, id, receta_id, personas_responsables, fecha, costo_asociado, resultado):
        self.id = id
        self.receta_id = receta_id
        self.personas_responsables=personas_responsables
        self.fecha=fecha
        self.costo_asociado=costo_asociado
        self.resultado=resultado

    def show_attr(self):# metodo para mostrar los atributos de la clase
        print(f"ID: {self.id}")
        print(f"Receta del Experimento: ")
        for experimento in self.receta_id:
           experimento.show_attr()
        print(f"Personas responsables: {self.personas_responsables}")
        print(f"Fecha: {self.fecha}")
        print(f"Costo asociado: {self.costo_asociado}")
        print(f"Resultado: {self.resultado}")
        print()
        
        
                

