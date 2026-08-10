class Galleta_chocolate:
    def __init__(self, sabor):
        self.sabor = sabor

    def mostrar_sabor(self):
        return f"El sabor de la galleta es {self.sabor}"


p = Galleta_chocolate("chocolate")
print(p.mostrar_sabor())
