def verificar_triangulo():
    a = int(input("Digite o valor (inteiro) do primeiro lado do triângulo: "))
    b = int(input("Digite o valor (inteiro) do segundo lado do triângulo: "))
    c = int(input("Digite o valor (inteiro) do terceiro lado do triângulo: "))
    if (abs(b - c) < a < b + c) or (abs(a - c) < b < a + c) or (abs(a - b) < c < a + b):
        if a == b == c:
            print("O triângulo é equilátero!")
        elif (a == b != c) or (a == c != b) or (b == c != a):
            print("O triângulo é isósceles!")
        else:
            print("O triângulo é escaleno!")
    else:
        print("Não é um triângulo!")

def calcular_equacao_segundo_grau():
    a = int(input("Digite um valor para a: "))
    b = int(input("Digite um valor para b: "))
    c = int(input("Digite um valor para c: "))
    delta = b ** 2 - (4 * a * c)
    if a == 0:
        print("Esta não é uma equação de segundo grau!")
    elif delta < 0:
        print("A equação não possui raízes reais!")
    elif delta == 0:
        raizUnica = (-b) / (2 * a)
        print(f"A equação possui raiz única! \nO valor da raiz é: {raizUnica:.2f}")
    else:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        print(f"Os valores das raízes são: {x1:.2f} e {x2:.2f}")

def conferir_data():
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))
    if ano > 0 and (mes > 0 and mes <= 12):
        if mes in [4, 6, 9, 11] and dia > 30:
            print("A data não está correta!")
        elif mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
                if dia > 29:
                    print("A data não está correta!")
                else:
                    print("A data está correta!")
            elif dia > 28:
                print("A data não está correta!")
            else:
                print("A data está correta!")
        else:
            print("A data está correta!")
    else:
        print("A data não está correta!")

def verificar_tamanho_texto():
    texto = input("Digite um texto: ")
    tamanho = len(texto)
    if tamanho < 5:
        print("O texto digitado é muito pequeno.")
    elif 5 <= tamanho < 15:
        print("O texto digitado é de tamanho médio.")
    elif 15 <= tamanho < 20:
        print("O texto digitado é grande.")
    else:
        print("O texto digitado é inválido.")

def analisar_cpf():
    cpf = input("Digite o seu CPF apenas com números: ")
    if len(cpf) == 11 and cpf.isdigit():
        print("CPF válido!")
    else:
        print("CPF inválido!")

def contar_caracteres():
    texto = input("Digite um texto: ").lower()
    vogais = sum(1 for char in texto if char in 'aeiou')
    espacos = texto.count(' ')
    outros = sum(1 for char in texto if char.isalnum() and char not in 'aeiou')
    print(f"Quantidade de vogais no texto: {vogais}\nQuantidade de espaços no texto: {espacos}\nQuantidade de outros caracteres: {outros}")

while True:
    nome = input("Digite seu nome: ")
    print(f"\nOlá",nome+".")
    op = int(input("\nDigite a opção desejada: \n1) Verificar triângulo \n2) Calcular equação do segundo grau \n3) Conferir data \n4) Verificar tamanho do texto \n5) Analisar CPF \n6) Contar caracteres \n7) Sair \n"))

    if op == 1:
        verificar_triangulo()
    elif op == 2:
        calcular_equacao_segundo_grau()
    elif op == 3:
        conferir_data()
    elif op == 4:
        verificar_tamanho_texto()
    elif op == 5:
        analisar_cpf()
    elif op == 6:
        contar_caracteres()
    elif op == 7:
        print(f"Obrigado por utilizar nosso sistema.")
        break
    else:
        print(f"Erro, a opção selecionada não está disponível")
