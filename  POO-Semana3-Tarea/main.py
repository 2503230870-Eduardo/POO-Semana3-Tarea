# main.py

from cafetera import Cafetera, Filtro, Prensa, Capsulas

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
