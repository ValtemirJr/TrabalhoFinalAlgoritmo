class produto:
    codProd = ''
    nameProd = ''
    priceProd = 0.0
    quantProd = 0


def estoque(l):
    prod = [['2200', 'Amaciante', 3.00, 20], ['2201', 'Sabonete', 3.00, 20], ['2202', 'Detergente', 2.50, 20],
            ['2203', 'Shampoo', 6.00, 18], ['2204', 'Arroz', 15.00, 15], ['2205', 'Feijão', 10.00, 16],
            ['2206', 'Macarrão', 7.00, 22], ['2207', 'Café', 11.00, 20], ['2208', 'Bolacha', 5.00, 23],
            ['2209', 'Água', 1.50, 30]]
    for i in range(len(prod)):
        p = produto()
        p.codProd = prod[i][0]
        p.nameProd = prod[i][1]
        p.priceProd = prod[i][2]
        p.quantProd = prod[i][3]
        l.append(p)


def verificaCodProd(invetario, cod):
    for i in range(len(invetario)):
        if invetario[i].codProd == cod:
            return i
    return -1


def verificaNomeProd(invetario, nome):
    for i in range(len(invetario)):
        if invetario[i].nameProd == nome:
            return i
    return -1


def ehNumFloat(num):  # VERIFICA SE UMA VÁRIAVEL PODE SER FLOAT E DEPOIS CONVERTE PARA FLOAT
    try:  # E RETORNA ESSE VALOR CASO CONTRÁRIO RETORNA -1
        return float(num)
    except ValueError:
        return False


def ehNumInt(num):  # VERIFICA SE UMA VÁRIAVEL PODE SER INT E DEPOIS CONVERTE PARA INT
    try:  # E RETORNA ESSE VALOR CASO CONTRÁRIO RETORNA -1
        return int(num)
    except ValueError:
        return -1


