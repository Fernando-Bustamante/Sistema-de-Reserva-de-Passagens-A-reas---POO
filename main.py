from FlightManager import FlightManager
from User import User
from UserManager import UserManager

def displayMenu():
    print("  Aproveite nossas ofertas de passagens aéreas e programe toda a sua viagem com a GoldTrip. Aqui você vai encontrar diversas opções de voos para diversos lugares e com as melhores companhias aéreas nacionais e internacionais. Consulte todas as disponibilidades e realize sua compra de maneira fácil, rápida e sem precisar sair de casa. Além das melhores tarifas, na GoldTrip você encontra dicas para deixar sua viagem ainda mais completa. Não perca tempo, reserve agora mesmo sua passagem e embarque nessa nova aventura. Reserve suas passagens no maior e melhor sistema de reservas de passagens! Planejar sua próxima viagem nunca foi tão fácil!\n")
    print("-> 1. Visualizar voos disponíveis")
    print("-> 2. Login/Cadastro")
    print("-> 0. Sair")
    print("Escolha uma opção: ")

def displayProfileMenu():
    print("  Altere seu perfil. Acompanhe preços, organize planos de viagem e acesse ofertas e experiências exclusivas com sua conta. Assim fica muito mais fácil!\n")
    print("-> 1. Alterar nome")
    print("-> 2. Alterar e-mail")
    print("-> 3. Alterar senha")
    print("-> 4. Visualizar tickets")
    print("-> 5. Comprar ticket")
    print("-> 6. Cancelar ticket")
    print("-> 7. Visualizar seu perfil")
    print("-> 0. Voltar ao menu principal")
    print("Escolha uma opção: ")

def main():
    Sistema = FlightManager()
    SistemadeUsuario = UserManager(Sistema)

    choice = -1  # Inicializando com um valor diferente de 0
    while choice != 0:
        displayMenu()
        choice = int(input())

        profileChoice = -1

        if choice == 1:
            Sistema.showFlights()

        elif choice == 2:
            usuario = None
            login_choice = bool(int(input("Escolha se quer logar(1) ou cadastrar uma nova conta(0): ")))
            if login_choice:  # LOGIN
                while True:
                    name = input("Para voltar digite '0'\nDigite o nome do usuário: ")
                    if name == '0':
                        break
                    if SistemadeUsuario.validName(name):
                        print("Insira um nome de usuário válido.")
                        continue
                    password = input("Digite sua senha: ")
                    if not SistemadeUsuario.validPassword(name, password):
                        print("Senha incorreta.")
                        continue
                    usuario = SistemadeUsuario.returnUser(name, password)
                    break
            else:  # CADASTRO
                print("Por favor, insira os dados requisitados:")
                name = ''
                while True:
                    name = input("Digite o nome: ")
                    if SistemadeUsuario.validName(name):
                        break
                    else:
                        print("Nome de usuário inválido.")
                cpf = int(input("Adicione o CPF: "))
                email = input("Digite um e-mail: ")
                password = input("Digite sua senha: ")
                cc = int(input("Digite o número do cartão de crédito: "))
                usuario = User(name, email, password, cpf, cc, [])  # Criando um novo usuário com os dados fornecidos
                SistemadeUsuario.addUser(usuario)
                usuario = SistemadeUsuario.returnUser(name, password)

            while profileChoice != 0:
                displayProfileMenu()
                profileChoice = int(input())

                if profileChoice == 1:
                    name = input("Digite um novo nome: ")
                    usuario.changeName(name)

                elif profileChoice == 2:
                    email = input("Digite um novo e-mail: ")
                    usuario.changeEmail(email)

                elif profileChoice == 3:
                    old_password = input("Digite sua antiga senha: ")
                    new_password = input("Digite a nova senha: ")
                    usuario.changePassword(old_password, new_password)

                elif profileChoice == 4:
                    usuario.checkTickets()

                elif profileChoice == 5:
                    Sistema.showFlights()
                    codigo = int(input("Selecione seu voo pelo código: "))
                    if 1 <= codigo <= Sistema.manyFlights():
                        flightaux = Sistema.returnFlight(codigo)
                        flightaux.printseats()
                        assento = int(input("Selecione um assento pelo número: "))
                        if 1 <= assento <= flightaux.flightSize() and not flightaux.seatCheck(assento):
                            usuario.buyTicket(codigo, assento, Sistema)
                        else:
                            print("Insira um assento válido, retornando ao sistema do perfil.")
                    else:
                        print("Insira um código de voo válido, retornando ao sistema do perfil.")

                elif profileChoice == 6:
                    usuario.checkTickets()
                    codigo = int(input("Selecione o voo que quer cancelar pelo código: "))
                    if 1 <= codigo <= Sistema.manyFlights():
                        flightaux = Sistema.returnFlight(codigo)
                        assento = int(input("Selecione um assento pelo número: "))
                        if 1 <= assento <= flightaux.flightSize() and flightaux.seatCheck(assento):
                            usuario.cancelTicket(codigo, assento, Sistema)
                        else:
                            print("Insira um assento válido, retornando ao sistema do perfil.")
                    else:
                        print("Insira um código de voo válido, retornando ao sistema do perfil.")

                elif profileChoice == 7:
                    usuario.perfil()

                elif profileChoice == 0:
                    print("Voltando ao menu principal.")
        elif choice == 0:
            print("Saindo do programa. Obrigado!")            
        else:
            print("Opção inválida. Tente novamente.")

    SistemadeUsuario.UpdatePassenger()
    

if __name__ == "__main__":
    main()
