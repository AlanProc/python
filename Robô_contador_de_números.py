    # Define uma função para classificar o número como positivo, negativo ou zero.
def classificar_numero(numero):

    if numero < 0:
        return "negativo!"
    elif numero > 0:
        return "positivo!"
    else:
        return "zero!"

def main():
    positivos = 0  # Inicializa a contagem de números positivos
    negativos = 0  # Inicializa a contagem de números negativos
    zeros = 0      # Inicializa a contagem de zeros
    
    while True:
        numero = int(input())  # Solicita um número ao usuário
        
        if numero == 0:
            break  # Encerra o loop se o usuário digitar 0.
        
        classificacao = classificar_numero(numero)  # Chama a função classificar_numero para classificar o número
        print(classificacao)
        
        # Atualiza as contagens de números positivos, negativos e zeros
        if classificacao == "positivo!":
            positivos += 1
        elif classificacao == "negativo!":
            negativos += 1
        else:
            zeros += 1
    
    # Imprime a quantidade de números positivos e negativos inseridos
    print(f"{positivos} números positivos, {negativos} números negativos")

if __name__ == "__main__":
    main()