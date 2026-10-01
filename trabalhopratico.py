# 1. Nome do cliente

def ler_nome():
    nome = input("Digite seu nome: ").strip()
    while nome == "":
        print("Nome inválido! O nome não pode ficar em branco.")
        nome = input("Digite seu nome novamente: ").strip()
    return nome


def mostrar_cardapio():
    # Cardápio 
    print("\n--- CARDÁPIO ---")
    print("1 - X-Burguer (R$ 20.00)")
    print("2 - X-Bacon (R$ 25.00)")
    print("3 - X-Tudo (R$ 32.00)")
    print("4 - X-Salada (R$ 15.00)")
    print("5 - Suco Natural (R$ 10.00)")


def obter_o_nome_produto(codigo):
    if codigo == "1":
        return "X-Burguer"
    elif codigo == "2":
        return "X-Bacon"
    elif codigo == "3":
        return "X-Tudo"
    elif codigo == "4":
        return "X-Salada"
    elif codigo == "5":
        return "Suco Natural"
    else:
        return ""
    
def obter_preco_produto(codigo):
    if codigo == "1":
        return 20.00
    elif codigo == "2":
        return 25.00
    elif codigo == "3":
        return 32.00
    elif codigo == "4":
        return 15.00
    elif codigo == "5":
        return 10.00
    else:
        return 0.0
 
 
def ler_codigo():
    codigo = input("Digite o código do produto desejado: ").strip()
    while obter_o_nome_produto(codigo) == "":
        print("Código inválido! Digite um número de 1 a 5.")
        codigo = input("Digite o código do produto desejado: ").strip()
    return codigo
 
 
def ler_quantidade(produto):
    texto = input(f"Quantas unidades de {produto} você deseja? ").strip()
    while not texto.isdigit() or int(texto) <= 0:
        print("Quantidade inválida! Digite um número inteiro maior que zero.")
        texto = input(f"Quantas unidades de {produto} você deseja? ").strip()
    return int(texto)
 
 
def perguntar_continuar():
    resposta = input("Deseja adicionar outro produto? (S/N): ").strip().upper()
    while resposta != "S" and resposta != "SIM" and resposta != "N" and resposta != "NAO" and resposta != "NÃO":
        print("Resposta inválida! Digite sim ou  não.")
        resposta = input("Deseja adicionar outro produto? (S/N): ").strip().upper()
    return resposta == "S" or resposta == "SIM"
 
 
def calcular_percentual_desconto(total):
    if total < 50.00:
        return 0
    elif total < 100.00:
        return 5
    else:
        return 10
 
 
def escolher_pagamento():
    forma_pagamento = ""
    while forma_pagamento == "":
        print("\n--- FORMA DE PAGAMENTO ---")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão")
 
        opcao = input("Escolha a forma de pagamento (1-3): ").strip()
 
        match opcao:
            case "1":
                forma_pagamento = "Dinheiro"
            case "2":
                forma_pagamento = "PIX"
            case "3":
                forma_pagamento = "Cartão"
            case _:
                print("Opção inválida! Escolha 1, 2 ou 3.")
    return forma_pagamento
 
 
def mostrar_resumo(nome, total, percentual, valor_desconto, valor_final, forma_pagamento):
    """Exibe o resumo final do pedido."""
    print("\n" + "=" * 30)
    print("--- RESUMO DO PEDIDO ---")
    print("=" * 30)
    print(f"Cliente: {nome}")
    print(f"Valor Original: R$ {total:.2f}")
    print(f"Desconto Aplicado: {percentual}%")
    print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
    print(f"Valor Final: R$ {valor_final:.2f}")
    print(f"Forma de Pagamento: {forma_pagamento}")
    print("=" * 30)
 
 
def main():
    nome = ler_nome()
    total_compra = 0.0
    continuar = True
 
    # Loop de repetição
    while continuar:
        mostrar_cardapio()
 
        codigo = ler_codigo()
        produto = obter_o_nome_produto(codigo)
        preco = obter_preco_produto(codigo)
        quantidade = ler_quantidade(produto)
 
        subtotal = preco * quantidade
        total_compra = total_compra + subtotal
 
        print(f"-> Adicionado: {quantidade}x {produto} = R$ {subtotal:.2f}")
        print(f"Total parcial da compra: R$ {total_compra:.2f}\n")
 
        continuar = perguntar_continuar()
 
    print(f"\nPedido encerrado! Total sem desconto: R$ {total_compra:.2f}")
 
    percentual = calcular_percentual_desconto(total_compra)
    valor_desconto = total_compra * (percentual / 100)
    valor_final = total_compra - valor_desconto
 
    forma_pagamento = escolher_pagamento()
 
    mostrar_resumo(nome, total_compra, percentual, valor_desconto, valor_final, forma_pagamento)
 
 
main()
  