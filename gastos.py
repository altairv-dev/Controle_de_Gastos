APP_TITLE = "Controle de Gatos"

gastos = []


def cadastrar_gasto(descricao, valor):
    gastos.append({"descricao": descricao, "valor": valor})


def main():
    print(APP_TITLE)


if __name__ == "__main__":
    main()
