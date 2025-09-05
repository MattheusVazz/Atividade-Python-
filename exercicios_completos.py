# Lista Completa de 69 Exercícios Python
# Importações necessárias para os exercícios
import random      # Para números aleatórios (exercício 57, 64)
import re          # Para validação de email e nome (exercício 68)
from datetime import datetime  # Para validação de data (exercício 68)

# ===== EXERCÍCIOS 1-10: ESTRUTURAS CONDICIONAIS BÁSICAS =====

def exercicio_01():
    """Exercício 1: Converter número (1-3) para seu nome por extenso"""
    # Solicita um número de 1 a 3 do usuário
    numero = int(input("Digite um número de 1 a 3: "))
    
    # Verifica qual número foi digitado e exibe o nome correspondente
    if numero == 1:
        print("um")
    elif numero == 2:
        print("dois")
    elif numero == 3:
        print("três")
    else:
        # Caso o número não esteja no range válido
        print("Número inválido!")

def exercicio_02():
    """Exercício 2: Verificar se um número é maior que 10"""
    # Recebe um número do usuário
    numero = int(input("Digite um número: "))
    
    # Compara o número com 10 e exibe o resultado
    if numero > 10:
        print("O número é maior que 10")
    else:
        print("O número não é maior que 10")

def exercicio_03():
    """Exercício 3: Converter número (1-7) para dia da semana"""
    # Solicita um número de 1 a 7 representando o dia da semana
    dia = int(input("Digite um número de 1 a 7 para o dia da semana: "))
    
    # Dicionário que mapeia números para dias da semana
    dias = {1: "Segunda-feira", 2: "Terça-feira", 3: "Quarta-feira", 
            4: "Quinta-feira", 5: "Sexta-feira", 6: "Sábado", 7: "Domingo"}
    
    # Verifica se o número está no range válido e exibe o dia correspondente
    if dia in dias:
        print(dias[dia])
    else:
        print("Número inválido!")

def exercicio_04():
    """Exercício 4: Exibir mensagem baseada na cor escolhida"""
    # Recebe uma cor do usuário e converte para minúscula
    cor = input("Digite uma cor (vermelho, verde, azul): ").lower()
    
    # Verifica a cor digitada e exibe mensagem correspondente
    if cor == "vermelho":
        print("Cor vibrante e energética!")
    elif cor == "verde":
        print("Cor da natureza!")
    elif cor == "azul":
        print("Cor calma e serena!")
    else:
        # Caso a cor não seja uma das três opções
        print("Cor não reconhecida!")

def exercicio_05():
    """Exercício 5: Verificar se dois números são ambos pares"""
    # Recebe dois números do usuário
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    # Verifica se ambos são pares usando o operador módulo (%)
    # Um número é par quando dividido por 2 tem resto 0
    if num1 % 2 == 0 and num2 % 2 == 0:
        print("Ambos os números são pares")
    else:
        print("Nem todos os números são pares")

def exercicio_06():
    """Exercício 6: Calculadora simples com as quatro operações básicas"""
    # Recebe a operação desejada do usuário
    operacao = input("Digite uma operação (+, -, *, /): ")
    # Recebe os dois números (usando float para permitir decimais)
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Realiza a operação baseada no símbolo digitado
    if operacao == "+":
        print(f"Resultado: {num1 + num2}")
    elif operacao == "-":
        print(f"Resultado: {num1 - num2}")
    elif operacao == "*":
        print(f"Resultado: {num1 * num2}")
    elif operacao == "/":
        # Verifica divisão por zero antes de calcular
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Erro: Divisão por zero!")
    else:
        print("Operação inválida!")

def exercicio_07():
    """Exercício 7: Classificar nota como Baixa, Média ou Alta"""
    # Recebe uma nota de 0 a 10
    nota = float(input("Digite uma nota de 0 a 10: "))
    
    # Classifica a nota em três categorias
    if 0 <= nota < 4:
        print("Baixa")  # Notas de 0 a 3.9
    elif 4 <= nota < 7:
        print("Média")  # Notas de 4 a 6.9
    elif 7 <= nota <= 10:
        print("Alta")   # Notas de 7 a 10
    else:
        # Nota fora do range válido
        print("Nota inválida!")

def exercicio_08():
    """Exercício 8: Verificar e exibir estado civil do usuário"""
    # Recebe o estado civil e converte para minúscula para facilitar comparação
    estado = input("Digite seu estado civil (solteiro, casado, divorciado, viúvo): ").lower()
    
    # Verifica o estado civil e exibe mensagem correspondente
    if estado == "solteiro":
        print("Você é solteiro(a)")
    elif estado == "casado":
        print("Você é casado(a)")
    elif estado == "divorciado":
        print("Você é divorciado(a)")
    elif estado == "viúvo":
        print("Você é viúvo(a)")
    else:
        print("Estado civil não reconhecido!")

def exercicio_09():
    """Exercício 9: Verificar se um número é par ou ímpar"""
    # Recebe um número do usuário
    numero = int(input("Digite um número: "))
    
    # Usa o operador módulo para verificar se é par ou ímpar
    # Se o resto da divisão por 2 for 0, o número é par
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

def exercicio_10():
    """Exercício 10: Verificar se pessoa é maior ou menor de idade"""
    # Recebe a idade do usuário
    idade = int(input("Digite sua idade: "))
    
    # Verifica se tem 18 anos ou mais (maioridade no Brasil)
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")

# ===== EXERCÍCIOS 11-20: ESTRUTURAS CONDICIONAIS INTERMEDIÁRIAS =====

def exercicio_11():
    """Exercício 11: Exibir mensagem de boas-vindas personalizada"""
    # Recebe o nome do usuário
    nome = input("Digite seu nome: ")
    
    # Exibe mensagem personalizada usando f-string para interpolação
    print(f"Olá, {nome}! Seja bem-vindo!")

def exercicio_12():
    """Exercício 12: Exibir velocidade média baseada no modo de transporte"""
    # Recebe o modo de transporte e converte para minúscula
    transporte = input("Escolha um modo de transporte (carro, bicicleta, a pé): ").lower()
    
    # Verifica o transporte e exibe a velocidade média correspondente
    if transporte == "carro":
        print("Velocidade média: 60 km/h")
    elif transporte == "bicicleta":
        print("Velocidade média: 15 km/h")
    elif transporte == "a pé":
        print("Velocidade média: 5 km/h")
    else:
        print("Modo de transporte não reconhecido!")

