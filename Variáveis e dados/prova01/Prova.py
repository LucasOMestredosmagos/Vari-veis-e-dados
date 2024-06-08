# Definindo variáveis de diferentes tipos
inteiro = 20              #Variável inteira (int)
flutuante = 20.5          #Variável de ponto flutuante (float)
texto = "Olá, Mundo!"     #Variável de texto (string)
booleano = True           #Variável booleana (True or false)

# Solicitando dados do úsuario 
nome = input("Por favor, digite seu nome: ")
idade = int(input("Por favor, digite sua idade: "))
altura = float(input("Por favor, digite sua altura (em metros): "))

#imprimindo a solicitação anterior na tela com uma mensagem personalizada
print(f"Olá, {nome}! Você tem {idade} anos e {altura} metros de altura")