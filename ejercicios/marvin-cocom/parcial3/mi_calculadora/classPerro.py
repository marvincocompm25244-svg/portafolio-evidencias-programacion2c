class Perro:
#atributo de la clase perro 
 especie = "Canis lups"


#constructor de clase Perro
def __init__(self,nombre,raza = "caramelo", edad =0):
    self.nombre=nombre
    self.raza=raza
    self.edad=edad

#metodo para imprimir los datos del perro 
def imprimirDatos(self):
    print("Nombre: ", self.nombre)
    print("Raza: " ,self.raza)
    print("Edad: " ,self.edad)
    
def main():
 #crea un objetivo de la clase perro
 perro1= perro1("Firulias","labrador",5,)
 perro1.imprimirDatos()
 perro2= perro2("Rex" , "pastor aleman", 3)
 perro2.imprimirDatos()
 print("informacion del perro2:" ,perro2.nombre,perro2.raza,perro2.edad)
 perro3 = perro3("max", "Bulldog", 2)
 perro3.imprimirDatos()
 perro4 = perro4("Dante",)
 perro4.edad = 4
 perro4.imprimirDatos()
 perro2.raza = "pastor Belga"
 perro2.imprimirDatos()
 perro5 = perro5("raya", "siames", 1)
 perro5.especie = "Feliz catus"
 perro5.imprimirDatos()

 if __name__ == "__main__":
    main()
    