def exercicio_13():
    """Exercício 13: Determinar estação do ano baseada no mês (Hemisfério Sul)"""
    # Recebe o número do mês (1-12)
    mes = int(input("Digite um mês (1-12): "))
    
    # Determina a estação baseada no mês (padrão brasileiro - Hemisfério Sul)
    if mes in [12, 1, 2]:  # Dezembro, Janeiro, Fevereiro
        print("Verão")
    elif mes in [3, 4, 5]:  # Março, Abril, Maio
        print("Outono")
    elif mes in [6, 7, 8]:  # Junho, Julho, Agosto
        print("Inverno")
    elif mes in [9, 10, 11]:  # Setembro, Outubro, Novembro
        print("Primavera")
    else:
        print("Mês inválido!")

def exercicio_14():
    """Exercício 14: Verificar se a soma de dois números é maior que 100"""
    # Recebe dois números do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Calcula a soma dos números
    soma = num1 + num2
    
    # Verifica se a soma é maior que 100 e exibe o resultado
    if soma > 100:
        print(f"A soma ({soma}) é maior que 100")
    else:
        print(f"A soma ({soma}) não é maior que 100")

def exercicio_15():
    """Exercício 15: Verificar se pessoa é adolescente (13-17 anos)"""
    # Recebe a idade do usuário
    idade = int(input("Digite sua idade: "))
    
    # Verifica se a idade está na faixa de adolescente (13 a 17 anos)
    if 13 <= idade <= 17:
        print("Você é adolescente")
    else:
        print("Você não é adolescente")

def exercicio_16():
    """Exercício 16: Exibir preço do combustível baseado no tipo"""
    # Recebe o tipo de combustível e converte para minúscula
    combustivel = input("Digite o tipo de combustível (gasolina, etanol, diesel): ").lower()
    
    # Verifica o tipo e exibe o preço correspondente por litro
    if combustivel == "gasolina":
        print("Preço: R$ 5.50 por litro")
    elif combustivel == "etanol":
        print("Preço: R$ 3.80 por litro")
    elif combustivel == "diesel":
        print("Preço: R$ 4.20 por litro")
    else:
        print("Tipo de combustível não reconhecido!")

def exercicio_17():
    """Exercício 17: Realizar todas as operações matemáticas básicas"""
    # Recebe dois números do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Realiza e exibe todas as quatro operações básicas
    print(f"Soma: {num1 + num2}")
    print(f"Subtração: {num1 - num2}")
    print(f"Multiplicação: {num1 * num2}")
    
    # Verifica divisão por zero antes de dividir
    if num2 != 0:
        print(f"Divisão: {num1 / num2}")
    else:
        print("Divisão: Não é possível dividir por zero")

def exercicio_18():
    """Exercício 18: Verificar se três números são todos positivos"""
    # Recebe três números do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    
    # Verifica se todos os três números são positivos (maior que zero)
    # Usa o operador 'and' para verificar todas as condições simultaneamente
    if num1 > 0 and num2 > 0 and num3 > 0:
        print("Todos os números são positivos")
    else:
        print("Nem todos os números são positivos")

def exercicio_19():
    """Exercício 19: Verificar se a fruta digitada é uma maçã"""
    # Recebe o nome da fruta e converte para minúscula
    fruta = input("Digite o nome de uma fruta: ").lower()
    
    # Verifica se é maçã (aceita com e sem acento para flexibilidade)
    if fruta == "maçã" or fruta == "maca":
        print("É uma maçã!")
    else:
        print("Não é uma maçã")

def exercicio_20():
    """Exercício 20: Converter temperatura de Celsius para Fahrenheit"""
    # Recebe a temperatura em graus Celsius
    celsius = float(input("Digite a temperatura em Celsius: "))
    
    # Aplica a fórmula de conversão: F = (C * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    
    # Exibe o resultado da conversão
    print(f"{celsius}°C = {fahrenheit}°F")

# ===== EXERCÍCIOS 21-30: ESTRUTURAS CONDICIONAIS AVANÇADAS =====

def exercicio_21():
    """Exercício 21: Comparar número com 10 (maior, menor ou igual)"""
    # Recebe um número do usuário
    numero = float(input("Digite um número: "))
    
    # Compara o número com 10 usando estrutura if-elif-else
    if numero > 10:
        print("O número é maior que 10")
    elif numero < 10:
        print("O número é menor que 10")
    else:
        # Se não é maior nem menor, então é igual
        print("O número é igual a 10")

def exercicio_22():
    """Exercício 22: Verificar se o primeiro número é maior que o segundo"""
    # Recebe dois números do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Compara os dois números
    if num1 > num2:
        print("O primeiro número é maior que o segundo")
    else:
        # Inclui casos onde são iguais ou o segundo é maior
        print("O primeiro número não é maior que o segundo")

def exercicio_23():
    """Exercício 23: Verificar se a palavra digitada é 'Python'"""
    # Recebe uma palavra do usuário
    palavra = input("Digite uma palavra: ")
    
    # Compara com 'python' em minúscula para ignorar diferenças de capitalização
    if palavra.lower() == "python":
        print("A palavra é Python!")
    else:
        print("A palavra não é Python")

def exercicio_24():
    """Exercício 24: Verificar se a cidade é a capital do Brasil"""
    # Recebe o nome da cidade e converte para minúscula
    cidade = input("Digite o nome de uma cidade: ").lower()
    
    # Verifica se é Brasília (aceita com e sem acento)
    if cidade == "brasília" or cidade == "brasilia":
        print("É a capital do Brasil!")
    else:
        print("Não é a capital do Brasil")

def exercicio_25():
    """Exercício 25: Verificar se número está no intervalo de 10 a 15"""
    # Recebe um número de 0 a 20
    numero = int(input("Digite um número de 0 a 20: "))
    
    # Verifica se o número está no intervalo [10, 15] (inclusive)
    # Usa operador de comparação em cadeia para verificar o intervalo
    if 10 <= numero <= 15:
        print("O número está entre 10 e 15")
    else:
        print("O número não está entre 10 e 15")

def exercicio_26():
    """Exercício 26: Verificar se ambos os números são múltiplos de 5"""
    # Recebe dois números do usuário
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    # Verifica se ambos são múltiplos de 5 (resto da divisão por 5 igual a 0)
    if num1 % 5 == 0 and num2 % 5 == 0:
        print("Ambos os números são múltiplos de 5")
    else:
        print("Nem todos os números são múltiplos de 5")

def exercicio_27():
    """Exercício 27: Encontrar o maior de três números"""
    # Recebe três números do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    
    # Usa a função built-in max() para encontrar o maior valor
    maior = max(num1, num2, num3)
    print(f"O maior número é: {maior}")

