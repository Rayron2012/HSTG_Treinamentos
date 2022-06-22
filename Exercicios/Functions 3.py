meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}

def apontador_de_indicadores(meta, lista):
    ganhadores = []
    qtd_meta_batida = 0
    qtd_total = 0
    for vendedor in lista:
        valor = lista[vendedor]
        if valor > meta:
            ganhadores.append(vendedor)
            qtd_meta_batida += 1
        if valor != "":
            qtd_total += 1
        porcento = qtd_meta_batida / qtd_total
    return ganhadores, porcento

print(apontador_de_indicadores(meta, vendas))




