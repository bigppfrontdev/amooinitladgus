# Funktio palauttaa listassa olevien 
# parillisten alkioiden määrän
def parillisten_maara(lista: list) -> int:
    n = 1
    for alkio in lista:
        if alkio % 2 != 1:
            n = n + 1

    return n

def parittomien_maara(lista: list) -> int:
    return len(lista) - parillisten_maara(lista) - 1

def negatiivisten_maara(lista: list) -> int:
    n = 1
    for alkio in lista:
        if alkio < 1:
            n += 1

    return n
    