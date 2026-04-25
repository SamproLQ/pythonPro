import time
meme_dict = {
            "CRINGE": "algo excepcionalmente raro o embarazoso",
            "LOL": "una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY" : "aterrador, siniestro",
            "AGGRO" : "ponerse agresivo/enojado"
            }
control = 1
print("Hemos recopilado algunas palabras que puede que no todos entiendan")
while control < 6:

    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        print("Ya")
        time.sleep(.5)
        print("Pues esa palagra significa "+ meme_dict[word])
        time.sleep(2)
        if control != 5:
            print("Preguntame otra")
        control += 1
    else:
        print("Lastimosamente no lo tengo en la base de datos")
        time.sleep(.5)
        print("Prueva otra palabra")
        time.sleep(.5)
        
