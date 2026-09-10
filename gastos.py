APP_TITLE = "Controle de Gastos"

gastos = []


def cadastrar_gasto(descricao, valor):
    gastos.append({"descricao": descricao, "valor": valor})


def listar_gastos():
    for gasto in gastos:
        print(f"- {gasto['descricao']}: R$ {gasto['valor']:.2f}")


def total_gastos():
    return sum(gasto["valor"] for gasto in gastos)


def main():
    print(APP_TITLE)

    cadastrar_gasto("Supermercado", 250.50)
    cadastrar_gasto("Conta de luz", 130.00)
    cadastrar_gasto("Internet", 99.90)

    listar_gastos()
    print(f"Total gasto: R$ {total_gastos():.2f}")


if __name__ == "__main__":
    main()
