# Candidatos a vereador
Vereador11111 = "Jack Black"
Vereador22222 = "Andrew Zimmern"
Vereador33333 = "Carlinhos Maia"
Vereador44444 = "Tirulipa"
Vereador55555 = "Johnny Damon"
Vereador66666 = "Viktor Yaglusvo"
Vereador77777 = "Guy Fieri"
Vereador88888 = "Nusr Et"
Vereador99999 = "Tony Ramos"
Vereador00000 = "Marcus Smart"

# nome dos candidatos a prefeito
Prefeito99 = "Aaron Judge"
Prefeito48 = "Anthony Rizzo"
Prefeito27 = "Giancarlo Stanton"
Prefeito26 = "DJ Lemahieu"
Prefeito24 = "Matt Carpenter"

# variaveis onde salva os votos para Vereador
votoVereador11111 = 0
votoVereador22222 = 0
votoVereador33333 = 0
votoVereador44444 = 0
votoVereador55555 = 0
votoVereador66666 = 0
votoVereador77777 = 0
votoVereador88888 = 0
votoVereador99999 = 0
votoVereador00000 = 0

# variaveis onde salva os votos para prefeito
votoPrefeito99 = 0
votoPrefeito48 = 0
votoPrefeito27 = 0
votoPrefeito26 = 0
votoPrefeito24 = 0

# variáveis para salvar os votos nulos
anular = 0
anularVereador = 0
anularPrefeito = 0

# variável para salvar os votos em brancos
votoEmBranco = 0

# variável para computar os votos em branco
votoEmBrancoVereador = 0
votoEmBrancoPrefeito = 0

# variavel para salvar a opcao do menu
opcaoMenu = 0

