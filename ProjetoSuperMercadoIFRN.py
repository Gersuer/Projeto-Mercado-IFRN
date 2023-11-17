def titulo(linhas, texto):
    print('=' * linhas)
    print(' ' * ((linhas - len(texto)) // 2) + texto)
    print('=' * linhas)
    
def imprimir_produtos(produtos):
    print("Nº   Produto          Valor   Qnt  Total")
    total_compras = 0
    for produto in produtos:
        total_compras += produto['total']
        print(f"{produto['numero']:<4} {produto['nome']:16} {produto['valor']:<4.2f} {produto['quantidade']: 5} {produto['total']:7.2f}")
    print(f"{seta:>34}", f"{total_compras:>5.2f}")
    
produtos = []
info_produto = {"numero", "nome", "valor", "quantidade", "total"}
fila = 0
seta = "-->"

titulo(40, "Supermercado Tabajara")
def adicionar():
  nome = input("Digite o nome do produto: ")
  valor = float(input("Digite o valor do produto: "))
  quantidade = int(input("Digite a quantidade do produto: "))
  total = round((valor * quantidade), 2)
  info_produto = {
      "numero": fila,
      "nome": nome,
      "valor": valor,
      "quantidade": quantidade,
      "total": total
  }
  produtos.append(info_produto)
  print("Produto adicionado com sucesso!")
while True:
  add = input("Deseja adicionar um produto? S/N ").lower()
  if add == "s":
    fila = fila + 1
    adicionar()
  else:
    break
titulo(40, "Confirmação e Exclusão")
while True:
  if len(produtos) == 0:
    print('Não há produtos no carrinho')
    break
  deletar = input("Deseja retirar algum produto? S/N ").lower()
  index_item = -1
  print(f'O usuário decidiu deletar? {deletar}')
  if deletar != "s" or deletar != "s":
    print("Opção inválida")
  if deletar == "s":
    numero = int(input("Digite o número do produto que deseja excluir: "))
    for item in produtos:
      if item['numero'] == numero:
        index_item = produtos.index(item)
    if index_item != -1:
      del produtos[index_item]
      print("Produto excluído com sucesso!")
      index_item = -1
    else:
      print("Produto não encontrado")
  if deletar == "n":
    break
  
titulo(40, "Resumo das compras")
imprimir_produtos(produtos)


