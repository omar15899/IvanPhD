class SuperClase:
    def __init__(self, variable1, variable2) -> None:
        self.variable1 = variable1
        self.variable2 = variable2
        self.polla = "hola"


class SubClase(SuperClase):
    def __init__(self, variable1, variable2):
        super().__init__(variable1, variable2)
        self.variable2 = variable2


objeto2 = SubClase(5, 5)
print(objeto2.polla)
print(objeto2.variable)
