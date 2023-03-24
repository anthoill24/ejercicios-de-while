def es_primo(numero):
  primo = numero
  numEntero = []
  resultado = 0
  numeropri = 0
  while numero >= 1:
    numero -= 1
    if numero >= 1:
      numeropri = primo / numero
    resultado = numeropri
    if resultado % 1 == 0:
      numEntero.append(resultado)

  if len(numEntero) > 2:
    print(f"El numero {primo} no es primo")
  else:
    print(f"El numero {primo} Es primo")

intervalo = 1
numero = int(input("ingrese numero : "))
while intervalo < numero:
  intervalo += 1
  es_primo(intervalo)


           

    
            
       
         
       


      
      
    


# "{:.2f}".format(numeropri).rstrip("0").rstrip(".")