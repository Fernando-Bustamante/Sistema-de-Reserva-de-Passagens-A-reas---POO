class Flight:
    def __init__(self):
        self.destination = {"city": "", "country": ""}
        self.origin = {"city": "", "country": ""}
        self.price = 0.00
        self.seats = 0
        self.codigo_voo = 0
        self.hour = {"hour": 0, "minutes": 0}
        self.seat = []

    def addDestinationCity(self, city):
        self.destination["city"] = city

    def addDestinationCountry(self, country):
        self.destination["country"] = country

    def addOriginCity(self, city):
        self.origin["city"] = city

    def addOriginCountry(self, country):
        self.origin["country"] = country

    def addTimeHour(self, hr):
        self.hour["hour"] = hr

    def addTimeMinute(self, min):
        self.hour["minutes"] = min

    def addPrice(self, p):
        self.price = p

    def addFlightCode(self, c):
        self.codigo_voo = c

    def code(self):
        return self.codigo_voo

    def addSeat(self, q):
        self.seats = q
        self.seat = [False] * q

    def seatCheck(self, n):
        return self.seat[n - 1]

    def returnPrice(self):
        return self.price

    def getSeat(self, n):
        if n > 0:
            if n <= self.seats:
                if not self.seat[n - 1]:
                    self.seat[n - 1] = True
        else:
            print("Esse assento não existe!")

    def getTicket(self, n):
        return {"codigo_voo": self.codigo_voo, "origin": self.origin, "destination": self.destination,
                "hour": self.hour, "seat": n, "price": self.price}

    def cancelSeat(self, n):
        if 0 <= n - 1 < self.seats:
            if self.seat[n - 1]:
                self.seat[n - 1] = False
        else:
            print("Não existe esse assento!")

    def printFlight(self):
        print("Código do Vôo:", self.codigo_voo)
        print("Origem:", self.origin["city"] + ", " + self.origin["country"])
        print("Destino:", self.destination["city"] + ", " + self.destination["country"])
        print("Horario:", str(self.hour["hour"]) + ":" + str(self.hour["minutes"]))
        print("Preço: R$", self.price)
        print("Assentos:", self.seats)
        print("-----------------------")

    def printSeats(self):
        print(" 0 : Disponivel")
        print(" 1 : Ocupado")

        aux = 0

        for i in range(self.seats):
            if i + 1 < 100:
                if i + 1 < 10:
                    print("  ", end="")
                else:
                    print(" ", end="")
            print(i + 1, ":", int(self.seat[i]), "|", end=" ")
            aux += 1
            if aux == 3 or aux == 7:
                print("    ", end="")
            elif aux == 10:
                aux = 0
                print()

    def flightSize(self):
        return len(self.seat)

