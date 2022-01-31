print("→Calculadora de IMC ❤️←")
print("Use >q< para sair")
nome = str(input("Qual seu nome?: "))

while True:
  sexo = int(input(f"\n{nome}, qual o seu sexo? \n1 - Homem \n2 - Mulher\n→R= "))
  altura = float(input(f'\n{nome}, qual a sua altura? (use pontuação)\n→R= '))
  peso = float(input(f"\n{nome}, qual o seu peso? (use pontuação)\n→R= "))

#
  imc = peso / (altura * altura)

#Homem
  if sexo == 1:
    if imc < 20.7:
      print(f"{nome} o seu IMC é: {imc:.2f}. Você está abaixo do peso.")
    elif 20.7 <= imc <= 26.4:
      print(f"{nome}, o seu IMC é: {imc:.2f}. Você está no peso ideal.")
    elif 26.5 <= imc <= 27.8:
      print(f"{nome}, o seu IMC é: {imc:.2f}. Você está um pouco acima do peso.")
    elif 27.9 <= imc <= 31.1:
      print(f"{nome}, o seu IMC é: {imc:.2f}. Você está acima do peso.")
    elif imc >= 31.2:
      print("f{nome}, o seu IMC é: {imc:.2f}. Você está bem acima do peso")
      
#Mulher
  if sexo == 2:
    if imc < 19.1:
      print(f"{nome} o seu IMC é: {imc:.2f}. Você está abaixo do peso.")
    elif 19.1 <= imc <= 25.8:
      print(f"{nome}, o seu IMC é: {imc:.2f}. Você está no peso ideal.")
    elif 25.9 <= imc <= 27.3:
      print(f"{nome}, o seu IMC é: {imc:.2f}. Você está um pouco acima do peso.")
    elif 27.4 <= imc <= 32.3:
      print(f"{nome}, o seu IMC é: {imc:.2f}. Você está acima do peso.")
    elif imc >= 32.4:
      print(f"{nome}, o seu IMC é: {imc:.2f}. Você está bem acima do peso.")
