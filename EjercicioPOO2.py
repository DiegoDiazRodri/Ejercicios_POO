class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mostrar_estado(self):
        if self.nota>=3:
            print("Desaprobo")
        else:
            print("Aprobo")


# bloque principal

alumno1=Alumno()
alumno1.inicializar("diego",1)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno()
alumno2.inicializar("ana",8)
alumno2.imprimir()
alumno2.mostrar_estado()