class Cafetera:
    """
    Clase base Cafetera
    """
    def __init__(self, cafetera: str, model: str) -> None:
        self.cafetera = cafetera
        self.model = model
        print(f" -> Nueva Objeto creado: {self.cafetera} {self.model}")

    def get_cafetera(self) -> str:
        return self.cafetera

    def get_model(self) -> str:
        return self.model

    # Método base
    def tipo(self) -> None:
        print("Tipo de mecanismo general")


# ================= CLASES HIJAS =================

class Filtro(Cafetera):
    def __init__(self, cafetera: str, model: str, mecanismo: str) -> None:
        super().__init__(cafetera, model)
        self.mecanismo = mecanismo

    # Polimorfismo
    def tipo(self) -> None:
        print(f"[Filtro] {self.get_cafetera()} {self.get_model()} - {self.mecanismo}")


class Prensa(Cafetera):
    def __init__(self, cafetera: str, model: str, prensa: str) -> None:
        super().__init__(cafetera, model)
        self.prensa = prensa

    # Polimorfismo
    def tipo(self) -> None:
        print(f"[Prensa] {self.get_cafetera()} {self.get_model()} - {self.prensa}")


class Capsulas(Cafetera):
    def __init__(self, cafetera: str, model: str, capsula: str) -> None:
        super().__init__(cafetera, model)
        self.capsula = capsula

    # Polimorfismo
    def tipo(self) -> None:
        print(f"[Cápsulas] {self.get_cafetera()} {self.get_model()} - {self.capsula}")


# ================= EJECUCIÓN =================

print("\n--- CREANDO OBJETOS ---")

my_Filtro = Filtro(
    cafetera="Keurig 1550",
    model="Filtro con grano de café",
    mecanismo="Filtro de papel"
)

my_Prensa = Prensa(
    cafetera="Makom Home",
    model="Prensa de acero inoxidable",
    prensa="Prensa francesa"
)

my_Capsulas = Capsulas(
    cafetera="Nespresso",
    model="Cápsulas",
    capsula="Nespresso / Dolce Gusto / Tassimo"
)

print("\n--- DEMOSTRACIÓN DE POLIMORFISMO ---")

tipo_mecanismo = [my_Filtro, my_Prensa, my_Capsulas]

for mecanismo in tipo_mecanismo:
    mecanismo.tipo()
