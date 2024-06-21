import time


memes_dict = {
             "CRINGE": "algo que pueda generar rechazo o que genera pena ajena",
             "XD": "expresion usada cuando algo nos da risa",
             "FANBOY": "fan empedernido que no se da cuenta de que el producto que admira puede tener defectos"
             }
for i in range(5):
    time.sleep(3)
    word = input("que palabra quieres aprender").upper()
    if word in memes_dict.keys():
        print(memes_dict[word])
    else:
        print("la palabra no está en el diccionario")
