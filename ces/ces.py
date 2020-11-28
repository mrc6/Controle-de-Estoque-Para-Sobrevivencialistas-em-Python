from datetime import datetime
from mongo_model import insert_one, delete_one, find_all, find_out_of_date
from os import system, name


# Ref.: https://www.geeksforgeeks.org/clear-screen-python/
# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


simulateDB = []


def date_verify(date):
    d_check = date
    while d_check[2] != "-" or d_check[5] != "-" or len(d_check) != 10:
        print("Data informada é inválida, digite novamente ")
        d_check = input("Digite a Validade do Produto no formato DD-MM-AAAA: ")
    year = int(d_check[6:10])
    month = int(d_check[3:5])
    day = int(d_check[0:2])
    return datetime(year, month, day, 00, 00, 00, 000000)


def verify_input_is_number(text):
    while True:
        try:
            n = int(input(text))
            return n
            break
        except ValueError:
            print("Digite apenas números")


def menu_inicial():
    choice = -1
    while choice != 5:
        clear()
        print("Escolha uma opção: ")
        print("1 - Cadastrar Produto")
        print("2 - Excluir Produto")
        print("3 - Ver Produtos Vencidos")
        print("4 - Ver todos os Produtos")
        print("5 - Sair do Sistema")
        choice = verify_input_is_number("Digite a opção escolhida: ")
        if choice == 1:
            name = input("Digite o Nome do Produto: ")
            qty = input("Digite a Quantidade do Produto: ")
            val = input("Digite a Validade do Produto no formato DD-MM-AAAA: ")
            dateTimeVal = date_verify(val)
            simulateDB.append({"name": name, "qty": qty, "val": dateTimeVal})
            insert_one({"name": name, "qty": qty, "val": dateTimeVal})
            input("Digite ENTER para voltar ao menu anterior")
        if choice == 2:
            name = input("Digite o Nome do Produto a ser DELETADO: ")
            print("O produto a ser DELETADO é: ", name)
            yes_or_no = verify_input_is_number("33 - CONFIRMAR, 0 - DESISTIR ")
            if yes_or_no != 33:
                input("Operação não realizada. Digite ENTER")
            else:
                delete_one({"name": name})
                input("Digite ENTER para voltar ao menu anterior")
        if choice == 3:
            actual_date = datetime.now()
            products = find_out_of_date(actual_date)
            clear()
            print("Produtos Vencidos")
            print("Qty Description")
            for product in products:
                print(product["qty"], product["name"])
            input("Digite ENTER para voltar ao menu anterior")
        if choice == 4:
            products = find_all()
            for product in products:
                print(product["name"])
            input("Digite ENTER para voltar ao menu anterior")


menu_inicial()
