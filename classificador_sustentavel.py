#Checkpoint de Computational Thinking Python; Integrantes:
#1: Tárik Moussa Alma. - RM: 571411
#2: Fábricio Aquiles - RM: 570985
#3: Giovanne Dias - RM: 569750
#4:
#5:




print("                                         =============== Classificação de ações sustentáveis =============== ")
print()
print()
#Entrada de dados.
impacto = int(input("Como você avalia o impacto desta ação? ( Digite 1 - Baixo, 2 - Médio, 3 - Alto ): " ))
vezes = int(input("Quantas vezes essa mesma ação foi realizada neste mês? ( Digite apenas um número. ): " ))
validacao = input("Essa ação já foi validada pela plataforma, por foto, comprovante ou conferência? ( Sim/Não ): ")
acao = input( "Essa ação foi coletiva ou gerou benefício para outras pessoas? ( Sim/Não ):  " )

#Classificação de pripriedades.
if validacao == "Não":
    classificacao = "Sem pontuação."
elif impacto == 3 and acao == "Sim":
    classificacao = "Destaque Sústentavel."
elif impacto == 3 and vezes >= 5:
    classificacao = "Pontuação Bônus."
else:
    classificacao = "Participação Registrada."

#Mensagem de acordo com a prioridade.
if classificacao == "Sem pontuação":
    acao = "Solicitar validação da ação."
elif classificacao == "Destaque Sústentavel":
    acao = "Liberar Bônus Especial"
elif classificacao == "Pontuação bônus":
    acao = "Registrar Ação com Bônus"
else:
    acao = "Registrar Participação"

#Saída de Dados.
print("\n             ----Resultado----")
print(f"Classificação: {classificacao}")
print(f"Ação Recomendada: {acao}")