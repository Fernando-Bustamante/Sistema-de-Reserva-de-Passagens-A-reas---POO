from Build.User import User

class UserManager:
    def __init__(self, System):
        self.users_ = []
        try:
            with open("Data/passengers.txt", "r", encoding='utf-8') as arquivo:
                lines = arquivo.readlines()
                i = 0
                while i < len(lines):
                    if i + 5 >= len(lines):
                        print(f"Dados incompletos para um usuário no arquivo na linha {i}")
                        break
                    try:
                        name = lines[i].strip()
                        email = lines[i + 1].strip()
                        password = lines[i + 2].strip()
                        cpf = int(lines[i + 3].strip())
                        credit_card = int(lines[i + 4].strip())
                        num_tickets = int(lines[i + 5].strip())
                        flight_info = []
                        i += 5
                        for j in range(num_tickets):
                            if i >= len(lines):
                                print(f"Dados de voo incompletos para o usuário {name} na linha {i}")
                                break
                            flight_line = lines[i].strip().split()
                            if len(flight_line) != 2:
                                print(f"Dados de voo mal formatados para o usuário {name} na linha {i}")
                                break
                            flight_info.append((int(flight_line[0]), int(flight_line[1])))
                            i += 1
                        user = User(name, email, password, cpf, credit_card, flight_info)
                        self.users_.append(user)
                    except ValueError as ve:
                        print(f"Erro de valor ao processar dados do usuário na linha {i}: {ve}")
                        i += 6  # Pular para o próximo conjunto de dados
        except FileNotFoundError:
            print("Erro ao abrir o arquivo passengers.txt")

    def addUser(self, passenger):
        self.users_.append(passenger)

    def returnUser(self, name, password):
        for user in self.users_:
            if user.checkName(name):
                if user.checkPassword(password):
                    return user
        print("Não existe o usuário")
        raise ValueError("erro")

    def UpdatePassenger(self):
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
