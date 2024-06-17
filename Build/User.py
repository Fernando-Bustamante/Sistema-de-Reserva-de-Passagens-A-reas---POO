class User:
    def __init__(self, name_:str, email_:str, password_:str, cpf_:int, credit_card:int, tickets_:list) -> None:
        self.name_ = name_
        self.email_ = email_
        self.password_ = password_
        self.cpf_ = cpf_
        self.credit_card = credit_card
        self.tickets_ = tickets_

    def perfil(self) -> None:
        print("Perfil ")
        print("Nome:", self.name_)
        print("CPF:", self.cpf_)
        print("Email:", self.email_)
        print("Senha:", self.password_)
        print("Cartão de Credito:", self.credit_card)

    def addName(self, name: str) -> None:
        if not self.name_:
            self.name_ = name
        else:
            print("Já existe um nome de usuário!")

    def changeName(self, name: str) -> None:
        if not self.name_:
            print("Não existe nenhum nome de usuário!")
        else:
            self.name_ = name
            print("Nome de usuário alterado!")

    def addCpf(self, cpf: int) -> None:
        if self.cpf_ == 0:
            self.cpf_ = cpf
        else:
            print("Já existe um cpf para esse usuário!")

    def addEmail(self, email: str) -> None:
        if not self.email_:
            self.email_ = email
        else:
            print("Já existe um email para esse usuário!")

    def changeEmail(self, email: str) -> None:
        if not self.email_:
            print("Não existe nenhum email para esse usuário!")
        else:
            self.email_ = email
            print("Email foi alterado!")

    def addPassword(self, password: str) -> None:
        if not self.password_:
            self.password_ = password
        else:
            print("Já existe uma senha para esse usuário!")

    def changePassword(self, old_password: str, new_password: str) -> None:
        if not self.password_:
            print("Não existe nenhuma senha para esse usuário!")
        else:
            if self.password_ == old_password:
                self.password_ = new_password
                print("Senha foi alterada!")
            else:
                print("Senha incorreta!")

    def addCreditCard(self, cc: int) -> None:
        if self.credit_card == 0:
            self.credit_card = cc
        else:
            print("Já existe um Cartão de Crédito para esse usuário")

    def checkTickets(self) -> None:
        for ticket in self.tickets_:
            print("Passagem:")
            print("Codigo do voo:", ticket["codigo_voo"])
            print("Origem:", ticket["origin"]["city"] + ", " + ticket["origin"]["country"])
            print("Destino:", ticket["destination"]["city"] + ", " + ticket["destination"]["country"])
            print("Horario:", str(ticket["hour"]["hour"]) + ":" + str(ticket["hour"]["minutes"]))
            print("Assento:", ticket["seat"], "  Preço: $", str(ticket["price"]) + ",00")

    def cancelTicket(self, codigo_voo, seat, System):
        aux = System.returnFlight(codigo_voo)
        if aux.seatCheck(seat):
            check = True
            for ticket in self.tickets_:
                if ticket["codigo_voo"] == codigo_voo and ticket["seat"] == seat:
                    aux.cancelSeat(seat)
                    self.tickets_.remove(ticket)
                    check = False
                    break
            if check:
                print("Esse assento não é seu")
        else:
            print("Assento desocupado")

    def buyTicket(self, codigo_voo, seat, System) -> None:
        aux = System.returnFlight(codigo_voo)
        if not aux.seatCheck(seat):
            aux.getSeat(seat)
            self.tickets_.append(aux.getTicket(seat))
        else:
            print("Assento ocupado")

    def checkName(self, name: str) -> bool:
        return self.name_ == name

    def checkPassword(self, password: str) -> bool:
        return self.password_ == password

    def checkCpf(self, cpf: int) -> bool:
        return self.cpf_ == cpf

    def ReturnProfile(self):
        profile_user = {
            "name": self.name_,
            "email": self.email_,
            "password": self.password_,
            "cpf": self.cpf_,
            "credit_card": self.credit_card,
            "flight_info": [(ticket["voo"], ticket["seat"]) for ticket in self.tickets_]
        }
        return profile_user
  
