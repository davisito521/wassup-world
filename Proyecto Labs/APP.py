import requests
from Gestion_reactivos import Gestion_Reactivos
from Gestion_experimentos import Gestion_Experimentos

class App:
    def obtener_datos(self,url, params=None): #Obtiene datos del API
        try:
            response_json= requests.get(url, params=params)
            return response_json.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
        
        #Ejemplo de uso
    def cargar_datos(self):#Carga los datos com json
        self.experimentos_json=self.obtener_datos("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/experimentos.json")
        self.recetas_json=self.obtener_datos("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/recetas.json")
        self.reactivos_json=self.obtener_datos("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/refs/heads/main/reactivos.json")
        Gestion_Reactivos.crear_reactivos(self, self.reactivos_json)
        Gestion_Experimentos.crear_experimentos(self, self.experimentos_json, self.recetas_json)
        

        
    
         
    def menu_principal(self): #Aqui esta el menu principal
        while True: #Entre API y txt
            menu=input("Seleccione una opción para empezar: \n\t1. Cargar API \n\t2. Cargar por txt \n\t--->  ")

            if menu=="1":
                while True:# Input entre los diferentes modulos
                 menu_labs=input("Bienvenido al Laboratorio de Química!!, selecciona una opción: \n\t1. Gestión de reactivos\n\t2. Gestión de Experimentos\n\t3. Gestión de Resultados\n\t4. Estadísticas\n\t---> ")

                 if menu_labs=="1":
                     while True:#Gestion de Reactivos
                         menu_reactivos=input("Elige una opción que quieres realizar con los reactivos: \n\t1. Ver reactivo\n\t2. Editar reactivo\n\t3. Eliminar reactivo\n\t4.Mostrar todo reactivos\n\t---> ")
                         
                         
                         if menu_reactivos == "1":#Buscar un reactivo en especifico, te muestra datos, conversiones y verifica inventario 
                             id_reactivo = input("Introduce el ID del reactivo que deseas ver: ")
                             reactivo = Gestion_Reactivos.buscar_reactivo(self, id_reactivo)
                             if reactivo:
                                 print(f"Nombre: {reactivo.nombre}")
                                 print(f"Descripción: {reactivo.descripcion}")
                                 print(f"Inventario Disponible: {reactivo.inventario_disponible}")
                                 print(f"Unidad Medida: {reactivo.unidad_medida}")
                                 print(f"Minimo Sugerido: {reactivo.minimo_sugerido}")
                                 print(f"Fecha de Caducidad {reactivo.fecha_caducidad}")
                                 Gestion_Reactivos.verificar_inventario(self, reactivo)
                                 Gestion_Reactivos.mostrar_conversiones(self, reactivo)
                             else:
                                 print("Reactivo no encontrado.")

                         elif menu_reactivos=="2":#Un reactivo en especifico para editar
                             id_reactivo = input("Introduce el ID del reactivo que deseas editar: ")
                             reactivo = Gestion_Reactivos.buscar_reactivo(self, id_reactivo)
                             if reactivo:
                                 Gestion_Reactivos.editar_reactivo(self,reactivo)

                         elif menu_reactivos=="3":# Un reactivo en especifico para eliminar
                             id_reactivo = input("Introduce el ID del reactivo que deseas eliminar: ")
                             reactivo= Gestion_Reactivos.buscar_reactivo(self, id_reactivo)
                             if reactivo:
                                 Gestion_Reactivos.eliminar_reactivo(self, id_reactivo)

                         elif menu_reactivos=="4":#Muestra todo los reactivos
                             if self.reactivos:
                                for i in self.reactivos:
                                    i.show_attr()


                 if menu_labs=="2":
                     while True:#Gestion de Experimentos
                         menu_experimentos=input("Elige una opción que quieres realizar con los experimentos: \n\t1. Ver experimento\n\t2. Editar experimento\n\t3. Eliminar experimento\n\t4. Mostrar todos los experimentos\n\t5. Realizar Experimento\n\t--->  ")
                         if menu_experimentos=="1":#Buscar un experimento en especifico, te muestra datos con datos de recetas
                           id_experimento = input("Introduce el ID del experimento que deseas ver: ")
                           experimento = Gestion_Experimentos.buscar_experimento(self, id_experimento)
                           if experimento:
                             experimento.show_attr()
                           else:
                            print("Experimento no encontrado.")

                         if menu_experimentos=="2":# Un experimento en especifico para editar
                             id_experimento = input("Introduce el ID del experimento que deseas editar: ")
                             experimento = Gestion_Experimentos.buscar_experimento(self, id_experimento)
                             if experimento:
                                 Gestion_Experimentos.editar_experimento(self,experimento)


                         if menu_experimentos=="3": # Un experimento en especifico para eliminar
                             id_experimento = input("Introduce el ID del experimento que deseas eliminar: ")
                             experimento = Gestion_Experimentos.buscar_experimento(self, id_experimento)
                             if experimento:
                                 Gestion_Experimentos.eliminar_experimento(self, id_experimento)



                         if menu_experimentos=="4":# Muestra todo los experimentos
                             if self.experimentos:
                                 for i in self.experimentos:
                                     i.show_attr()


                         if menu_experimentos=="5": # Realizar un experimento, indica inventario restante y si esta vencido los reactivos
                             id_experimento = input("Introduce el ID del experimento que deseas realizar: ")
                             experimento = Gestion_Experimentos.buscar_experimento(self, id_experimento)
                             validar_reactivo= Gestion_Reactivos.validar_fecha_caducidad(self, experimento)
                             if experimento and validar_reactivo:
                                 
                                 print("La cantidad de tu inventario restante es: ")
                                 Gestion_Reactivos.realizar_experimento(self, experimento)


                 if menu_labs=="3":# Gestion de Resultados, muestra resultado de experimento en especifico y evalua si estaba dentro de parametros
                    id_resultado= input("Introduce el resultado del experimento que deseas ver: ")
                    experimento = Gestion_Experimentos.buscar_experimento(self, id_resultado)
                    
                    if experimento:
                        print(f"Valores a medir: {experimento.receta_id[0].valores_a_medir}")
                        print(f"Resultados de Experimento: {experimento.resultado}")
                        Gestion_Experimentos.evaluar_experimento(self, experimento)


                 if menu_labs=="4":#Gestion de Estadisticas
                     while True: 
                         menu_estadisticas=input("Bienvenido a las estadisticas, cual estadisticas quieres ver:\n\t1. Investigadores que mas utilizan el laboratorio\n\t2. El Experimento mas hecho y menos hecho\n\t3. Top 5 reactivos en rotacion\n\t4. Top 3 reactivos en de mayor desperdicio\n\t5. Reactivos que mas se vencen\n\t6. Veces que no se logro hacer un experimento por falta de reactivos\n\t---> ")
                         if menu_estadisticas=="2":# El Experimento mas hecho y menos hecho
                             experimento=None
                             reactivo=None
                             print("El experimento mas hecho es:")
                             Gestion_Experimentos.exp_mas_hecho(self, experimento, reactivo)
                             



                
                     



                    





                        
                                     


                            
                             
                         
                             
                             

                    



                            



                             
                             
                         

                             

                             
                             



                
            
