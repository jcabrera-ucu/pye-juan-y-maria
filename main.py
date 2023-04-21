import random

def tirar_dado():
    return random.randint(1, 6)


def calcular_puntaje(dado_1, dado_2):
    if dado_1 == 4:
        return dado_2
    elif dado_2 == 4:
        return dado_1
    else:
        return 0


def tirar_ambos_dados():
    return calcular_puntaje(tirar_dado(), tirar_dado())


def juan():
    puntaje = tirar_ambos_dados()
    if puntaje == 0:
        return tirar_ambos_dados()
    elif puntaje <= 3:
        return tirar_dado()
    else:
        return puntaje


def maria(puntaje_de_juan):
    puntaje = tirar_ambos_dados()
    if puntaje == 0:
        return tirar_ambos_dados()
    else:
        if puntaje > puntaje_de_juan:
            return puntaje
        elif puntaje == puntaje_de_juan:
            if puntaje <= 3:
                return tirar_dado()
            else:
                return puntaje
        else:  # puntaje < puntaje_de_juan
            return tirar_dado()



if __name__ == '__main__':
    for tiradas in [10_000, 100_000, 300_000]:
        gana_juan = 0
        gana_maria = 0
        empatan = 0

        for _ in range(tiradas):
            puntaje_juan = juan()
            puntaje_maria = maria(puntaje_juan)

            if puntaje_juan == puntaje_maria:
                empatan += 1
            elif puntaje_juan > puntaje_maria:
                gana_juan += 1
            else:
                gana_maria += 1

        print(f'Gana juan:  {gana_juan} veces de {tiradas}. Frecuencia relativa: {gana_juan / tiradas}')
        print(f'Gana maría: {gana_maria} veces de {tiradas}. Frecuencia relativa: {gana_maria / tiradas}')
        print(f'Empatan:    {empatan} veces de {tiradas}. Frecuencia relativa: {empatan / tiradas}')
        print()