def exercicio_28():
    """Exercício 28: Verificar se uma palavra tem mais de 5 letras"""
    # Recebe uma palavra do usuário
    palavra = input("Digite uma palavra: ")
    
    # Usa len() para contar o número de caracteres na palavra
    if len(palavra) > 5:
        print("A palavra tem mais de 5 letras")
    else:
        print("A palavra não tem mais de 5 letras")

def exercicio_29():
    """Exercício 29: Verificar se um número é múltiplo de 3"""
    # Recebe um número do usuário
    numero = int(input("Digite um número: "))
    
    # Verifica se é múltiplo de 3 (resto da divisão por 3 igual a 0)
    if numero % 3 == 0:
        print("O número é múltiplo de 3")
    else:
        print("O número não é múltiplo de 3")

def exercicio_30():
    """Exercício 30: Verificar se pessoa pode votar (16+ anos no Brasil)"""
    # Recebe a idade do usuário
    idade = int(input("Digite sua idade: "))
    
    # No Brasil, o voto é facultativo a partir dos 16 anos e obrigatório dos 18-70
    if idade >= 16:
        print("Você pode votar")
    else:
        print("Você não pode votar")

# ===== EXERCÍCIOS 31-40: ESTRUTURAS CONDICIONAIS FINAIS =====

def exercicio_31():
    """Exercício 31: Verificar se número de 1 a 5 é igual a 3"""
    # Recebe um número de 1 a 5
    numero = int(input("Digite um número de 1 a 5: "))
    
    # Verifica especificamente se o número é igual a 3
    if numero == 3:
        print("O número é igual a 3")
    else:
        print("O número não é igual a 3")

def exercicio_33():
    """Exercício 33: Calcular desconto de 10% em um produto"""
    # Recebe o valor do produto
    valor = float(input("Digite o valor do produto: R$ "))
    
    # Calcula 10% de desconto
    desconto = valor * 0.10
    # Subtrai o desconto do valor original
    valor_final = valor - desconto
    
    # Exibe os valores formatados com 2 casas decimais
    print(f"Valor original: R$ {valor:.2f}")
    print(f"Desconto (10%): R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")

def exercicio_34():
    """Exercício 34: Classificar número como positivo, negativo ou zero"""
    # Recebe um número do usuário
    numero = float(input("Digite um número: "))
    
    # Classifica o número em três categorias possíveis
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        # Se não é maior nem menor que zero, então é zero
        print("Zero")

def exercicio_35():
    """Exercício 35: Verificar se a multiplicação de dois números é igual a 20"""
    # Recebe dois números do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Calcula a multiplicação dos números
    multiplicacao = num1 * num2
    
    # Verifica se o resultado é exatamente 20
    if multiplicacao == 20:
        print("A multiplicação é igual a 20")
    else:
        print(f"A multiplicação é {multiplicacao}, não é igual a 20")

def exercicio_36():
    """Exercício 36: Converter número (1-12) para nome do mês"""
    # Recebe um número de 1 a 12 representando o mês
    numero = int(input("Digite um número de 1 a 12: "))
    
    # Dicionário que mapeia números para nomes dos meses
    meses = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }
    
    # Verifica se o número está no range válido e exibe o mês correspondente
    if numero in meses:
        print(meses[numero])
    else:
        print("Número inválido!")

def exercicio_37():
    """Exercício 37: Verificar se número é múltiplo de 2 ou de 5"""
    # Recebe um número do usuário
    numero = int(input("Digite um número: "))
    
    # Verifica se é múltiplo de 2 OU de 5 (operador 'or')
    # Um número é múltiplo quando o resto da divisão é zero
    if numero % 2 == 0 or numero % 5 == 0:
        print("O número é múltiplo de 2 ou de 5")
    else:
        print("O número não é múltiplo de 2 nem de 5")

def exercicio_38():
    """Exercício 38: Verificar se altura é maior que 1,75m"""
    # Recebe a altura em metros
    altura = float(input("Digite sua altura em metros: "))
    
    # Compara a altura com 1.75 metros
    if altura > 1.75:
        print("Sua altura é maior que 1,75m")
    else:
        print("Sua altura não é maior que 1,75m")

def exercicio_39():
    """Exercício 39: Verificar se a senha digitada é '1234'"""
    # Recebe a senha do usuário
    senha = input("Digite a senha: ")
    
    # Compara com a senha predefinida "1234"
    if senha == "1234":
        print("Senha correta!")
    else:
        print("Senha incorreta!")

def exercicio_40():
    """Exercício 40: Verificar se três números são todos iguais"""
    # Recebe três números do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    
    # Usa comparação em cadeia para verificar se todos são iguais
    if num1 == num2 == num3:
        print("Todos os números são iguais")
    else:
        print("Os números não são todos iguais")

# ===== EXERCÍCIOS 41-50: ESTRUTURAS DE REPETIÇÃO (FOR) =====

def exercicio_41():
    """Exercício 41: Exibir números de 1 até o número informado"""
    # Recebe um número inteiro positivo
    numero = int(input("Digite um número inteiro positivo: "))
    
    # Verifica se o número é positivo antes de executar o loop
    if numero > 0:
        # Loop for que vai de 1 até o número (inclusive)
        # range(1, numero + 1) gera uma sequência de 1 até numero
        for i in range(1, numero + 1):
            print(i)
    else:
        print("Por favor, digite um número positivo")

def exercicio_42():
    """Exercício 42: Somar 5 números inteiros fornecidos pelo usuário"""
    # Inicializa a variável acumuladora
    soma = 0
    
    # Loop for que executa 5 vezes (range(5) = 0, 1, 2, 3, 4)
    for i in range(5):
        # Solicita o número (i+1 para mostrar 1º, 2º, etc.)
        numero = int(input(f"Digite o {i+1}º número: "))
        # Adiciona o número à soma (operação de acumulação)
        soma += numero
    
    # Exibe o resultado final
    print(f"A soma dos números é: {soma}")

def exercicio_43():
    """Exercício 43: Repetir uma mensagem N vezes usando for"""
    # Recebe o número de repetições desejadas
    vezes = int(input("Quantas vezes deseja exibir a mensagem? "))
    # Recebe a mensagem a ser repetida
    mensagem = input("Digite a mensagem: ")
    
    # Loop for que executa 'vezes' repetições
    for i in range(vezes):
        # Exibe a mensagem numerada (i+1 para começar do 1)
        print(f"{i+1}. {mensagem}")

def exercicio_44():
    """Exercício 44: Receber 10 números e exibir apenas os pares"""
    print("Digite 10 números:")
    
    # Loop for para receber exatamente 10 números
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número: "))
        
        # Verifica se o número é par usando o operador módulo
        if numero % 2 == 0:
            print(f"Número par: {numero}")

