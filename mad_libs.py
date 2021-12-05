
def main():
    inicio = """Bienvenido al generador de historias locas, a continuación se te mostrará un texto y debes completarlo como tú desees
    
Habia una vez un 1)______ que vivia en 2)______, desde muy niño siempre quiso ser un 3)______, cuando creció decidio abandonar 
su casa y cumplir su meta de ser el mejor 4)______."""
    print(inicio)
    print("")
    texto_1 = input("completa el literal 1): ")
    texto_2 = input("completa el literal 2): ")
    texto_3 = input("completa el literal 3): ")
    texto_4 = input("completa el literal 4): ")
    print(f"""
Tú historia es:

Habia una vez un {texto_1} que vivia en {texto_2}, desde muy niño siempre quiso ser un {texto_3}, cuando creció decidio abandonar 
su casa y cumplir su meta de ser el mejor {texto_4}.""")

if __name__ == "__main__":

    main()