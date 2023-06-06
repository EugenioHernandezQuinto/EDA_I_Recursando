diccionario={}
diccionario['gelatina'] = 'dgari'
diccionario['leche'] = 'santa'
diccionario['papel'] = 'petalos'
diccionario['tortillas'] = 'noBrand'
diccionario['lumus'] = 'laCosteña'


print("diccionario {}".format(diccionario))

diccionario['gelatina'] = None
print("diccionario {}".format(diccionario)) #quita mal, no quita el elemento bien, curioso que digamos que con el codigo(key) quitamos el nombre(item)

diccionario.pop('lumus')#quita el key y el item #.pop se llama method
print("diccionario {}".format(diccionario)) 

diccionario.popitem()#quita solo item, pero el último
print("diccionario {}".format(diccionario)) 

#lo que tenemos que hacer es poder quitar key Y item, ya sea con key o item. 
