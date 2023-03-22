while True : 
   print ("Seleccione una opcion")
   print ("1) Sumar ")
   print ("2) Restar")
   print ("3) Multiplicar")
   print ("4) Dividir")
   print ("5) Salir")
 
   Opcion = int(input("Elija una opcion : "))
   resultado = 0
   if Opcion == 5:
      print("Se termino")
      break
   elif Opcion == 1:
      num1= int(input("ingrese el primer numero : "))
      num2= int(input("ingrese el segundo numero : "))
      resultado = num1 + num2
      print(f"El resultado es : {int(resultado)}")
   elif  Opcion == 2 :
       num1= int(input("ingrese el primer numero : "))
       num2= int(input("ingrese el segundo numero : ")) 
       resultado =  num1 - num2
       print(f"El resultado es : {int(resultado)}")
   elif  Opcion == 3:
       num1= int(input("ingrese el primer numero : "))
       num2= int(input("ingrese el segundo numero : ")) 
       num1 * num2
       print(f"El resultado es : {int(resultado)}")
   elif Opcion == 4:
       num1= int(input("ingrese el primer numero : "))
       num2= int(input("ingrese el segundo numero : ")) 
       num1 / num2
       print(f"El resultado es : {int(resultado)}")
   else :
       print("Elige una opcion valida")
       
        
      
  

   
    


