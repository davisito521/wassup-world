#Todas las medidas lo voy a convertir en ml, por el volumen que tenemos que tomar en cuenta
#En este caso, una tza=240 ml, una cda= 15ml y un cdta= 5ml 


print("Hello, welcome to the kitchen!")
print("Today we will show you how to make some arepas!!")
print("For the recipe, you will need at least 1 cup of water, 1 cup of harina PAN, 1 tablespoon of oil and 1 teaspoon of salt")

#Aqui, convertimos unidades, multiplicamos la cantidad de tazas que quieres con 240(1 tza=240ml), lo mismo con aceite(1 cda=15ml) y sal(1 cdta= 5ml) 
#Para tener todo en ml

ml_water=float(input("How many cups of water would u like?"))*240
ml_flourPAN=float(input("How many cups of harina PAN would u like?"))*240
ml_oil=float(input("How many tablespoons of oil would u like?"))*15
ml_salt=float(input("How many teaspoons of salt would u like?"))*5

#Luego sumamos todo el volumen de todos los ingredientes 

total_ml=(ml_water+ml_flourPAN+ml_oil+ml_salt)

#Finalmente, se multiplica por 0.9 para tomar en cuenta el 10% que se evaporó

total_ml= total_ml*0.9
print("Congrats! you now have a total mix of", total_ml, "ml for your arepas!!")

