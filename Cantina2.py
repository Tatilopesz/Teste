print("******Bem vindo a Cantina do SENAI*******")

print(" Codigo |      Descricao       |    R$"   )
print("  100   |   Cachorro - Quente  | R$ 9.00" )
print("  101   |   Cachorro - Duplo   | R$ 11.00" )
print("  102   |       X - Egg        | R$ 12.00" )
print("  103   |        X Salada      | R$ 12.00" )
print("  104   |        X- Bacon      | R$ 14.00" )
print("  105   |        X- Tudo       | R$ 17.00" )
print("  200   |   Refrigerante Lata  | R$ 5.00" )
print("  201   |       Chá Gelado     | R$ 4.00" )

total = 0
lista = []

while True:
    codigo = input("Digite o código do produto desejado: ")

    codigosValidos = ("100","101","102","103","104","105","200","201")

    while codigo not in codigosValidos:
        print("Código inválido!")
        codigo = input("Digite o código do produto desejado: ")

    if codigo == "100":
        valor = 9.00
        print(f"Você pediu um Cachorro-Quente, valor: R${valor:.2f}")
        item = "Cachorro-Quente R$ 9.00"
    elif codigo == "101":
        valor = 11.00
        print(f"Você pediu um Cachorro-Duplo, valor: R${valor:.2f}")
        item = "Cachorro - Duplo R$ 11.00"
    elif codigo == "102":
        valor = 12.00
        print(f"Você pediu um X-Egg, valor: R${valor:.2f}") 
        item = "X - Egg R$ 12.00"
    elif codigo == "103":
        valor = 12.00
        print(f"Você pediu um X-Salada, valor: R${valor:.2f}")
        item = "X - Salada R$ 12.00"
    elif codigo == "104":
        valor = 14.00
        print(f"Você pediu um X-Bacon, valor: R${valor:.2f}")
        item = "X - Bacon R$ 14.00"
    elif codigo == "105":
        valor = 17.00
        print(f"Você pediu um X-Tudo, valor: R${valor:.2f}") 
        item = "X - Tudo R$ 17.00"
    elif codigo == "200":
        valor = 5.00
        print(f"Você pediu um Refrigerante, valor: R${valor:.2f}")
        item = "Refrigerante R$ 5.00"
    elif codigo == "201":
        valor = 4.00
        print(f"Você pediu um Chá Gelado, valor: R${valor:.2f}")
        item = "Chá Gelado R$ 4.00"
    
    lista.append(item)
    
    total += valor

    opcao = input("Deseja Continuar? (S/N)").lower()
    while opcao != 's' and opcao != 'n':
        print("Opção inválida!")
        opcao = input("Deseja Continuar? (S/N)").lower()
    
    if opcao == 'n':
        break
print("\nSeu pedido foi:")
for item in lista:
  print(item)
print("------------------------------------")
print(f"Total da compra é: R${total:.2f}")
