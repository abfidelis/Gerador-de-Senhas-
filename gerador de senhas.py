import random
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    print("Gerador de Senha")
    comprimento = int(input("Digite o comprimento desejado da senha: "))

    if comprimento <= 0:
        print("O comprimento da senha deve ser maior que zero.")
    else:
        senha = gerar_senha(comprimento)
        print("Senha gerada:", senha)

if __name__ == "__main__":
    main()

