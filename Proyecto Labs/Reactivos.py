class Reactivo:
  def __init__(self, id, nombre, descripcion, costo, categoria, inventario_disponible, unidad_medida, fecha_caducidad, minimo_sugerido, conversiones_posibles):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.categoria = categoria
        self.inventario_disponible = inventario_disponible
        self.unidad_medida = unidad_medida
        self.fecha_caducidad = fecha_caducidad
        self.minimo_sugerido = minimo_sugerido
        self.conversiones_posibles = conversiones_posibles

  def show_attr(self): #metodo para mostrar atributos de la clase
        print(f"Id: {self.id}")
        print(f"Nombre:{self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Costo:{self.costo}")
        print(f"Categora:{self.categoria}")
        print(f"Inventario Disponible: {self.inventario_disponible}")
        print(f"Unidad de medida: {self.unidad_medida}")
        print(f"Fecha de caducidad:{self.fecha_caducidad}")
        print(f"minimo_sugerido:{self.minimo_sugerido}")
        print()
          
           
        
                
                
               
                
   





