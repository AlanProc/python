# Desafio: A Aventura do Explorador

# Entrada
quantidade_passos = int(input())

# Adicione uma condição para verificar se a quantidade de passos é positiva.
if quantidade_passos > 0:
#Utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.  
    for passos in range(1, quantidade_passos + 1):
        if passos == 1:
            print(f"Explorador: {passos} passo")
        else:
            print(f"Explorador: {passos} passos")
# Se a quantidade de passos for inválida, imprima "Nenhum passo dado na floresta."
else:
  print("Nenhum passo dado na floresta.")
