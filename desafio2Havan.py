finalizar = input(" Olá, bem vindo ao programada de conversão, você gostaria de iniciar? (S/N)")


while (finalizar is  "S" or finalizar is  "s"):
    from datetime import date
#Criação de variáveis, juntamento com a lista das moedas pré-cadastradas
    nomeCliente = input("Insira o seu nome:")
    listaMoedas = ["dólar","Dólar","euro","Euro","real","Real"]
    moedaOrigem = input(" Insira a moeda de origem dentro dessas moedas pré-cadastradas:" +str(listaMoedas))
    moedaDestino = input(" Insira a moeda de destino dentro dessas moedas pré-cadastradas:" +str(listaMoedas))
    data = date.today()
    moedaVlr = float(input("Insira o valor a ser convertido em " +moedaDestino+ ":"))
    moedaVlrConvert = ""


#verificação se as moedas estão na lista pré-cadastrada
    if (moedaOrigem in listaMoedas and moedaDestino in listaMoedas):
     #se as moedas forem iguais, não é possível executar
        if(moedaOrigem == moedaDestino):
            print("Você não pode converter duas moedas iguais.")


     #se as moedas forem diferentes executa o programa
    if(moedaOrigem != moedaDestino):
        if(moedaOrigem in ["dólar","Dólar"] and moedaDestino in ["real","Real"]):
               moedaVlrConvert = moedaVlr * 5.26
               taxa = moedaVlrConvert * .5

        if(moedaOrigem in ["dólar","Dólar"] and moedaDestino in ["euro","Euro"]):
               moedaVlrConvert = moedaVlr * 0.82
               taxa = moedaVlrConvert * .5

        if(moedaOrigem in ["real","Real"] and moedaDestino in ["dólar","Dólar"]):
               moedaVlrConvert = moedaVlr / 5.26
               taxa = moedaVlrConvert *.5

        if(moedaOrigem in ["real","Real"] and moedaDestino in ["euro","Euro"]):
               moedaVlrConvert = moedaVlr * 0.16 
               taxa = moedaVlrConvert * .5

        if(moedaOrigem in ["euro","euro"] and moedaDestino in ["dólar","Dólar"]):
               moedaVlrConvert = moedaVlr * 1.22 
               taxa = moedaVlrConvert * .5

        if(moedaOrigem in ["euro","euro"] and moedaDestino in ["real","Real"]):
               moedaVlrConvert = moedaVlr * 6.39   
               taxa = moedaVlrConvert * .5

        print(
        "A moeda escolhida para ser convertida foi " +moedaOrigem+
        "e a moeda de destino, " +moedaDestino+"  ,o valor convertido é:"+str(round(moedaVlrConvert, 2)),
        " e a taxa cobrada foi de:",round(taxa), "no dia:",data," pelo cliente:",nomeCliente
        )

        finalizar = input("Você gostaria de continuar? (S/N)")
    else:
        print("As moedas escolhidas não estão na lista.")

print("Obrigado por utilizar nosso programa, tenha uma ótimo dia.")