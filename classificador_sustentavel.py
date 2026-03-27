from enum import Enum

#Checkpoint de Computational Thinking Python; Integrantes:
#1: Tárik Moussa Alma. - RM: 571411
#2: Fábricio Aquiles - RM: 570985
#3: Giovane Dias - RM: 569750

# Cria as categorias de classificacao
class Classificacao(Enum):
    NO_POINTS = 'Sem pontuação.'
    HIGHLIGHT = 'Destaque Sústentavel.'
    BONUS = 'Pontuação Bônus.'
    REGISTER_PARTICIPATION = 'Participação registrada.'

print("                                         =============== Classificação de ações sustentáveis =============== ")
print()
print()
#Entrada de dados
impacto = int(input("Como você avalia o impacto desta ação? ( Digite 1 - Baixo, 2 - Médio, 3 - Alto ): " ))
vezes = int(input("Quantas vezes essa mesma ação foi realizada neste mês? ( Digite apenas um número. ): " ))
validacao = input("Essa ação já foi validada pela plataforma, por foto, comprovante ou conferência? ( S/N ): ")
acao = input( "Essa ação foi coletiva ou gerou benefício para outras pessoas? ( S/N ):  " )

#Classificação de pripriedades.
if validacao.upper() == "N":
    classificacao = Classificacao.NO_POINTS
elif impacto == 3 and vezes >= 5:
    classificacao = Classificacao.BONUS
elif impacto == 3 and acao.upper() == "S":
    classificacao = Classificacao.HIGHLIGHT
else:
    classificacao = Classificacao.REGISTER_PARTICIPATION

#Mensagem de acordo com a prioridade.
if classificacao == Classificacao.NO_POINTS:
    acao = "Solicitar validação da ação."
elif classificacao == Classificacao.HIGHLIGHT:
    acao = "Liberar Bônus Especial"
elif classificacao == Classificacao.BONUS:
    acao = "Registrar Ação com Bônus"
else:
    acao = "Registrar Participação"

#Saída de Dados.
print("\n             ----Resultado----")
print(f"Classificação: {classificacao.value}")
print(f"Ação Recomendada: {acao}")
