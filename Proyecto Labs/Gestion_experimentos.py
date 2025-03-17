from Experimentos import Experimentos
from Recetas import Recetas


class Gestion_Experimentos():
    experimentos=[]
    receta=[]


    def crear_experimentos(self, experimentos_json, recetas_json):# Pon los datos del experimento y recetas en una lista  
       lista_experimentos = []
       for experimento in experimentos_json:
            lista_recetas =[]
            for receta in recetas_json:
               if receta["id"]== experimento["receta_id"]:
                  lista_recetas.append(Recetas(receta["id"], receta["nombre"], receta["objetivo"], receta["reactivos_utilizados"], receta["procedimiento"], receta["valores_a_medir"]))
            lista_experimentos.append(Experimentos(experimento["id"],lista_recetas, experimento["personas_responsables"], experimento["fecha"], experimento["costo_asociado"], experimento["resultado"]))
       self.experimentos = lista_experimentos
    
     
    
   
    def buscar_experimento(self, id):# Buscar el id en especifico de un reactivo
    
       respuesta = None
       for experimento in self.experimentos:
         if int(experimento.id) == int(id):
            respuesta = experimento
         return respuesta 

    def editar_experimento(self, experimento): # se puede editar completamente los reactivos
        #print(experimento)
        if experimento:
        
            print("Datos:")
            print(f"Receta_ID: {experimento.receta_id}")
            print(f"Personas Responsables: {experimento.personas_responsables}")
            print(f"Fecha: {experimento.fecha}")
            print(f"Costo Asociado: {experimento.costo_asociado}")
            print(f"Unidad Medida: {experimento.resultado}")
         
            experimento.personas_responsables = input("Ingresa nuevos personas responsables: (dejalo vacio para quedar con el actual): ") or experimento.personas_responsables
            experimento.fecha = input("Ingresa nueva fecha de experimento: (dejalo vacio para quedar con el actual): ") or experimento.fecha
            experimento.costo_asociado = input("Ingresa nuevo costo de experimento: (dejalo vacio para quedar con el actual): ") or experimento.costo_asociado
            experimento.resultado = input("Ingresa nuevos resultados: (dejalo vacio para quedar con el actual): ") or experimento.resultado
            
    def evaluar_experimento(self, experimento):#para resultados, evalua los valores de medir de las recetas con los resultados de experimento
        if experimento:
            receta=experimento.receta_id[0]#busca id de receta
            print(receta.valores_a_medir[0])#busca los valores de medir de receta
            for valor_medir in receta.valores_a_medir:
               print(valor_medir["minimo"])
               valor=input("Ingresa el valor para {valor_medir.nombre}: ")
               if valor:
                  if float(valor_medir["minimo"]) <= float(valor) and float(valor) <= float(valor_medir["maximo"]):#compara valores
                     print("El valor ingresado esta dentro de los parametros")
                  else:
                     print("El valor no esta dentro de los parametros")
        else:
         print("No se encontró el experimento con el ID proporcionado.")
                    
                
            
           
    
    def eliminar_experimento(self, id):# Corre id de reactivos para eliminar con pop

        for i, experimento in enumerate(self.experimentos):
         if int(experimento.id) == int(id):
            experimento_eliminado = self.experimentos.pop(i)  # Elimina el reactivo y lo guarda
            print("El experimento ha sido eliminado exitosamente")
            return experimento_eliminado  # Retorna el reactivo eliminado
    
        print(f"No se encontró ningún experimento con el ID: {id}")
        return None  # Retorna None si no se encuentra el reactivo
    
    def exp_mas_hecho(self, experimento):
        experimento_mas_hecho=sorted(self.reactivos,key=lambda x: x.fecha_de_caducidad)[:3]
        for recetas in experimento_mas_hecho:
            print(recetas.show_attr())
        info={}  
        for experimento in self.experimentos:  
            if experimento.receta in info:
                info[experimento.receta.nombre]+=1
            else:

                info[experimento.receta.nombre]=1

        print(info)


    
    

    