def compra(inventario):
    listaCompra = []
    total = 0
    print("----------------------------------------")
    print("------------COMPRA INICIADA-------------")
    print("----------------------------------------")
    print("PARA FINALIZAR A COMPRA DIGITE [f] COMO CÓDIGO DO PRODUTO")
    while True:
        cp = produto()
        cod = str(input("Código do Produto: "))
        srcProd = verificaCodProd(inventario, cod)
        if cod == 'f':
            print("--------------------------------------------------")
            print("Item  Cód.  Descrição       Quant.    Unit.  Total")
            print("--------------------------------------------------")
            for i in range(len(listaCompra)):
                print(f'{i+1: <5} {listaCompra[i].codProd: <5} {listaCompra[i].nameProd: <13} {listaCompra[i].quantProd: >5} {(listaCompra[i].priceProd/listaCompra[i].quantProd): >10} {listaCompra[i].priceProd: >7}')
            print("--------------------------------------------------")
            print("VALOR TOTAL:                              []   ",total)
            print("--------------------------------------------------")
            return
        if srcProd == -1:
            print("Produto não existe")
        else:
            print("Produto:", inventario[srcProd].nameProd)
            quant = input("Quantidade: ")
            num = ehNumInt(quant)
            if num <= 0 or num > inventario[srcProd].quantProd:
                print("Quantidade inválida ou insuficiente)
                print("Quantidade em estoque:", inventario[srcProd].quantProd )
            else:
                inventario[srcProd].quantProd = inventario[srcProd].quantProd - num
                subTotal = inventario[srcProd].priceProd * num
                total += subTotal
                print("Valor UNIT:", inventario[srcProd].priceProd, "Total:", subTotal)
                print("Saldo:", total)
                cp.codProd = inventario[srcProd].codProd
                cp.nameProd = inventario[srcProd].nameProd
                cp.priceProd = subTotal
                cp.quantProd = num
                listaCompra.append(cp)


def mostraProd(inventario, prod):
    print("----------------------------------------")
    print("Cód.      Nome           Preço    Quant.")
    print("----------------------------------------")
    print(
        f'{inventario[prod].codProd: <7} {inventario[prod].nameProd: <15} {inventario[prod].priceProd: >5} {inventario[prod].quantProd: >8}')
    print("----------------------------------------")


def atualizaProd(inventario):
    cod = str(input("Código do Produto que deseja atualizar: "))
    srcProd = verificaCodProd(inventario, cod)
    while True:
        if srcProd == -1:
            print("Produto não existe")
            cod = str(input("Código do Produto que deseja atualizar: "))
            srcProd = verificaCodProd(inventario, cod)
        else:  # ATUALIZA PREÇO
            print("Produto:", inventario[srcProd].nameProd)
            print("Preço atual:", inventario[srcProd].priceProd)
            novoPreco = input("Novo preço: ")
            num = ehNumFloat(novoPreco)
            if num <= 0:
                print("Preço inválido")
            else:
                inventario[srcProd].priceProd = num
                break
    while True:  # ATUALIZA QUANTIDADE
        print("Quantidade atual:", inventario[srcProd].quantProd)
        novaQuant = input("Nova quantidade: ")
        num = ehNumInt(novaQuant)
        if num < 0:
            print("Quantiade inválida")
        else:
            inventario[srcProd].quantProd = num
            return


def cadastroProd(inventario):
    cp = produto()
    while True:     # CADASTRA CÓDIGO
        cp.codProd = str(input("Código do Produto: "))
        sprod = verificaCodProd(inventario, cp.codProd)
        while cp.codProd == 'f':
            print("Código inválido")
            cp.codProd = str(input("Código do Produto: "))
        if sprod == -1:
            break
        else:
            print("Código já cadastrado")
    while True:     # CADASTRA NOME
        cp.nameProd = str((input("Nome: ")))
        sprod = verificaNomeProd(inventario, cp.nameProd)
        if sprod == -1:
            break
        else:
            print("Nome já cadastrado")
    while True:     # CADASTRA PREÇO
        preco = input("Preço: ")
        num = ehNumFloat(preco)
        if num <= 0:
            print("Preço inválido")
        else:
            cp.priceProd = num
            break
    while True:     # CADASTRA QUANTIDADE
        quant = input("Quantidade: ")
        num = ehNumInt(quant)
        if num < 0:
            print("Quantidade inválida")
        else:
            cp.quantProd = num
            break
    return cp


def relatorioEstoque():
    print("----------------------------------------")
    print("Cód.      Nome           Preço    Quant.")
    print("----------------------------------------")
    for i in range(len(inventario)):
        print(
            f'{inventario[i].codProd: <7} {inventario[i].nameProd: <15} {inventario[i].priceProd: >5} {inventario[i].quantProd: >8}')
    print("----------------------------------------")


def menu():
    print("--------------------------")
    print("1 - Nova Compra")
    print("2 - Consultar Produto")
    print("3 - Atualizar Produto")
    print("4 - Cadastro de  Produto")
    print("5 - Relatório de Produtos")
    print("0 - Encerrar")
    print("--------------------------")
    return str(input())


inventario = []
estoque(inventario)

while True:
    opcaoMenu = menu()
    if opcaoMenu != '0' and opcaoMenu != '1' and opcaoMenu != '2' and opcaoMenu != '3' and opcaoMenu != '4' and opcaoMenu != '5':
        print("Opção inválida")    # OPÇÃO INVÁLIDA
    if opcaoMenu == '0':    # ENCERRA
        print("Sistema encerrado")
        break
    if opcaoMenu == '1':    # COMPRA
        compra(inventario)
    if opcaoMenu == '2':    # CONSULTA
        cod = str(input("Código do Produto: "))
        prod = verificaCodProd(inventario, cod)
        if prod == -1:
            print("Produto não cadastrado")
        else:
            mostraProd(inventario, prod)
    if opcaoMenu == '3':    # ATUALIZA
        atualizaProd(inventario)
    if opcaoMenu == '4':    # CASDASTRO
        novoProd = cadastroProd(inventario)
        inventario.append(novoProd)
    if opcaoMenu == '5':    # RELATÓRIO
        relatorioEstoque()
