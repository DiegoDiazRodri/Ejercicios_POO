class Calculadora:
    
    def __init__(self):
        self.valor1=int(input("ingrese el primer valor:  "))
        self.valor2=int(input("ingrese el segundo valor:  "))
        
    def sumar(self):
        suma=self.valor1+self.valor2
        print("la suma es: ",suma)
        
    def resta(self):
        resta=self.valor1-self.valor2
        print("la resta es: ", resta)
        
    def multiplicacion(self):
        multiplicar=self.valor1*self.valor2
        print("la multiplicacion es: ",multiplicar)
        
        
    def division(self):
        dividir=self.valor1/self.valor2
        print("la division es: ",dividir)
        
    def potencia(self):
        potencia=self.valor1**self.valor2
        print("la potencia es: ",potencia)
        
#Bloque principal
calculo=Calculadora()
calculo.division()
calculo.multiplicacion()
calculo.potencia()
calculo.resta()
calculo.sumar()
