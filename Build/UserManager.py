from Build.User import User

class UserManager:
    def __init__(self, System):
        self.users_ = []
        self.System = System
        self._carregar_usuarios()

    def _carregar_usuarios(self):
        try:
            with open("Data/passengers.txt", "r", encoding='utf-8') as arquivo:
                lines = arquivo.readlines()
                i = 0
                while i < len(lines):
                    name = lines[i].strip()
                    email = lines[i + 1].strip()
                    password = lines[i + 2].strip()
                    cpf = int(lines[i + 3].strip())
                    credit_card = int(lines[i + 4].strip())
                    num_tickets = int(lines[i + 5].strip())
                    flight_info = []

                    for j in range(num_tickets):
                        flight_line = lines[i + 6 + j].strip().split()
                        flight_info.append({
                            "voo": int(flight_line[0]),
                            "seat": int(flight_line[1])
                        })

                    user = User(name, email, password, cpf, credit_card, flight_info)
                    self.users_.append(user)
                    i += 6 + num_tickets
        except FileNotFoundError:
            print("Erro ao abrir o arquivo passengers.txt")

    def _cadastro_usuario(self, user_data):
        user = User(**user_data)
        self.users_.append(user)

    def addUser(self, passenger):
        user_data = {
            'name_': passenger[0],
            'email_': passenger[1],
            'password_': passenger[2],
            'cpf_': int(passenger[3]),
            'credit_card': int(passenger[4]),
            'tickets_': passenger[5]
        }
        self._cadastro_usuario(user_data)
        self.atualizar_arquivo_usuarios()

    def returnUser(self, name, password):
        for user in self.users_:
            if user.checkName(name):
                if user.checkPassword(password):
                    return user
        print("Não existe o usuário")
        raise ValueError("erro")

    def UpdatePassenger(self):
        self.atualizar_arquivo_usuarios()

    def atualizar_arquivo_usuarios(self):
        try:
            with open("Data/passengers.txt", "w", encoding='utf-8') as arquivo:
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
        except Exception as e:
            print(f"Erro ao atualizar o arquivo: {e}")

    def validName(self, name):
        for user in self.users_:
            if user.checkName(name):
                return False
        return True

    def validPassword(self, name, password):
        for user in self.users_:
            if user.checkName(name):
                if user.checkPassword(password):
                    return True
                else:
                    return False
        return False
