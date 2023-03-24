num= int(input("ingrese un numero : "))
num2= int(input("ingrese un numero : "))
mcd = 0
while num != 0: 
  if num2== 0:
    break
  resultado = num % num2
  mcd = num2
  num2 =resultado
  
print(f"\nEl maximo comun Divisor entre los dos Numeros es : {int(mcd)}")



