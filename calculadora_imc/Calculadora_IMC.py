while True:
    try:
        print("\n=== Calculadora de IMC ===")

        peso = float(input("Digite seu peso atual em Kgs: "))
        altura = float(input("Digite sua altura em metros: "))

        # cálculo do IMC
        imc = peso / (altura ** 2)

        # exibir e classificar IMC
        print(f"\nSeu IMC é: {imc:.2f}")

        if imc < 18.5:
            print("Você está abaixo do peso ideal.")
        elif 18.5 <= imc <= 25.0:
            print("Você está no peso ideal!")
        elif 25 < imc <= 30:
            print("Você está com sobrepeso.")
        elif 30 < imc <= 34.9:
            print("Obesidade de grau 1.")
        elif 35 < imc <= 39.9:
            print("Obesidade de grau 2.")
        elif imc >= 40:
            print("Obesidade de grau 3.")

        print("-" * 30)
        continuar = input("Deseja realizar uma nova análise? (Sim/Não): ").strip().upper()

        if continuar != "SIM":
            print("\nObrigado por usar a Calculadora de IMC. Encerrando o programa.")
            break  # Sai do loop

    except ValueError:
        print("\n[ERRO] Entrada inválida. Por favor, digite apenas números (use ponto para decimais).")
