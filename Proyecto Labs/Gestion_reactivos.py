from Reactivos import Reactivo
from datetime import datetime
import random

class Gestion_Reactivos():
    reactivos=[]
    def crear_reactivos(self, reactivos_json):# Pon los datos del reactivos en una lista       

        lista_reactivos = []
        for reactivo in reactivos_json:
            lista_reactivos.append(Reactivo(reactivo["id"], reactivo["nombre"], reactivo["descripcion"], reactivo["costo"], reactivo["categoria"], reactivo["inventario_disponible"], reactivo["unidad_medida"], reactivo["fecha_caducidad"], reactivo["minimo_sugerido"], reactivo["conversiones_posibles"]))
        self.reactivos = lista_reactivos
     

   
    def buscar_reactivo(self, id):# Buscar el id en especifico de un reactivo
     respuesta = None
     for reactivo in self.reactivos:
        if int(reactivo.id) == int(id):
            respuesta = reactivo
     return respuesta
    
    
    def eliminar_reactivo(self, id):# Corre id de reactivos para eliminar con pop
        for i, reactivo in enumerate(self.reactivos):
         if int(reactivo.id) == int(id):
            reactivo_eliminado = self.reactivos.pop(i)  # Elimina el reactivo y lo guarda
            print("El reactivo ha sido eliminado exitosamente")
            return reactivo_eliminado  # Retorna el reactivo eliminado
    
        print(f"No se encontró ningún reactivo con el ID: {id}")
        return None  # Retorna None si no se encuentra el reactivo
    

    def mostrar_conversiones(self, reactivo):#Muestra conversiones posibles
        if reactivo:
            print("Conversiones posibles:")
           
            for conversion in reactivo.conversiones_posibles:
              print(conversion)

    def validar_fecha_caducidad(self, experimento):# Valida fecha de vencimiento de los reactivos en un experimento
        receta=experimento.receta_id
        fecha_caducidad_exp= datetime.strptime(experimento.fecha, "%Y-%m-%d")#aqui se accede la fecha del experimento
        for reactivo_info in receta[0].reactivos_utilizados:#acceda a los reactivos utilizados de las recetas en un experimento
            id_reactivo = reactivo_info["reactivo_id"]
            for reactivo in self.reactivos:#confirma id
             if int(reactivo.id) == int(id_reactivo):
                respuesta = reactivo
            reactivo =  respuesta
            fecha_caducidad = datetime.strptime(reactivo.fecha_caducidad, "%Y-%m-%d")#aqui se accede la fecha de caducidad del reactivo
            
            if fecha_caducidad < fecha_caducidad_exp:
                print(f"El reactivo '{reactivo.nombre}' está caducado.")
                return False
        return True
    
    
        
    def editar_reactivo(self, reactivo):# se puede editar completamente los reactivos


        if reactivo:
            print("Current details:")
            print(f"Nombre: {reactivo.nombre}")
            print(f"Descripcion: {reactivo.descripcion}")
            print(f"Costo: {reactivo.costo}")
            print(f"Categoria: {reactivo.categoria}")
            print(f"Inventario Disponible: {reactivo.inventario_disponible}")
            print(f"Unidad Medida: {reactivo.unidad_medida}")
            print(f"Fecha Caducidad: {reactivo.fecha_caducidad}")
            print(f"Minimo Sugerido: {reactivo.minimo_sugerido}")
            print(f"Conversiones Posibles: {reactivo.conversiones_posibles}")

            reactivo.nombre = input("Ingresa nuevo nombre: (dejalo vacio para quedar con el actual): ") or reactivo.nombre
            reactivo.descripcion = input("Ingresa nuevo descripcion: (dejalo vacio para quedar con el actual): ") or reactivo.descripcion
            reactivo.costo = input("Ingresa nuevo costo: (dejalo vacio para quedar con el actual): ") or reactivo.costo
            reactivo.categoria = input("Ingresa nueva categoria: (dejalo vacio para quedar con el actual): ") or reactivo.categoria
            reactivo.inventario_disponible = input("Ingresa nuevo inventario disponible: (dejalo vacio para quedar con el actual): ") or reactivo.inventario_disponible
            reactivo.unidad_medida = input("Ingresa nuevo unidad de medida: (dejalo vacio para quedar con el actual): ") or reactivo.unidad_medida
            nueva_fecha_caducidad = input("Ingresa nuevo fecha de caducidad: (dejalo vacio para quedar con el actual): ") or reactivo.fecha_caducidad
            if nueva_fecha_caducidad:
                from datetime import datetime
                fecha_caducidad = datetime.strptime(nueva_fecha_caducidad, "%Y-%m-%d")
                if fecha_caducidad < datetime.now():
                    print(f"Advertencia: La nueva fecha de caducidad para '{reactivo.nombre}' está en el pasado.")
            reactivo.fecha_caducidad = nueva_fecha_caducidad

            reactivo.minimo_sugerido = input("Ingresa nuevo minimo sugerido: (dejalo vacio para quedar con el actual): ") or reactivo.minimo_sugerido
           
   
    def verificar_inventario(self, reactivo): #verifica el inventario disponible con el minimo sugerido       

        if int(reactivo.inventario_disponible) <= int(reactivo.minimo_sugerido):
            print(f"Alerta: El reactivo '{reactivo.nombre}' está en el nivel mínimo sugerido. Por favor, reponlo.")


    def realizar_experimento(self, experimento):#realizar un experimento con datos del reactivo y de la receta
        receta = experimento.receta_id #accede a la receta de un experimento id
        suma_costo= experimento.costo_asociado 
        for reactivo_info in receta[0].reactivos_utilizados:# accede a los reactivos utilizados en la receta
            id_reactivo = reactivo_info["reactivo_id"]
            for reactivo in self.reactivos:
             if int(reactivo.id) == int(id_reactivo):
                respuesta = reactivo
            reactivo =  respuesta
            suma_costo += reactivo.costo #suma el costo del reactivo con el costo del expermento
            
            minimo = 0.001  # 0.1%
            maximo = 0.225  # 22.5%
            resta= float(reactivo.inventario_disponible)-float(reactivo_info["cantidad_necesaria"])

            # Generar un número aleatorio de punto flotante entre el mínimo y el máximo
            porcentaje_aleatorio = random.uniform(minimo, maximo)
            reactivo.inventario_disponible=resta-(porcentaje_aleatorio*resta)
            print(f"El reactivo {reactivo.nombre} tiene el siguiente inventario: {reactivo.inventario_disponible}")
        print("El costo de los reactivos mas el costo del experimento es: ")
        print(suma_costo)
        


           

    
       