def exercicio_45():
    """Exercício 45: Encontrar o maior de 5 números"""
    # Inicializa com o menor valor possível (infinito negativo)
    maior = float('-inf')
    
    # Loop para receber 5 números
    for i in range(5):
        numero = float(input(f"Digite o {i+1}º número: "))
        
        # Atualiza o maior valor se o número atual for maior
        if numero > maior:
            maior = numero
    
    print(f"O maior número é: {maior}")

def exercicio_46():
    """Exercício 46: Calcular a média de 10 números"""
    # Inicializa a variável acumuladora para a soma
    soma = 0
    
    # Loop para receber 10 números
    for i in range(10):
        numero = float(input(f"Digite o {i+1}º número: "))
        # Acumula os valores na soma
        soma += numero
    
    # Calcula a média dividindo a soma pela quantidade de números
    media = soma / 10
    print(f"A média dos números é: {media:.2f}")

def exercicio_47():
    """Exercício 47: Exibir a tabuada de um número de 1 a 10"""
    # Recebe o número para calcular a tabuada
    numero = int(input("Digite um número para ver sua tabuada: "))
    
    print(f"\nTabuada do {numero}:")
    
    # Loop de 1 a 10 para gerar a tabuada completa
    # range(1, 11) gera os números de 1 a 10
    for i in range(1, 11):
        # Calcula e exibe cada linha da tabuada
        print(f"{numero} x {i} = {numero * i}")

def exercicio_48():
    """Exercício 48: Exibir cada letra de uma palavra em linha separada"""
    # Recebe uma palavra do usuário
    palavra = input("Digite uma palavra: ")
    
    print("Letras da palavra:")
    
    # enumerate() retorna tanto o índice quanto o valor
    # enumerate(palavra, 1) começa a contagem do 1 em vez de 0
    for i, letra in enumerate(palavra, 1):
        print(f"{i}. {letra}")

def exercicio_49():
    """Exercício 49: Contar quantos de 7 números são maiores que 10"""
    # Inicializa contador para números maiores que 10
    contador = 0
    
    # Loop para receber 7 números
    for i in range(7):
        numero = float(input(f"Digite o {i+1}º número: "))
        
        # Verifica se o número é maior que 10
        if numero > 10:
            contador += 1  # Incrementa o contador
    
    print(f"Quantidade de números maiores que 10: {contador}")

def exercicio_50():
    """Exercício 50: Exibir números de forma decrescente até 1"""
    # Recebe um número do usuário
    numero = int(input("Digite um número: "))
    
    print(f"Números de {numero} até 1:")
    
    # range(numero, 0, -1): começa em 'numero', vai até 1 (0 exclusivo), decrementando de 1
    # O terceiro parâmetro (-1) define o passo como decrescente
    for i in range(numero, 0, -1):
        print(i)

# ===== EXERCÍCIOS 51-60: ESTRUTURAS DE REPETIÇÃO (WHILE) =====

def exercicio_51():
    """Exercício 51: Somar números até que o usuário digite 0"""
    # Inicializa a variável acumuladora
    soma = 0
    
    print("Digite números para somar (digite 0 para parar):")
    
    # Loop infinito que só para quando o usuário digitar 0
    while True:
        numero = float(input("Digite um número: "))
        
        # Condição de parada: se digitar 0, sai do loop
        if numero == 0:
            break  # break interrompe o loop while
        
        # Acumula o número na soma
        soma += numero
    
    print(f"A soma total é: {soma}")

def exercicio_52():
    """Exercício 52: Pedir senha até que o usuário acerte"""
    # Define a senha correta
    senha_correta = "1234"
    
    # Loop que continua até o usuário acertar a senha
    while True:
        senha = input("Digite a senha: ")
        
        # Verifica se a senha está correta
        if senha == senha_correta:
            print("Senha correta! Acesso liberado.")
            break  # Sai do loop quando acerta
        else:
            print("Senha incorreta! Tente novamente.")

def exercicio_53():
    """Exercício 53: Fazer contagem regressiva até 1"""
    # Recebe o número inicial para a contagem
    numero = int(input("Digite um número para contagem regressiva: "))
    
    print("Contagem regressiva:")
    
    # Loop while que executa enquanto numero for maior ou igual a 1
    while numero >= 1:
        print(numero)
        numero -= 1  # Decrementa o número a cada iteração
    
    print("Fim!")

def exercicio_54():
    """Exercício 54: Coletar números até que um negativo seja digitado"""
    print("Digite números (número negativo para parar):")
    
    # Lista para armazenar os números digitados
    numeros = []
    
    # Loop infinito com condição de parada interna
    while True:
        numero = float(input("Digite um número: "))
        
        # Se o número for negativo, interrompe o loop
        if numero < 0:
            print("Número negativo inserido. Parando...")
            break
        
        # Adiciona o número à lista se for positivo ou zero
        numeros.append(numero)
    
    print(f"Números inseridos: {numeros}")

def exercicio_55():
    """Exercício 55: Solicitar número até que seja maior que 100"""
    # Loop que continua até o usuário digitar um número > 100
    while True:
        numero = int(input("Digite um número maior que 100: "))
        
        # Verifica se o número atende ao critério
        if numero > 100:
            print(f"Perfeito! Você digitou {numero}")
            break  # Sai do loop quando a condição é atendida
        else:
            print("O número deve ser maior que 100. Tente novamente.")

def exercicio_56():
    """Exercício 56: Exibir mensagem N vezes usando while"""
    # Recebe o número de repetições
    vezes = int(input("Quantas vezes quer exibir a mensagem? "))
    # Recebe a mensagem a ser repetida
    mensagem = input("Digite a mensagem: ")
    
    # Inicializa o contador
    contador = 0
    
    # Loop while com condição baseada no contador
    while contador < vezes:
        print(f"{contador + 1}. {mensagem}")
        contador += 1  # Incrementa o contador a cada iteração

def exercicio_57():
    """Exercício 57: Jogo de adivinhação de número de 1 a 10"""
    # Gera um número aleatório entre 1 e 10
    numero_secreto = random.randint(1, 10)
    
    print("Tente adivinhar o número secreto entre 1 e 10!")
    
    # Loop que continua até o usuário acertar
    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            
            # Verifica se o palpite está correto
            if palpite == numero_secreto:
                print("Parabéns! Você acertou!")
                break  # Sai do loop quando acerta
            else:
                print("Errou! Tente novamente.")
        except ValueError:
            # Trata erro caso o usuário digite algo que não seja número
            print("Digite um número válido!")

