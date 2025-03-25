def maxmin(lista):
    if len(lista) == 1:
        result = [lista[0], lista[0]]
        return result

    if len(lista) == 2:
        if lista[0] > lista[1]:
            result = [lista[1], lista[0]]
            return result
        else:
            result = [lista[0], lista[1]]
            return result

    meio = len(lista)//2
    esquerda = lista[:meio]
    direita = lista[meio:]

    min_esq, max_esq = maxmin(esquerda)
    min_dir, max_dir = maxmin(direita)

    min_total = min(min_esq, min_dir)
    max_total = max(max_esq, max_dir)

    result = [min_total, max_total]
    return result

def main():
    lista = []

    print("Digite os números da sua lista. Para parar, digite FIM.")
    while True:
        entrada = input()

        if entrada.upper() == "FIM":
            break

        for i in entrada.split():
            lista.append(int(i))

    if not lista:
        print("Lista vazia!")

    else:
        resultado = maxmin(lista)
        print("Os números min e máx são {} e {}".format(resultado[0], resultado[1]))

main()