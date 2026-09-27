import random

def jugar():
    print("¡Bienvenido a 'Adivina el Número'!")
    print("He pensado un número entre 1 y 100.")
    print("Intenta adivinarlo.")

    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            adivinanza = int(input("Tu guess: "))
            intentos += 1

            if adivinanza < numero_secreto:
                "Muy bajo! Intenta de nuevo."
            elif adivinanza > numero_secreto:
                "Muy alto! Intenta de nuevo."
            else:
                print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    jugar()