while opcaoMenu != 4:

    def imprimeMenu():
        print("\n+---------URNA ELETRÔNICA---------+")
        print("\n|  Qual a opção voce deseja?      |\n")
        print("+---------------------------------+")
        print("| 1 - Listar Candidatos           |")
        print("| 2 - Iniciar Votação             |")
        print("| 3 - Apurar votos                |")
        print("| 4 - Desligar a urna             |")
        print("+---------------------------------+\n")


    def recebeOpMenu():
        return (int(input("Digite a opção desejada: ")))


    imprimeMenu()
    opcaoMenu = recebeOpMenu()

    # lista dos candidatos
    if opcaoMenu == 1:
        print("\n+-----------CANDIDATOS------------+")
        print("|           Vereador              |")
        print("|                                 |")
        print("| 11111 = Jack Black              |")
        print("| 22222 = Andrew Zimmern          |")
        print("| 33333 = Carlinhos Maia          |")
        print("| 44444 = Tirulipa                |")
        print("| 55555 = Johnny Damon            |")
        print("| 66666 = Viktor Yaglusvo         |")
        print("| 77777 = Guy Fieri               |")
        print("| 88888 = Nusr Et                 |")
        print("| 99999 = Tony Ramos              |")
        print("| 00000 = Marcus Smart            |")
        print("|                                 |")
        print("|         Prefeito                |")
        print("|                                 |")
        print("| 99 = Aaron Judge                |")
        print("| 48 = Anthony Rizzo              |")
        print("| 27 = Giancarlo Stanton          |")
        print("| 26 = DJ Lemahieu                |")
        print("| 24 = Matt Carpenter             |")
        print("+---------------------------------+\n")

    elif opcaoMenu == 2:

        # Decisão do candidato à goverância
        votoVereador = input("\nDigite o número do candidato para vereador (ou B para Em Branco): ").upper()


        # função de confirmação dos votos
        def confirmarVoto():

            confirmar = input("\nConfirmar voto? (s ou n): ").lower()

            if confirmar == 's':
                print("\nVoto registrado!")
                return True

            elif confirmar == 'n':
                print("\nVotação cancelada!")
                return False

            else:
                print("\nOpção inválida!")
                return False


        # registros de cada voto para governador
        if votoVereador == 'B':
            print("\nVoto em Branco Registrado!")

            if confirmarVoto():
                votoEmBrancoVereador += 1

        elif votoVereador == '11111':
            print("\nCandidato escolhido: %s" % (Vereador11111))

            if confirmarVoto():
                votoVereador11111 += 1

        elif votoVereador == '22222':
            print("\nCandidato escolhido: %s" % (Vereador22222))

            if confirmarVoto():
                votoVereador22222 += 1

        elif votoVereador == '33333':
            print("\nCandidato escolhido: %s" % (Vereador33333))

            if confirmarVoto():
                votoVereador33333 += 1

        elif votoVereador == '44444':
            print("\nCandidato escolhido: %s" % (Vereador44444))

            if confirmarVoto():
                votoVereador44444 += 1

        elif votoVereador == '55555':
            print("\nCandidato escolhido: %s" % (Vereador55555))

            if confirmarVoto():
                votoVereador55555 += 1

        elif votoVereador == '66666':
            print("\nCandidato escolhido: %s" % (Vereador66666))

            if confirmarVoto():
                votoVereador66666 =+ 1

        elif votoVereador == '77777':
            print("\nCandidato escolhido: %s" % (Vereador77777))

            if confirmarVoto():
                votoVereador77777 = + 1

        elif votoVereador == '88888':
            print("\nCandidato escolhido: %s" % (Vereador88888))

            if confirmarVoto():
                votoVereador88888 = + 1

        elif votoVereador == '99999':
            print("\nCandidato escolhido: %s" % (Vereador99999))

            if confirmarVoto():
                votoVereador99999 = + 1

        elif votoVereador == '00000':
            print("\nCandidato escolhido: %s" % (Vereador00000))

            if confirmarVoto():
                votoVereador00000 = + 1

        else:
            # voto nulos para Vereadores
            anular = input("\nDeseja votar nulo? (s ou n): ").lower()

            if anular == "s":
                print("\nVoto nulo registrado!")
                anularVereador += 1

            elif anular == "n":
                print("\nVoto nulo não registrado!")

            else:
                print("\nOpção inválida!")

        # Decisão do candidato à presidência
        votoPrefeito = input("\nDigite o número do candidato à Prefeitura (ou B para Em Branco): ").upper()

        # registros de cada voto para presidente
        if votoPrefeito == 'B':
            print("Voto em Branco registrado!")

            if confirmarVoto():
                votoEmBrancoPrefeito += 1

        elif votoPrefeito == '99':
            print("Candidato escolhido: %s" % (Prefeito99))

            if confirmarVoto():
                votoPrefeito99 += 1

        elif votoPrefeito == '48':
            print("Candidato escolhido: %s" % (Prefeito48))

            if confirmarVoto():
                votoPrefeito48 += 1

        elif votoPrefeito == '24':
            print("Candidato escolhido: %s" % (Prefeito24))

            if confirmarVoto():
                votoPrefeito24 += 1

        elif votoPrefeito == '26':
            print("Candidato escolhido: %s" % (Prefeito26))

            if confirmarVoto():
                votoPrefeito26 += 1

        elif votoPrefeito == '27':
            print("Candidato escolhido: %s" % (Prefeito27))

            if confirmarVoto():
                votoPrefeito27 += 1

        else:
            # anulação do voto para presidente
            anular = input("\nDeseja votar nulo? (s/n): ").lower()

            if anular == 's':
                print("\nVoto nulo registrado!")
                anularPres += 1

            elif anular == 'n':
                print("\nVoto nulo não resgistrado!")

            else:
                print("\nOpção inválida!")

        # apuração dos votos
    elif opcaoMenu == 3:
        print("###########################################################")
        print("\n+----------------APURAÇÃO DOS VOTOS-----------------------+")
        print("|                  Votos para Vereador                   ")
        print("| Votos do candidato %s: %i" % (Vereador11111, votoVereador11111))
        print("| Votos do candidato %s: %i" % (Vereador22222, votoVereador22222))
        print("| Votos do candidato %s: %i" % (Vereador33333, votoVereador33333))
        print("| Votos do candidato %s: %i" % (Vereador44444, votoVereador44444))
        print("| Votos do candidato %s: %i" % (Vereador55555, votoVereador55555))
        print("| Votos do candidato %s: %i" % (Vereador66666, votoVereador66666))
        print("| Votos do candidato %s: %i" % (Vereador77777, votoVereador77777))
        print("| Votos do candidato %s: %i" % (Vereador88888, votoVereador88888))
        print("| Votos do candidato %s: %i" % (Vereador99999, votoVereador99999))
        print("| Votos do candidato %s: %i" % (Vereador00000, votoVereador00000))
        print("##########################################################")
        print("|                 Votos para Prefeito                    ")
        print("| Votos do candidato %s: %i" % (Prefeito99, votoPrefeito99))
        print("| Votos do candidato %s: %i" % (Prefeito48, votoPrefeito48))
        print("| Votos do candidato %s: %i" % (Prefeito27, votoPrefeito27))
        print("| Votos do candidato %s: %i" % (Prefeito26, votoPrefeito26))
        print("| Votos do candidato %s: %i" % (Prefeito24, votoPrefeito24))
        print("|##########################################################|")
        print("|                  Votos Nulos  ")
        print("| Votos nulos para vereador: %i" % (anularVereador))
        print("| Votos nulos para prefeito: %i" % (anularPrefeito))
        print("|##########################################################|")
        print("|               Votos em Branco     ")
        print("| Votos em branco para vereador: %i" % (votoEmBrancoVereador))
        print("| Votos em branco para prefeito: %i" % (votoEmBrancoPrefeito))
        print("###########################################################")

    # opção para encerrar o programa
    elif opcaoMenu == 4:
        print("\nObrigado por usar a Urna Eletrnônica!\nDesligando a Urna\n")

    # opção caso o usuário digite uma opção incorreta do menu
    else:
        print("\nOpção inválida!")