def exercicio_58():
    """Exercício 58: Coletar palavras até que o usuário digite 'sair'"""
    # Lista para armazenar as palavras
    palavras = []
    
    print("Digite palavras (digite 'sair' para parar):")
    
    # Loop infinito com condição de parada
    while True:
        palavra = input("Digite uma palavra: ")
        
        # Verifica se o usuário quer sair (ignora maiúscula/minúscula)
        if palavra.lower() == "sair":
            print("Saindo...")
            break
        
        # Adiciona a palavra à lista
        palavras.append(palavra)
    
    print(f"Palavras digitadas: {palavras}")

def exercicio_59():
    """Exercício 59: Pedir números até que o primeiro seja maior que o segundo"""
    # Loop que continua até a condição ser atendida
    while True:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Verifica se o primeiro é maior que o segundo
        if num1 > num2:
            print(f"Perfeito! {num1} é maior que {num2}")
            break  # Sai do loop quando a condição é atendida
        else:
            print("O primeiro número deve ser maior que o segundo. Tente novamente.")

def exercicio_60():
    """Exercício 60: Exibir todos os divisores de um número usando while"""
    # Recebe o número para encontrar os divisores
    numero = int(input("Digite um número para ver seus divisores: "))
    
    print(f"Divisores de {numero}:")
    
    # Inicializa o divisor começando por 1
    divisor = 1
    
    # Loop que testa todos os números de 1 até o próprio número
    while divisor <= numero:
        # Se a divisão é exata (resto = 0), então é um divisor
        if numero % divisor == 0:
            print(divisor)
        
        divisor += 1  # Incrementa para testar o próximo número

# ===== EXERCÍCIOS 61-65: LISTAS BÁSICAS =====

def exercicio_61():
    """Exercício 61: Criar lista de 1 a 5 e imprimir cada número"""
    # Cria uma lista com os números de 1 a 5
    numeros = [1, 2, 3, 4, 5]
    
    print("Números da lista:")
    
    # Itera sobre cada elemento da lista
    # O for percorre diretamente os valores, não os índices
    for numero in numeros:
        print(numero)

def exercicio_62():
    """Exercício 62: Solicitar 3 nomes e armazenar em lista"""
    # Inicializa uma lista vazia
    nomes = []
    
    print("Digite 3 nomes:")
    
    # Loop para coletar exatamente 3 nomes
    for i in range(3):
        nome = input(f"Digite o {i+1}º nome: ")
        # append() adiciona o elemento ao final da lista
        nomes.append(nome)
    
    # Exibe a lista completa
    print(f"\nLista completa de nomes: {nomes}")

def exercicio_63():
    """Exercício 63: Coletar 5 números em lista e calcular soma"""
    # Inicializa lista vazia para os números
    numeros = []
    
    print("Digite 5 números:")
    
    # Loop para coletar 5 números
    for i in range(5):
        numero = float(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)  # Adiciona à lista
    
    # Usa a função built-in sum() para somar todos os elementos
    soma = sum(numeros)
    
    # Exibe a lista e o resultado da soma
    print(f"Lista de números: {numeros}")
    print(f"Soma de todos os números: {soma}")

def exercicio_64():
    """Exercício 64: Criar lista com números aleatórios e filtrar múltiplos de 3"""
    # Cria lista com 10 números aleatórios entre 1 e 50
    # List comprehension: [expressão for item in range()]
    # O '_' indica que não usamos a variável do loop
    numeros = [random.randint(1, 50) for _ in range(10)]
    
    print(f"Lista original: {numeros}")
    
    # Inicializa lista para armazenar os múltiplos de 3
    multiplos_de_3 = []
    
    # Percorre cada número da lista original
    for numero in numeros:
        # Verifica se é múltiplo de 3 (resto da divisão = 0)
        if numero % 3 == 0:
            multiplos_de_3.append(numero)
    
    print(f"Múltiplos de 3: {multiplos_de_3}")

