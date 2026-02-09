turma = []
aula = []
chamada = {}

almoco = {
    "segunda": {},
    "terca": {},
    "quarta": {},
    "quinta": {},
    "sexta": {}
}

##########################################################################
def chamar_falta():
    aluno = input("Que aluno faltou?: ")
    if aluno in turma:
        chamada[aluno] = chamada.get(aluno, 0) + 1
        print("Falta marcada para", aluno, "- Total:", chamada[aluno] , "falta(s)")
    else:
        print("Aluno não existe na turma.")
##########################################################################
def registrar_falta():
    aluno = input("Nome do aluno: ")
    if aluno in chamada:
        print(f"{aluno} tem {chamada[aluno]} falta(s).")
    else:
        print("Esse aluno não tem faltas registadas.")

####################################################################
def adicionar_alunos():
    nome = input("Digite o nome do aluno que quer adicionar: ")
    if nome != str:
        print("por favor digite um nome")
    elif nome not in turma:
        turma.append(nome)
        print("Aluno adicionado. Bem-vindo", nome)
    else:
        print("Aluno já existe.")
######################################################################
def remover_alunos():
    nome = input("Digite o aluno que quer transferir: ")
    if nome in turma:
        turma.remove(nome)
        print("Aluno transferido")
    else:
        print("Aluno não existente")
######################################################################
def lista_alunos():
    if not turma:
        print("Nenhum aluno existente.")
    else:
        print("Alunos da turma:")
        for nome in turma:
            print("-", nome)
##########################################################################
def procurar_alunos():
    nome = input("Que aluno quer procurar?: ")
    if nome in turma:
        print("Aluno encontrado")
    else:
        print("Aluno não encontrado")

##########################################################################
def adicionar_disciplinas():
    nome = input("Digite a disciplina que quer adicionar: ")
    aula.append(nome)
    print("Disciplina adicionada:", nome)
#############################################################################
def lista_disciplinas():
    if not aula:
        print("Nenhuma disciplina existente.")
    else:
        print("Disciplinas:")
        for d in aula:
            print("-", d)

# ===================== ALMOÇO =====================
def marcar_almoco():
    aluno = input("Nome do aluno: ")
    if aluno not in turma:
        print("Aluno não existe na turma.")
        return

    dia = input("Dia do almoço (segunda/terca/quarta/quinta/sexta): ").lower()

    if dia not in almoco:
        print("Dia inválido.")
        return

    almoco[dia][aluno] = almoco[dia].get(aluno, 0) + 1
    print(f"Almoço marcado para {aluno} na {dia}. Total: {almoco[dia][aluno]} almoço")

def ver_almoco():
    dia = input("Dia (seg/ter/qua/qui/sex): ").lower()
    if dia in almoco and almoco[dia]:
        print(f"Almoços marcados para {dia}:")
        for aluno, total in almoco[dia].items():
            print(f"- {aluno}: {total}")
    else:
        print("Nenhum almoço marcado nesse dia.")

# ===================== MENU =====================
def menu():
    while True:
        print("\n///// Turma de programação /////")
        print("~~~~~~~~Alunos~~~~~~~~")
        print("1. Adicionar aluno")
        print("2. Remover aluno")
        print("3. Listar alunos")
        print("4. Procurar aluno")
        print("~~~~~~~~Disciplinas~~~~~~~~")
        print("5. Adicionar disciplina")
        print("6. Listar disciplinas")
        print("~~~~~~~~Faltas~~~~~~~~")
        print("7. Marcar falta")
        print("8. Ver faltas")
        print("~~~~~~~~Almoço~~~~~~~~")
        print("9. Marcar almoço")
        print("10. Ver almoços do dia")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_alunos()
        elif opcao == "2":
            remover_alunos()
        elif opcao == "3":
            lista_alunos()
        elif opcao == "4":
            procurar_alunos()
        elif opcao == "5":
            adicionar_disciplinas()
        elif opcao == "6":
            lista_disciplinas()
        elif opcao == "7":
            chamar_falta()
        elif opcao == "8":
            registrar_falta()
        elif opcao == "9":
            marcar_almoco()
        elif opcao == "10":
            ver_almoco()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida.")

menu()