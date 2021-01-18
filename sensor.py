import random

temp = random.randint(15, 28)
pdh=65267
g=5000
a=3
A=((g**a) % pdh)

ciudad = 'Viña del Mar'


f = open ('./ProyectoCripHacks/temperatura.txt','w')
f.write(str(A)+"\n")

temperatura = "La temperatura en "+ ciudad + " es de " + str(temp) +"°C."
p=503
q=643
n=p*q
d=(p-1)*(q-1)
k=5

caracteres=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"," ",",","°","-","/","."]
texto=[]

print("Encriptando mensaje..\n")
for letra in temperatura:
    i=0
    for caracter in caracteres:
        if (letra==caracter):
            texto.append(i)
        i+=1
print("Mensaje encriptado..\n")
textocifrado=[]

print("Creando archivo de texto..\n")
for t in texto:
    cifrado = (t**k) % n
    textocifrado.append(cifrado)
    f.write("%s\n" % cifrado)
print("Archivo de texto creado..\n")
f.close