def exercicio_65():
    """Exercício 65: Coletar 5 números e encontrar maior e menor"""
    # Lista para armazenar os números
    numeros = []
    
    print("Digite 5 números:")
    
    # Coleta 5 números do usuário
    for i in range(5):
        numero = float(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
    
    # Usa funções built-in para encontrar maior e menor
    maior = max(numeros)  # Retorna o maior valor da lista
    menor = min(numeros)  # Retorna o menor valor da lista
    
    # Exibe os resultados
    print(f"Lista de números: {numeros}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")

# ===== EXERCÍCIO 66: SISTEMA DE CADASTRO BÁSICO =====

def exercicio_66():
    """Exercício 66: Sistema de cadastro básico com CRUD de nomes"""
    # Lista para armazenar os nomes cadastrados
    nomes_cadastrados = []
    
    def cadastrar_nome():
        """Função para cadastrar um novo nome"""
        nome = input("Digite o nome para cadastrar: ")
        # strip() remove espaços em branco no início e fim
        if nome.strip():
            nomes_cadastrados.append(nome)
            print(f"✓ Nome '{nome}' cadastrado com sucesso!")
        else:
            print("✗ Nome inválido! Digite um nome válido.")

    def atualizar_nome():
        if not nomes_cadastrados:
            print("✗ Não há nomes cadastrados para atualizar.")
            return
        
        listar_nomes()
        try:
            indice = int(input("Digite o número do nome que deseja atualizar: ")) - 1
            if 0 <= indice < len(nomes_cadastrados):
                nome_antigo = nomes_cadastrados[indice]
                nome_novo = input("Digite o novo nome: ")
                if nome_novo.strip():
                    nomes_cadastrados[indice] = nome_novo
                    print(f"✓ Nome '{nome_antigo}' atualizado para '{nome_novo}' com sucesso!")
                else:
                    print("✗ Nome inválido! Atualização cancelada.")
            else:
                print("✗ Número inválido!")
        except ValueError:
            print("✗ Digite um número válido!")

    def excluir_nome():
        if not nomes_cadastrados:
            print("✗ Não há nomes cadastrados para excluir.")
            return
        
        listar_nomes()
        try:
            indice = int(input("Digite o número do nome que deseja excluir: ")) - 1
            if 0 <= indice < len(nomes_cadastrados):
                nome_excluido = nomes_cadastrados.pop(indice)
                print(f"✓ Nome '{nome_excluido}' excluído com sucesso!")
            else:
                print("✗ Número inválido!")
        except ValueError:
            print("✗ Digite um número válido!")

    def listar_nomes():
        if not nomes_cadastrados:
            print("✗ Não há nomes cadastrados.")
        else:
            print("\n=== NOMES CADASTRADOS ===")
            for i, nome in enumerate(nomes_cadastrados, 1):
                print(f"{i}. {nome}")
            print("=" * 25)

    def exibir_menu():
        print("\n=== SISTEMA DE CADASTRO ===")
        print("1 - Cadastrar nome")
        print("2 - Atualizar nome")
        print("3 - Excluir nome")
        print("4 - Listar todos os cadastrados")
        print("0 - Sair")
        print("=" * 27)
    
    print("Bem-vindo ao Sistema de Cadastro!")
    
    while True:
        exibir_menu()
        
        try:
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                cadastrar_nome()
                continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
                if continuar != 's':
                    print("Obrigado por usar o sistema!")
                    break
                    
            elif opcao == 2:
                atualizar_nome()
                continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
                if continuar != 's':
                    print("Obrigado por usar o sistema!")
                    break
                    
            elif opcao == 3:
                excluir_nome()
                continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
                if continuar != 's':
                    print("Obrigado por usar o sistema!")
                    break
                    
            elif opcao == 4:
                listar_nomes()
                continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
                if continuar != 's':
                    print("Obrigado por usar o sistema!")
                    break
                    
            elif opcao == 0:
                print("Obrigado por usar o sistema!")
                break
                
            else:
                print("✗ Opção inválida! Tente novamente.")
                
        except ValueError:
            print("✗ Digite um número válido!")

# ===== EXERCÍCIO 67: JOGO DA VELHA BÁSICO =====

def exercicio_67():
    """Exercício 67: Jogo da velha básico no terminal"""
    
    def criar_tabuleiro():
        """Cria um tabuleiro 3x3 vazio para o jogo da velha"""
        # List comprehension aninhada: cria matriz 3x3 preenchida com espaços
        return [[' ' for _ in range(3)] for _ in range(3)]

    def exibir_tabuleiro(tabuleiro):
        print("\n   0   1   2")
        for i, linha in enumerate(tabuleiro):
            print(f"{i}  {linha[0]} | {linha[1]} | {linha[2]} ")
            if i < 2:
                print("  -----------")

    def fazer_jogada(tabuleiro, linha, coluna, jogador):
        if 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = jogador
            return True
        return False

    def verificar_vitoria(tabuleiro, jogador):
        for linha in tabuleiro:
            if all(celula == jogador for celula in linha):
                return True
        
        for col in range(3):
            if all(tabuleiro[linha][col] == jogador for linha in range(3)):
                return True
        
        if all(tabuleiro[i][i] == jogador for i in range(3)):
            return True
        
        if all(tabuleiro[i][2-i] == jogador for i in range(3)):
            return True
        
        return False

    def tabuleiro_cheio(tabuleiro):
        return all(celula != ' ' for linha in tabuleiro for celula in linha)
    
    print("=== JOGO DA VELHA ===")
    print("Jogador 1: X")
    print("Jogador 2: O")
    print("Coordenadas: linha coluna (ex: 1 2)")
    
    tabuleiro = criar_tabuleiro()
    jogador_atual = 'X'
    jogador_numero = 1
    
    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"\nVez do Jogador {jogador_numero} ({jogador_atual})")
        
        try:
            entrada = input("Digite linha e coluna (ex: 1 2): ").split()
            if len(entrada) != 2:
                print("Digite exatamente duas coordenadas!")
                continue
                
            linha, coluna = int(entrada[0]), int(entrada[1])
            
            if fazer_jogada(tabuleiro, linha, coluna, jogador_atual):
                if verificar_vitoria(tabuleiro, jogador_atual):
                    exibir_tabuleiro(tabuleiro)
                    print(f"\n🎉 Parabéns! Jogador {jogador_numero} ({jogador_atual}) venceu!")
                    break
                elif tabuleiro_cheio(tabuleiro):
                    exibir_tabuleiro(tabuleiro)
                    print("\n🤝 Empate! O tabuleiro está cheio.")
                    break
                else:
                    jogador_atual = 'O' if jogador_atual == 'X' else 'X'
                    jogador_numero = 2 if jogador_numero == 1 else 1
            else:
                print("Posição inválida! Tente novamente.")
                
        except (ValueError, IndexError):
            print("Entrada inválida! Digite dois números entre 0 e 2.")

# ===== EXERCÍCIO 68: SISTEMA DE CADASTRO AVANÇADO =====

