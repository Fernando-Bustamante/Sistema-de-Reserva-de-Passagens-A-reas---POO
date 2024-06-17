from Build.Flight import Flight

class FlightManager:
    def __init__(self):
        self.flights = []  # Lista para armazenar os voos
        self._carregar_voos()  # Carregar voos do arquivo no momento da inicialização

    def _carregar_voos(self):
        # Método privado para carregar voos do arquivo "voos.txt"
        try:
            with open("Data/voos.txt", "r", encoding='utf-8') as arquivo:
                lines = arquivo.readlines()
                for i in range(0, len(lines), 9):
                    flight_data = {
                        'code': int(lines[i].strip()),
                        'origin_city': str(lines[i + 1].strip()),
                        'origin_country': str(lines[i + 2].strip()),
                        'destination_city': str(lines[i + 3].strip()),
                        'destination_country': str(lines[i + 4].strip()),
                        'time_hour': int(lines[i + 5].strip()),
                        'time_minute': int(lines[i + 6].strip()),
                        'price': float(lines[i + 7].strip()),
                        'seat': int(lines[i + 8].strip())
                    }
                    self._cadastro_voo(flight_data)  # Cadastro do voo utilizando o método privado
        except FileNotFoundError:
            print("Erro ao abrir o arquivo voos.txt")

    def _cadastro_voo(self, flight_data):
        # Método privado para criar um objeto Flight e adicioná-lo à lista de voos
        flight = Flight()
        flight.addFlightCode(flight_data['code'])
        flight.addOriginCity(flight_data['origin_city'])
        flight.addOriginCountry(flight_data['origin_country'])
        flight.addDestinationCity(flight_data['destination_city'])
        flight.addDestinationCountry(flight_data['destination_country'])
        flight.addTimeHour(flight_data['time_hour'])
        flight.addTimeMinute(flight_data['time_minute'])
        flight.addPrice(flight_data['price'])
        flight.addSeat(flight_data['seat'])
        self.flights.append(flight)

    def changeFlight(self, codigo, seat):
        # Método para alterar o assento de um voo específico
        self.flights[codigo - 1].getSeat(seat)

    def addFlight(self, flight):
        # Método para adicionar um novo voo à lista de voos
        self._cadastro_voo(flight)
        self.atualizar_arquivo_voos()  # Atualiza o arquivo de voos após adicionar um novo voo

    def showFlights(self):
        # Método para mostrar todos os voos
        for flight in self.flights:
            flight.printFlight()

    def returnFlight(self, codigo):
        # Método para retornar um voo específico pelo código
        for flight in self.flights:
            if codigo == flight.code():
                return flight
        return self.flights[codigo]

    def manyFlights(self):
        # Método para retornar a quantidade de voos
        return len(self.flights)

    def atualizar_arquivo_voos(self):
        # Método para atualizar o arquivo "voos.txt" com os dados atuais dos voos
        try:
            with open("Data/voos.txt", "w", encoding='utf-8') as arquivo:
                for flight in self.flights:
                    arquivo.write(f"{flight.code()}\n")
                    arquivo.write(f"{flight.originCity()}\n")
                    arquivo.write(f"{flight.originCountry()}\n")
                    arquivo.write(f"{flight.destinationCity()}\n")
                    arquivo.write(f"{flight.destinationCountry()}\n")
                    arquivo.write(f"{flight.timeHour()}\n")
                    arquivo.write(f"{flight.timeMinute()}\n")
                    arquivo.write(f"{flight.price()}\n")
                    arquivo.write(f"{flight.seat()}\n")
        except Exception as e:
            print(f"Erro ao atualizar o arquivo: {e}")
