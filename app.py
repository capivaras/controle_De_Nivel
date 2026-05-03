from colorama import Fore, Style


# Lista com os níveis do reservatório
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

# Função para definir a cor conforme o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Função principal
def exibir_nivel(nivel):
    if 1 <= nivel <= 5:
        cor = definir_cor(nivel)
        mensagem = niveis[nivel - 1]
        print(cor + mensagem)
    else:
        print(Fore.WHITE + "Nível inválido!")

# Programa principal
try:
    nivel_atual = int(input("Informe o nível do reservatório (1 a 5): "))
    exibir_nivel(nivel_atual)
except ValueError:
    print(Fore.WHITE + "Entrada inválida! Digite um número inteiro.")

# Restaura o estilo padrão
print(Style.RESET_ALL)

