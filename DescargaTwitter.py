#encoding: UTF-8

import requests
url = "https://twitter.com/katyperry"
info = requests.get(url)
if info.status_code == 200:	# lectura correcta?
    print(info.text)		# Procesa los datos

listaLineas = info.text.split("\n")
indice = 0
linea = listaLineas[indice]
while 'u-hiddenVisually">Seguidores' not in linea:
    indice += 1
    linea = listaLineas[indice]

linea = listaLineas[indice+1]

print("***** ", linea , " ++++")
tokens = linea.split()
print(tokens)
datos = tokens[2].split("=")
seguidores = int(datos[1])
print("Seguidores:",seguidores)

for linea in listaLineas:
    if "TweetTextSize" in linea:
        print(linea[linea.index('">')+2:])
