from Build.User import User

class UserManager:
    def __init__(self, System):
        self.users_ = []  # Lista para armazenar os usuários
        self._carregar_usuarios()  # Carregar usuários do arquivo no momento da inicialização

    def _carregar_usuarios(self):
        # Método privado para carregar usuários do arquivo "passengers.txt"
        try:
            with open("passengers.txt", "r", encoding='utf-8') as arquivo:
                lines = arquivo.readlines()
                i = 0
                while i < len(lines):
                    # Lendo os dados de cada usuário do arquivo
                    name = lines[i].strip()
                    email = lines[i + 1].strip()
                    password = lines[i + 2].strip()
                    cpf = int(lines[i + 3].strip())
                    credit_card = int(lines[i + 4].strip())
                    num_tickets = int(lines[i + 5].strip())
                    flight_info = []

                    for j in range(num_tickets):
                        # Lendo informações de voos do usuário
                        flight_line = lines[i + 6 + j].strip().split()
                        flight_info.append((int(flight_line[0]), int(flight_line[1])))

                    # Dados do usuário formatados em um dicionário
                    user_data = {
                        'name': name,
                        'email': email,
                        'password': password,
                        'cpf': cpf,
                        'credit_card': credit_card,
                        'flight_info': flight_info
                    }
                    self._cadastro_usuario(user_data)  # Cadastro do usuário utilizando o método privado
                    i += 6 + num_tickets
        except FileNotFoundError:
            print("Erro ao abrir o arquivo passengers.txt")

    def _cadastro_usuario(self, user_data):
        # Método privado para criar um objeto User e adicioná-lo à lista de usuários
        user = User(user_data)
        self.users_.append(user)

    def addUser(self, passenger):
        # Método público para adicionar um novo usuário, utilizando o método privado de cadastro
        self._cadastro_usuario(passenger)

    def returnUser(self, name, password):
        # Método para retornar um usuário que corresponda ao nome e senha fornecidos
        for user in self.users_:
            if user.checkName(name):
                if user.checkPassword(password):
                    return user
        print("Não existe o usuário")
        raise ValueError("erro")

    def UpdatePassenger(self):
        # Método para atualizar o arquivo "passengers.txt" com os dados atuais dos usuários
        with open("passengers.txt", "w", encoding='utf-8') as arquivo:
            for user in self.users_:
                profile_data = user.ReturnProfile()
                arquivo.write(profile_data["name"] + "\n")
                arquivo.write(profile_data["email"] + "\n")
                arquivo.write(profile_data["password"] + "\n")
                arquivo.write(str(profile_data["cpf"]) + "\n")
                arquivo.write(str(profile_data["credit_card"]) + "\n")
                arquivo.write(str(len(profile_data["flight_info"])) + "\n")
                for flight_info in profile_data["flight_info"]:
                    arquivo.write(str(flight_info[0]) + " " + str(flight_info[1]) + "\n")

    def validName(self, name):
        # Método para verificar se um nome de usuário é válido (não duplicado)
        for user in self.users_:
            if user.checkName(name):
                return False
        return True

    def validPassword(self, name, password):
        # Método para verificar se a senha é válida para um determinado nome de usuário
        for user in self.users_:
            if user.checkName(name):
                if user.checkPassword(password):
                    return True
                else:
                    return False
        return False
