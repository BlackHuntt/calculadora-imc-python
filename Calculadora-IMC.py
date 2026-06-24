def calcular_imc():
    """
    Calcula o IMC do usuário com validação de dados
    e classificação segundo a OMS
    """
    print("\n---- BEM VINDO AO CALCULADOR DE IMC ----")
  
    nome = input("Olá, digite seu nome: ").strip()
    
    # Validação de idade - não deixa passar até acertar
    while True:
        try:
            idade = int(input(f"{nome}, digite sua idade: "))
            if idade <= 0 or idade > 120:
                print("Idade inválida. Digite entre 1 e 120.")
                continue
            break
        except ValueError:
            print("Erro: Digite apenas números inteiros. Ex: 25")

    # Validação de peso
    while True:
        try:
            peso = float(input(f"{nome}, digite seu peso em kg: "))
            if peso <= 0 or peso > 300:
                print("Peso inválido. Digite entre 1 e 300kg.")
                continue
            break
        except ValueError:
            print("Erro: Use ponto para decimais. Ex: 70.5")
      
    # Validação de altura
    while True:
        try:
            altura = float(input(f"{nome}, digite sua altura em metros: "))
            if altura <= 0 or altura > 3:
                print("Altura inválida. Digite entre 0.5 e 3 metros.")
                continue
            break
        except ValueError:
            print("Erro: Use ponto para decimais. Ex: 1.75")

    # Cálculo do IMC
    imc = peso / (altura ** 2)
    
    print(f"\n{nome}, seu IMC é: {imc:.2f}")
    
    # Classificação OMS - isso aqui é valor pro usuário
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    elif imc < 35:
        classificacao = "Obesidade Grau I"
    elif imc < 40:
        classificacao = "Obesidade Grau II"
    else:
        classificacao = "Obesidade Grau III"
    
    print(f"Classificação: {classificacao}")
    print("-" * 40)

# Loop principal do programa
if __name__ == "__main__":
    while True:
        calcular_imc()
        
        continuar = input("\nDeseja calcular novamente? [s/n]: ").lower().strip()
        
        if continuar != 's':
            print("\nObrigado por usar a Calculadora de IMC!")
            print("Projeto by BlackHuntt 👊")
            break
  