def exercicio_68():
    """Exercício 68: Sistema de cadastro de alunos avançado com classes e validação"""
    
    class Aluno:
        """Classe para representar um aluno com dados pessoais e matrícula única"""
        # Set para armazenar matrículas já utilizadas (evita duplicação)
        matriculas_usadas = set()
        
        def __init__(self, nome, email, data_nascimento, matricula=None):
            self.nome = nome
            self.email = email
            self.data_nascimento = data_nascimento
            self.matricula = matricula if matricula else self._gerar_matricula()
            
        def _gerar_matricula(self):
            while True:
                matricula = f"ALU{random.randint(1000, 9999)}"
                if matricula not in Aluno.matriculas_usadas:
                    Aluno.matriculas_usadas.add(matricula)
                    return matricula
        
        def __str__(self):
            return f"""
=== DADOS DO ALUNO ===
Nome: {self.nome}
E-mail: {self.email}
Data de Nascimento: {self.data_nascimento}
Matrícula: {self.matricula}
=====================
"""

    def validar_nome(nome):
        if not nome or not nome.strip():
            return False, "Nome não pode estar vazio"
        
        nome = nome.strip()
        if len(nome) < 2:
            return False, "Nome deve ter pelo menos 2 caracteres"
        
        if not re.match("^[a-zA-ZÀ-ÿ\s]+$", nome):
            return False, "Nome deve conter apenas letras e espaços"
        
        return True, "Nome válido"

    def validar_email(email):
        if not email or not email.strip():
            return False, "E-mail não pode estar vazio"
        
        email = email.strip()
        padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(padrao_email, email):
            return False, "E-mail deve estar no formato correto (exemplo@email.com)"
        
        return True, "E-mail válido"

    def validar_data_nascimento(data):
        if not data or not data.strip():
            return False, "Data de nascimento não pode estar vazia"
        
        data = data.strip()
        try:
            data_obj = datetime.strptime(data, "%d/%m/%Y")
            
            if data_obj > datetime.now():
                return False, "Data de nascimento não pode ser futura"
            
            idade_anos = (datetime.now() - data_obj).days / 365.25
            if idade_anos > 120:
                return False, "Data de nascimento inválida (idade muito alta)"
            
            return True, "Data de nascimento válida"
        
        except ValueError:
            return False, "Data deve estar no formato DD/MM/AAAA"

    def validar_matricula(matricula, alunos):
        if not matricula or not matricula.strip():
            return False, "Matrícula não pode estar vazia"
        
        matricula = matricula.strip().upper()
        
        for aluno in alunos:
            if aluno.matricula == matricula:
                return True, "Matrícula válida"
        
        return False, "Matrícula não encontrada no sistema"

    alunos = []

    def cadastrar_aluno():
        print("\n=== CADASTRAR ALUNO ===")
        
        while True:
            nome = input("Digite o nome do aluno: ")
            valido, mensagem = validar_nome(nome)
            if valido:
                nome = nome.strip()
                break
            else:
                print(f"✗ {mensagem}")
        
        while True:
            email = input("Digite o e-mail do aluno: ")
            valido, mensagem = validar_email(email)
            if valido:
                email = email.strip()
                break
            else:
                print(f"✗ {mensagem}")
        
        while True:
            data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
            valido, mensagem = validar_data_nascimento(data_nascimento)
            if valido:
                data_nascimento = data_nascimento.strip()
                break
            else:
                print(f"✗ {mensagem}")
        
        novo_aluno = Aluno(nome, email, data_nascimento)
        alunos.append(novo_aluno)
        print(f"✓ Aluno '{nome}' cadastrado com sucesso!")
        print(f"Matrícula gerada: {novo_aluno.matricula}")

    def atualizar_aluno():
        if not alunos:
            print("✗ Não há alunos cadastrados.")
            return
        
        print("\n=== ATUALIZAR ALUNO ===")
        
        while True:
            matricula = input("Digite a matrícula do aluno: ")
            valido, mensagem = validar_matricula(matricula, alunos)
            if valido:
                matricula = matricula.strip().upper()
                break
            else:
                print(f"✗ {mensagem}")
        
        aluno = next(a for a in alunos if a.matricula == matricula)
        
        print(f"\nAluno encontrado: {aluno.nome}")
        print("Qual dado deseja atualizar?")
        print("1 - Nome")
        print("2 - E-mail")
        print("3 - Data de nascimento")
        
        try:
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                while True:
                    novo_nome = input("Digite o novo nome: ")
                    valido, mensagem = validar_nome(novo_nome)
                    if valido:
                        aluno.nome = novo_nome.strip()
                        print("✓ Nome atualizado com sucesso!")
                        break
                    else:
                        print(f"✗ {mensagem}")
            
            elif opcao == 2:
                while True:
                    novo_email = input("Digite o novo e-mail: ")
                    valido, mensagem = validar_email(novo_email)
                    if valido:
                        aluno.email = novo_email.strip()
                        print("✓ E-mail atualizado com sucesso!")
                        break
                    else:
                        print(f"✗ {mensagem}")
            
            elif opcao == 3:
                while True:
                    nova_data = input("Digite a nova data de nascimento (DD/MM/AAAA): ")
                    valido, mensagem = validar_data_nascimento(nova_data)
                    if valido:
                        aluno.data_nascimento = nova_data.strip()
                        print("✓ Data de nascimento atualizada com sucesso!")
                        break
                    else:
                        print(f"✗ {mensagem}")
            
            else:
                print("✗ Opção inválida!")
                
        except ValueError:
            print("✗ Digite um número válido!")

    def remover_aluno():
        if not alunos:
            print("✗ Não há alunos cadastrados.")
            return
        
        print("\n=== REMOVER ALUNO ===")
        
        while True:
            matricula = input("Digite a matrícula do aluno a ser removido: ")
            valido, mensagem = validar_matricula(matricula, alunos)
            if valido:
                matricula = matricula.strip().upper()
                break
            else:
                print(f"✗ {mensagem}")
        
        for i, aluno in enumerate(alunos):
            if aluno.matricula == matricula:
                nome_removido = aluno.nome
                alunos.pop(i)
                Aluno.matriculas_usadas.discard(matricula)
                print(f"✓ Aluno '{nome_removido}' removido com sucesso!")
                break

    def listar_alunos():
        if not alunos:
            print("✗ Não há alunos cadastrados.")
        else:
            print("\n=== ALUNOS CADASTRADOS ===")
            for i, aluno in enumerate(alunos, 1):
                print(f"{i}.")
                print(aluno)

    def buscar_aluno_por_matricula():
        if not alunos:
            print("✗ Não há alunos cadastrados.")
            return
        
        print("\n=== BUSCAR ALUNO ===")
        
        while True:
            matricula = input("Digite a matrícula do aluno: ")
            valido, mensagem = validar_matricula(matricula, alunos)
            if valido:
                matricula = matricula.strip().upper()
                break
            else:
                print(f"✗ {mensagem}")
        
        aluno = next(a for a in alunos if a.matricula == matricula)
        print(aluno)

    def exibir_menu():
        print("\n=== SISTEMA DE CADASTRO DE ALUNOS ===")
        print("1 - Cadastrar aluno")
        print("2 - Atualizar dados do aluno")
        print("3 - Remover aluno")
        print("4 - Listar todos os alunos")
        print("5 - Buscar aluno por matrícula")
        print("0 - Sair")
        print("=" * 38)

    print("Bem-vindo ao Sistema de Cadastro de Alunos!")
    
    while True:
        exibir_menu()
        
        try:
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                cadastrar_aluno()
                continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
                if continuar != 's':
                    print("Obrigado por usar o sistema!")
                    break
                    
            elif opcao == 2:
                atualizar_aluno()
                continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
                if continuar != 's':
                    print("Obrigado por usar o sistema!")
                    break
                    
            elif opcao == 3:
                remover_aluno()
                continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
                if continuar != 's':
                    print("Obrigado por usar o sistema!")
                    break
                    
            elif opcao == 4:
                listar_alunos()
                continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
                if continuar != 's':
                    print("Obrigado por usar o sistema!")
                    break
                    
            elif opcao == 5:
                buscar_aluno_por_matricula()
                continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
                if continuar != 's':
                    print("Obrigado por usar o sistema!")
                    break
                    
            elif opcao == 0:
                print("Obrigado por usar o sistema!")
                break
                
            else:
                print("✗ Opção inválida! Tente novamente.")
                
        except ValueError:
            print("✗ Digite um número válido!")

# ===== EXERCÍCIO 69: JOGO DA VELHA MELHORADO =====

