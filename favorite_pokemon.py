
#le damos la bienvendia al usuario para hacer su perfil
print("Hello!!, welcome to the making of your profile")
print("Heres a few questions that we would like you to answer")

#preguntamos su nombre, definimos el str y ponemos el input
#tambien queria el nombre como en todo mayusculas
name_1=str(input("What is you name?"))
print('Welcome',name_1.lower().upper())

#Preguntamos el sexo, usando if y elif para diferente respuestas
sex_1=str(input("What is your sex?"))
if sex_1== str( "male"):
 print("Nice to meet you my bro")
elif sex_1== str( "female") :
 print("Nice to meet you sis")
else: 
 print("Nice to meet you person")
""

#Preguntamos y definimos region, cada input con diferente respuestas y dando un fin al programa
#Aqui tambien usamos if y elif para diferente respuestas 
region_1=str(input("Where are you from?,Your options are Venezuela, United States or Spain:"))
cosas_favoritas= str()

if region_1==str("United States"):
 print("What a big country!!")
 cosas_favoritas= input("Do you like: hamburguesas, hot dogs or french fries?")
 print("I also really like", cosas_favoritas,"Thank you for responding, the making of your profile is succesful")

elif region_1== str("Venezuela"):
 print("Very hot, but wonderful culture")
 cosas_favoritas= input("Do you like: plato criollo, arepa or cachapa?")
 print("I also really like" ,cosas_favoritas,",Thank you for responding, the making of your profile is succesful")


elif region_1== str("Spain"):
 print("Has some very cool historical buildings")
 cosas_favoritas= input("Do you like: paella, pulpo or calamares?")
 print("I also really like", cosas_favoritas,"Thank you for responding, the making of your profile is succesful")


else: print("those are not some of the options")
exit()



