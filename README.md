# Trabalho Prático Final 
# Maisa Teixeira da Silva
# Algoritmos e Programação 

# Sistema de atendimento e pedidos de lanchonete 
O programa, realizado no Phyton, simula o atendimento de uma lanchonete. O cliente informa o nome, escolhe produtos do cardápio, define as quantidades e, ao final, escolhe a forma de pagamento. O sistema calcula o total da compra, aplica um desconto de acordo com o valor gasto e exibe um resumo completo do pedido.

As principais funcionalidades são:
- Identificação do cliente: solicita o nome e não aceita valores em branco.
- Cardápio: exibe a lista de produtos com seus códigos e preços.
- Escolha de produtos: o cliente informa o código do produto, com validação (somente códigos de 1 a 5).
- Quantidade: o cliente informa quantas unidades deseja, aceitando apenas números inteiros maiores que zero.
- Pedido com vários itens: é possível adicionar quantos produtos quiser, com exibição do subtotal do item e do total parcial a cada inserção.
- Desconto progressivo sobre o valor total da compra.
- Forma de pagamento: Dinheiro, PIX ou Cartão, com validação da opção escolhida.
- Resumo final: exibe o cliente, o valor original, o percentual e o valor do desconto, o valor final e a forma de pagamento.

Instruções necessárias para executar o programa: 
- Ter o Python 3.10 ou superior instalado na máquina
- Baixe ou clone este repositório:
 bash
   git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
- Acesse a pasta do projeto:
bash
   cd NOME-DO-REPOSITORIO
- Execute o programa:
bash
   python trabalhopratico.py

Siga as instruções exibidas no terminal: informe o nome, escolha os produtos e as quantidades, finalize o pedido e escolha a forma de pagamento.
