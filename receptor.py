pdh=65267
g=5000
b=36389

caracteres=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"," ",",","°","-","/","."]
p=503
q=643
n=p*q
d=(p-1)*(q-1)
A=0
Kb=0
textodescifrado=[]
print("Leyendo texto..")
texto = open ('temperatura.txt','r')

i=0
print("Descifrando texto..")
for t in texto:
    if i==0:
        A=int(t)
        Kb=((A**b) % pdh)
    else:
        t2=int(t)
        descifrado = (t2**Kb) % n
        textodescifrado.append(descifrado)
    i+=1

textodescifradol=[]
for num in textodescifrado:
    textodescifradol.append(caracteres[num])

print("Texto descifrado..")
textodescifrado = "".join(textodescifradol)
print(textodescifrado)
