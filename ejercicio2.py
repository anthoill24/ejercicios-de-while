N = int(input("Ingrese el numero"))  
primerN= 1
anterior = 0
sum =0
numPar = []
numInpar = []
while N >= 0 : 
  sum = primerN + anterior
  anterior = primerN
  primerN = sum
  N-=1
  if sum%2 == 0 :
     numPar.append(primerN)
  else:
   numInpar.append(primerN)  

print(f"los numeros pares son : {(numPar)} , y los numeros impares son : {(numInpar)} ")   
   
  

    
   