def exercicio_69():
    """Exercício 69: Jogo da velha melhorado com detecção de empate e nova partida"""
    
    def criar_tabuleiro():
        """Cria um tabuleiro 3x3 vazio"""
        return [[' ' for _ in range(3)] for _ in range(3)]

    def exibir_tabuleiro(tabuleiro):
        print("\n   0   1   2")
        for i, linha in enumerate(tabuleiro):
            print(f"{i}  {linha[0]} | {linha[1]} | {linha[2]} ")
            if i < 2:
                print("  -----------")

    def fazer_jogada(tabuleiro, linha, coluna, jogador):
        if 0 <= linha < 3 and 0 <= coluna < 3:
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogador
                return True
            else:
                print("✗ Essa posição já está ocupada! Escolha outra.")
                return False
        else:
            print("✗ Posição inválida! Use coordenadas entre 0 e 2.")
            return False

    def verificar_vitoria(tabuleiro, jogador):
        combinacoes_vitoria = [
            [(0,0), (0,1), (0,2)],
            [(1,0), (1,1), (1,2)], 
            [(2,0), (2,1), (2,2)],
            [(0,0), (1,0), (2,0)],
            [(0,1), (1,1), (2,1)],
            [(0,2), (1,2), (2,2)],
            [(0,0), (1,1), (2,2)],
            [(0,2), (1,1), (2,0)]
        ]
        
        for combinacao in combinacoes_vitoria:
            if all(tabuleiro[linha][coluna] == jogador for linha, coluna in combinacao):
                return True
        
        return False

    def verificar_empate(tabuleiro):
        return all(celula != ' ' for linha in tabuleiro for celula in linha)

    def perguntar_nova_partida():
        while True:
            resposta = input("\nDeseja jogar novamente? (s/n): ").lower().strip()
            if resposta in ['s', 'sim']:
                return True
            elif resposta in ['n', 'não', 'nao']:
                return False
            else:
                print("Por favor, responda 's' para sim ou 'n' para não.")

    print("=== JOGO DA VELHA MELHORADO ===")
    print("Jogador 1: X")
    print("Jogador 2: O")
    print("Coordenadas: linha coluna (ex: 1 2)")
    print("Não é permitido jogar na mesma posição duas vezes!")
    
    while True:
        tabuleiro = criar_tabuleiro()
        jogador_atual = 'X'
        jogador_numero = 1
        
        while True:
            exibir_tabuleiro(tabuleiro)
            print(f"\nVez do Jogador {jogador_numero} ({jogador_atual})")
            
            try:
                entrada = input("Digite linha e coluna (ex: 1 2): ").split()
                if len(entrada) != 2:
                    print("✗ Digite exatamente duas coordenadas!")
                    continue
                    
                linha, coluna = int(entrada[0]), int(entrada[1])
                
                if fazer_jogada(tabuleiro, linha, coluna, jogador_atual):
                    if verificar_vitoria(tabuleiro, jogador_atual):
                        exibir_tabuleiro(tabuleiro)
                        print(f"\n🎉 Parabéns! Jogador {jogador_numero} ({jogador_atual}) venceu!")
                        break
                    
                    elif verificar_empate(tabuleiro):
                        exibir_tabuleiro(tabuleiro)
                        print("\n🤝 Empate! Nenhum jogador venceu.")
                        break
                    
                    else:
                        jogador_atual = 'O' if jogador_atual == 'X' else 'X'
                        jogador_numero = 2 if jogador_numero == 1 else 1
                        
            except (ValueError, IndexError):
                print("✗ Entrada inválida! Digite dois números entre 0 e 2.")
        
        if not perguntar_nova_partida():
            print("Obrigado por jogar! Até a próxima! 🎮")
            break

# ===== MENU PRINCIPAL =====

def menu_principal():
    """Menu principal para navegação entre todos os 69 exercícios"""
    # Dicionário que mapeia números dos exercícios para suas funções correspondentes
    exercicios = {
        1: exercicio_01, 2: exercicio_02, 3: exercicio_03, 4: exercicio_04, 5: exercicio_05,
        6: exercicio_06, 7: exercicio_07, 8: exercicio_08, 9: exercicio_09, 10: exercicio_10,
        11: exercicio_11, 12: exercicio_12, 13: exercicio_13, 14: exercicio_14, 15: exercicio_15,
        16: exercicio_16, 17: exercicio_17, 18: exercicio_18, 19: exercicio_19, 20: exercicio_20,
        21: exercicio_21, 22: exercicio_22, 23: exercicio_23, 24: exercicio_24, 25: exercicio_25,
        26: exercicio_26, 27: exercicio_27, 28: exercicio_28, 29: exercicio_29, 30: exercicio_30,
        31: exercicio_31, 33: exercicio_33, 34: exercicio_34, 35: exercicio_35, 36: exercicio_36,
        37: exercicio_37, 38: exercicio_38, 39: exercicio_39, 40: exercicio_40, 41: exercicio_41,
        42: exercicio_42, 43: exercicio_43, 44: exercicio_44, 45: exercicio_45, 46: exercicio_46,
        47: exercicio_47, 48: exercicio_48, 49: exercicio_49, 50: exercicio_50, 51: exercicio_51,
        52: exercicio_52, 53: exercicio_53, 54: exercicio_54, 55: exercicio_55, 56: exercicio_56,
        57: exercicio_57, 58: exercicio_58, 59: exercicio_59, 60: exercicio_60, 61: exercicio_61,
        62: exercicio_62, 63: exercicio_63, 64: exercicio_64, 65: exercicio_65, 66: exercicio_66,
        67: exercicio_67, 68: exercicio_68, 69: exercicio_69
    }
    
    print("=" * 60)
    print("          LISTA COMPLETA DE 69 EXERCÍCIOS PYTHON")
    print("=" * 60)
    print("📚 Exercícios 1-40: Estruturas Condicionais")
    print("🔄 Exercícios 41-60: Estruturas de Repetição") 
    print("📋 Exercícios 61-65: Listas Básicas")
    print("🎮 Exercícios 66-69: Projetos Especiais")
    print("=" * 60)
    
    while True:
        try:
            print("\nDigite o número do exercício (1-69) ou 0 para sair:")
            escolha = int(input("Exercício: "))
            
            if escolha == 0:
                print("Obrigado por usar o sistema! 👋")
                break
            elif escolha == 32:
                print("⏭️ Exercício 32 foi pulado conforme instruções")
            elif escolha in exercicios:
                print(f"\n{'=' * 20} EXERCÍCIO {escolha} {'=' * 20}")
                exercicios[escolha]()
                print("=" * (42 + len(str(escolha))))
            else:
                print("❌ Exercício inválido! Digite um número entre 1 e 69.")
                
        except ValueError:
            print("❌ Digite um número válido!")
        except KeyboardInterrupt:
            print("\n\nSaindo do programa... 👋")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

# Ponto de entrada do programa
# Executa o menu principal apenas se o arquivo for executado diretamente
if __name__ == "__main__":
    menu_principal()