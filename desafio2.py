
import textwrap


def menu():
    menu = """
    -----------MENU-----------

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo Usuário
    [5] Nova Conta
    [6] Listar Contas
    [0] Sair

    --------------------------
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo+=valor
        extrato+=f"Depósito de: R$ {valor:.2f} \n"
        print("Depósito efetuado com sucesso!")

    else:
        print("Operação Falhou! O valor informado é invaldido.") 
             
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor < 0:
        print("Operação Falhou! O valor informado é invaldido.")

    elif valor <= limite:

        if numero_saques < limite_saques:

            if valor <= saldo:
                extrato += f"Saque de: R$ {valor:.2f} \n"
                saldo -= valor
                print("Saque efetuado com sucesso!")

            else:
                print("Operação Falhou! Valor informado para saque é maior que o saldo.")

        else:
            print("Operação Falhour! A quantidade de saques por dia já foi efetuada.")

    else:
        print("Operação Falhour! O valor informado é maior que o limite por saque.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n#################### EXTRATO ####################")
    print("Não foram realizadas movimentações na conta." if not extrato else extrato)
    print(f"\nSaldo de: R$ {saldo:.2f}")
    print("##################################################")


def criar_usuario(usuarios):
    cpf = input("informe o seu CPF (apenas número): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\nOperação Falhou! Já existe usuário com esse CPF.")
        return
    
    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("informe o seu endereço (logradouro, numero - bairro - cidade/sigla do estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
        })
    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        contas.append({
            "agencia": agencia, 
            "numero_conta": numero_conta, 
            "usuario": usuario
            })
        return None
    
    print("Operação Falhou! Usuário não encontrado.")


def listar_contas(contas):
    for conta in contas:
        texto = f"""
            Agência: {conta['agencia']}
            Conta: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print(textwrap.dedent(texto))



saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []

LIMITE_SAQUES = 3
AGENCIA = "0001"

while True:

    opcao = menu()
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito :"))

        saldo, extrato = depositar(saldo, valor, extrato)
        
    elif opcao == "2":
        valor = float(input("Informe o valor do saque : "))
        copia_saldo = saldo
        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )
        if saldo != copia_saldo:
            numero_saques += 1
        
    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "4":
        criar_usuario(usuarios)    

    elif opcao == "5":
        numero_conta = len(contas) + 1
        criar_conta(AGENCIA, numero_conta, usuarios, contas)



    elif opcao == "6":
        listar_contas(contas)

    elif opcao == "0":
        break

    else:
        print("Opção Inválida, por favor selecione novamente a opção desejada.")