from Flight import Flight
class FlightManager:
    def __init__(self):
        self.flights = []
        try:
            with open("Data/voos.txt", "r" ,encoding='utf-8') as arquivo:
                lines = arquivo.readlines()
                for i in range(0, len(lines), 9):
                    flight = Flight()
                    flight.addFlightCode(int(lines[i].strip()))
                    flight.addOriginCity(str(lines[i + 1].strip()))
                    flight.addOriginCountry(str(lines[i + 2].strip()))
                    flight.addDestinationCity(str(lines[i + 3].strip()))
                    flight.addDestinationCountry(str(lines[i + 4].strip()))
                    flight.addTimeHour(int(lines[i + 5].strip()))
                    flight.addTimeMinute(int(lines[i + 6].strip()))
                    flight.addPrice(float(lines[i + 7].strip()))
                    flight.addSeat(int(lines[i + 8].strip()))
                    self.flights.append(flight)
        except FileNotFoundError:
            print("Erro ao abrir o arquivo voos.txt")

    def changeFlight(self, codigo, seat):
        self.flights[codigo - 1].getSeat(seat)

    def addFlight(self, flight):
        self.flights.append(flight)

    def showFlights(self):
        for flight in self.flights:
            flight.printFlight()

    def returnFlight(self, codigo):
        for flight in self.flights:
            if codigo == flight.code():
                return flight
        return self.flights[codigo]

    def manyFlights(self):
        return len(self.flights)
