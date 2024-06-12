#Crear una lista y un diccionario con el contenido de esta tabla: 
#ACCION              TERROR        DEPORTES
#MAXIMA VELOCIDAD    LA MONJA       ESPN
#ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#RAPIDO Y FURIOSO I  LA MALDICION   ACCION


tabla_lista=[
    ["Accion","Arma Mortal 4 ,Maxima Velocidad, Rapido y Furioso 1"],
    ["Terror","La monja, El conjuro, La maldicion"],
    ["Deportes","ESPN ,Mas Deporte, Fox Sport"]
]

diccionario={
     "Categorias":"",
     "Accion": "Arma Mortal 4 ,Maxima Velocidad, Rapido y Furioso 1",
     "Terror": "La monja, El conjuro, La maldicion",
     "Deportes": "ESPN ,Mas Deporte, Fox Sport"
}

for fila in tabla_lista:
    print(fila)
for i in diccionario:
    print(f"{i} : {diccionario[i]}")





